"""Regression tests for registry scripts; all writes stay in temporary fixtures.

Run: PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tools/tests -v
"""
import contextlib
from datetime import date
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_links
import register_paper
import sync_registry
from registry_common import card_label, insert_dated_item, list_status, update_catalog, update_listing


def paper(folder='cross-domain/papers/camel', **overrides):
    entry = {
        'id': 'arxiv:2503.18813', 'title': 'Defeating Prompt Injections by Design',
        'year': '2025', 'resource_kind': 'paper', 'content_kind': 'reading',
        'topic_paths': ['cross-domain/agents'], 'catalog_anchor': 'p001',
        'canonical_folder': folder, 'canonical_readme': folder + '/README.md',
        'canonical_path': folder + '/reading.md',
    }
    entry.update(overrides)
    return entry


class FormattingTests(unittest.TestCase):
    def test_kind_and_reading_labels_are_independent(self):
        for kind in ('paper', 'official_technical_report'):
            self.assertEqual(card_label(paper(resource_kind=kind)), '文献卡')
        for kind in ('repository', 'official_blog', 'official_documentation', 'author_article'):
            item = paper(resource_kind=kind, content_kind='bibliographic_card')
            self.assertEqual(card_label(item), '资料卡')
            self.assertEqual(list_status(item), '资料卡，暂无独立精读')
            item['content_kind'] = 'reading'
            self.assertEqual(list_status(item), '技术精读')

    def test_new_day_does_not_extend_historical_section(self):
        text = '# 目录\r\n\r\n## 2026年10月3日文献增量\r\n\r\n- [旧](old)\r\n\r\n## 人工说明\r\n\r\n保留这段\r\n'
        result = insert_dated_item(text, '- [新](new)', date(2026, 10, 4))
        self.assertTrue(result.startswith(text))
        self.assertIn('## 2026年10月4日文献与资料增量\r\n\r\n- [新](new)\r\n', result)
        self.assertNotIn('\n', result.replace('\r\n', ''))

    def test_existing_day_section_is_reused_before_next_section(self):
        text = '# 目录\n\n## 2026年10月4日文献增量\n\n- [当天](same)\n\n手写说明\n\n## 其他\n\n- [其他](other)\n'
        result = insert_dated_item(text, '- [新](new)', date(2026, 10, 4))
        self.assertEqual(result.count('2026年10月4日'), 1)
        self.assertIn('- [当天](same)\n- [新](new)\n\n手写说明', result)
        self.assertTrue(result.endswith('## 其他\n\n- [其他](other)\n'))

    def test_empty_dated_section_has_separate_item(self):
        self.assertEqual(insert_dated_item('## 2026年10月4日资源增量', '- [新](new)', date(2026, 10, 4)),
                         '## 2026年10月4日资源增量\n\n- [新](new)\n')

    def test_camel_placeholder_upgrade_and_manual_suffix(self):
        text = '- [CaMeL（人工简称）](papers/camel/README.md) · 年份见原文 · 文献卡，暂无独立精读 · 保留批注\r\n'
        result = update_listing(text, 'cross-domain/PAPERS.md', [paper()])
        self.assertEqual(result, '- [CaMeL（人工简称）](papers/camel/README.md) · 2025 · 技术精读 · 保留批注\r\n')
        self.assertEqual(update_listing(result, 'cross-domain/PAPERS.md', [paper()]), result)

    def test_cross_domain_year_update_preserves_teaching_status(self):
        text = '- [CaMeL](../cross-domain/papers/camel/README.md#机制) · 2024 · 逐步教学版 · 人工说明\n'
        result = update_listing(text, 'llm/PAPERS.md', [paper()])
        self.assertEqual(result, text.replace('2024', '2025'))

    def test_nonreading_year_update_and_resource_type(self):
        item = paper('cross-domain/resources/guide', resource_kind='official_documentation', content_kind='bibliographic_card')
        text = '- [Guide](resources/guide/README.md) · 年份见原文 · 文献卡，非独立全文精读 · 保留\n'
        result = update_listing(text, 'cross-domain/PAPERS.md', [item])
        self.assertEqual(result, text.replace('年份见原文', '2025').replace('文献卡', '资料卡'))

    def test_reading_downgrade_changes_generated_label_only(self):
        item = paper(content_kind='bibliographic_card')
        text = ('- [CaMeL](papers/camel/README.md) · 2025 · 技术精读 · 保留批注\r\n'
                '- [教学版](papers/camel/README.md) · 2025 · 逐步教学版\r\n'
                '- [自定义](papers/camel/README.md) · 2025 · 技术精读，人工限定范围\r\n')
        result = update_listing(text, 'cross-domain/PAPERS.md', [item])
        self.assertEqual(result, text.replace('技术精读 · 保留批注', '文献卡，暂无独立精读 · 保留批注'))
        self.assertEqual(update_listing(result, 'cross-domain/PAPERS.md', [item]), result)

    def test_curated_rows_unrelated_rows_and_unknown_year_are_preserved(self):
        item = paper('cross-domain/resources/guide', resource_kind='official_documentation', content_kind='bibliographic_card', year='')
        text = '- [Guide](resources/guide/README.md) · 官方技术文档\n- [Other](papers/other/README.md) · 年份见原文 · 文献卡，暂无独立精读\n'
        self.assertEqual(update_listing(text, 'cross-domain/PAPERS.md', [item]), text)
        text = '- [Guide](resources/guide/README.md) · 2020 · 手写说明\n'
        self.assertEqual(update_listing(text, 'cross-domain/PAPERS.md', [item]), text)

    def test_catalog_reconciles_existing_reading_and_preserves_notes(self):
        text = ('# Catalog\r\n共 1 个去重资源（1 篇论文）\r\n\r\n<a id="p001"></a>\r\n'
                '## p001 · Old title\r\n\r\n- 主题：old\r\n- 来源：手工证据\r\n'
                '- [文献卡（尚无独立精读）](../cross-domain/papers/camel/README.md)\r\n\r\n'
                '## 2026年10月3日既有条目更新\r\n\r\n保留记录\r\n')
        result = update_catalog(text, [paper()])
        self.assertIn('- [独立讲解](../cross-domain/papers/camel/reading.md)', result)
        self.assertIn('- 来源：手工证据\r\n', result)
        self.assertTrue(result.endswith('## 2026年10月3日既有条目更新\r\n\r\n保留记录\r\n'))
        self.assertEqual(update_catalog(result, [paper()]), result)
        self.assertNotIn('\n', result.replace('\r\n', ''))

    def test_catalog_resource_label_preserves_boundary(self):
        item = paper('cross-domain/resources/guide', resource_kind='official_documentation', content_kind='bibliographic_card',
                     canonical_path='cross-domain/resources/guide/README.md')
        text = '<a id="p001"></a>\n## p001 · Guide\n- 主题：old\n- [文献卡，暂无独立精读](../cross-domain/resources/guide/README.md)\n'
        result = update_catalog(text, [item])
        self.assertIn('- [资料卡，暂无独立精读](../cross-domain/resources/guide/README.md)', result)


class ScriptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for module in (register_paper, sync_registry, check_links):
            patcher = mock.patch.object(module, 'ROOT', str(self.root))
            patcher.start()
            self.addCleanup(patcher.stop)
        self.write('papers.csv', 'id,title,year,canonical_path,content_kind,resource_kind\r\n')
        self.write('README.md', '收录 0 项资源，其中 0 篇有讲解\r\n')
        self.write('cross-domain/README.md', '本领域收录 0 项资源，其中 0 篇有讲解\r\n')
        self.write('cross-domain/PAPERS.md', '# 目录\r\n\r\n## 2026年10月3日文献增量\r\n\r\n- [旧](papers/old/README.md)\r\n')
        self.write('cross-domain/papers/README.md', '# 论文\r\n')
        self.write('cross-domain/resources/README.md', '# 资料\r\n')
        self.write('docs/paper-catalog.md', '# 目录\r\n\r\n共 0 个去重资源（）\r\n')

    def write(self, name, text):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode('utf-8'))

    def read(self, name):
        return (self.root / name).read_bytes().decode('utf-8')

    def write_json(self, name, data):
        self.write(name, json.dumps(data, ensure_ascii=False, indent=2).replace('\n', '\r\n') + '\r\n')

    def source(self, item):
        source = {k: item[k] for k in ('title', 'year', 'topic_paths', 'resource_kind', 'content_kind')}
        source.update(resource_id=item['id'], official_url='https://example.org/source', modality_tags=['text'], task_tags=['analysis'])
        self.write_json(item['canonical_folder'] + '/source.json', source)
        self.write(item['canonical_folder'] + '/README.md', '# Card\r\n')
        if item['content_kind'] == 'reading':
            self.write(item['canonical_folder'] + '/reading.md', '# Reading\r\n')

    def run_script(self, module, *args):
        output = io.StringIO()
        with mock.patch.object(sys, 'argv', [module.__file__, *args]), contextlib.redirect_stdout(output), mock.patch.object(module.subprocess, 'run') as generator:
            module.main()
        return output.getvalue(), generator

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def test_registration_labels_dates_duplicates_and_root_reading_count(self):
        self.write_json('papers.json', [])
        entries = [paper(), paper('cross-domain/resources/guide', id='url:https://example.org/guide',
                                 title='Guide {with braces}', content_kind='bibliographic_card', resource_kind='official_documentation')]
        for item in entries:
            self.source(item)
        self.run_script(register_paper, '--date', '2026-10-04', *(p['canonical_folder'] for p in entries), entries[0]['canonical_folder'])
        self.assertEqual(len(json.loads(self.read('papers.json'))), 2)
        listing = self.read('cross-domain/PAPERS.md')
        self.assertIn(' · 2025 · 技术精读', listing)
        self.assertIn(' · 2025 · 资料卡，暂无独立精读', listing)
        self.assertLess(listing.index('2026年10月4日'), listing.index('CaMeL') if 'CaMeL' in listing else listing.index('Defeating'))
        self.assertEqual(listing.count('2026年10月4日'), 1)
        self.assertIn('收录 2 项资源，其中 1 篇有讲解', self.read('README.md'))
        self.assertIn('[资料卡]', self.read('docs/paper-catalog.md'))

    def test_register_dry_has_no_writes_or_generator_and_reports_card_kind(self):
        self.write_json('papers.json', [])
        item = paper()
        self.source(item)
        before = self.snapshot()
        output, generator = self.run_script(register_paper, '--dry', '--date', '2026-10-04')
        self.assertEqual(before, self.snapshot())
        self.assertIn('技术精读 | date=2026-10-04', output)
        generator.assert_not_called()

    def test_sync_recovers_stale_reading_link_placeholder_and_is_idempotent(self):
        item = paper(canonical_path='cross-domain/papers/camel/README.md')
        self.source(item)
        self.write_json('papers.json', [item])
        self.write('cross-domain/PAPERS.md', '- [CaMeL](papers/camel/README.md) · 年份见原文 · 文献卡，暂无独立精读 · 手写注释\r\n')
        self.write('cross-domain/papers/README.md', '- [CaMeL](camel/README.md) · 年份见原文 · 文献卡，暂无独立精读\r\n')
        self.write('docs/paper-catalog.md', '<a id="p001"></a>\r\n## p001 · Old\r\n- 主题：old\r\n- [文献卡](../cross-domain/papers/camel/README.md)\r\n')
        before = self.snapshot()
        output, generator = self.run_script(sync_registry, '--dry')
        self.assertEqual(before, self.snapshot())
        generator.assert_not_called()
        self.assertIn('would update cross-domain/PAPERS.md', output)
        self.assertIn('canonical_path:', output)
        self.run_script(sync_registry)
        self.assertIn(' · 2025 · 技术精读 · 手写注释\r\n', self.read('cross-domain/PAPERS.md'))
        self.assertIn(' · 2025 · 技术精读\r\n', self.read('cross-domain/papers/README.md'))
        self.assertIn('[独立讲解](../cross-domain/papers/camel/reading.md)', self.read('docs/paper-catalog.md'))
        first = self.snapshot()
        output, _ = self.run_script(sync_registry)
        self.assertIn('0 field changes', output)
        self.assertIn('0 registry/catalog/list/count files need update', output)
        self.assertEqual(first, self.snapshot())

    def test_sync_reports_stale_lists_even_with_zero_field_changes(self):
        item = paper()
        item.update(modality_tags=['text'], task_tags=['analysis'])
        self.source(item)
        self.write_json('papers.json', [item])
        self.write('cross-domain/PAPERS.md', '- [CaMeL](papers/camel/README.md) · 年份见原文 · 文献卡，暂无独立精读\r\n')
        output, _ = self.run_script(sync_registry, '--dry')
        self.assertIn('0 field changes', output)
        self.assertIn('would update cross-domain/PAPERS.md', output)

    def test_sync_new_reading_updates_old_year_and_placeholder_together(self):
        self.source(paper())
        self.write_json('papers.json', [paper(year='', content_kind='bibliographic_card',
                                           canonical_path='cross-domain/papers/camel/README.md')])
        self.write('cross-domain/PAPERS.md', '- [CaMeL](papers/camel/README.md) · 年份见原文 · 文献卡，暂无独立精读\r\n')
        self.write('cross-domain/papers/README.md', '- [CaMeL](camel/README.md) · 2024 · 文献卡，暂无独立精读\r\n')
        self.run_script(sync_registry)
        for listing in ('cross-domain/PAPERS.md', 'cross-domain/papers/README.md'):
            self.assertIn(' · 2025 · 技术精读\r\n', self.read(listing))
        entry = json.loads(self.read('papers.json'))[0]
        self.assertEqual(entry['year'], '2025')
        self.assertEqual(entry['content_kind'], 'reading')
        self.assertEqual(entry['canonical_path'], 'cross-domain/papers/camel/reading.md')

    def test_sync_downgrade_updates_listing_catalog_and_target_together(self):
        self.source(paper(content_kind='bibliographic_card'))
        self.write_json('papers.json', [paper()])
        self.write('cross-domain/PAPERS.md', '- [CaMeL](papers/camel/README.md) · 2025 · 技术精读 · 手写注释\r\n')
        self.write('docs/paper-catalog.md', '<a id="p001"></a>\r\n## p001 · CaMeL\r\n- 主题：old\r\n- [独立讲解](../cross-domain/papers/camel/reading.md)\r\n')
        self.run_script(sync_registry)
        self.assertIn(' · 2025 · 文献卡，暂无独立精读 · 手写注释\r\n', self.read('cross-domain/PAPERS.md'))
        self.assertIn('[文献卡](../cross-domain/papers/camel/README.md)', self.read('docs/paper-catalog.md'))
        self.assertEqual(json.loads(self.read('papers.json'))[0]['canonical_path'], 'cross-domain/papers/camel/README.md')

    def test_check_links_ignores_templates_only_in_style(self):
        text = '[模板](...) [原文](<官方链接>) [错误](missing.md)\n'
        self.write('STYLE.md', text)
        self.write('article.md', text)
        self.assertEqual(list(check_links.broken_links('STYLE.md')), ['missing.md'])
        self.assertEqual(list(check_links.broken_links('./STYLE.md')), ['missing.md'])
        self.assertEqual(list(check_links.broken_links('article.md')), ['...', '<官方链接>', 'missing.md'])


if __name__ == '__main__':
    unittest.main()
