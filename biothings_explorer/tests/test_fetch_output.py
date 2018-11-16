import unittest
from unittest import TestCase

from biothings_explorer_test import fetch_output

class TestFetchOutput(TestCase):

    def test_fetch_output(self):
        data = fetch_output('hgnc.symbol', 'CXCR4', 'chembl.compound')
        self.assertIn('CHEMBL.COMPOUND:CHEMBL16694', [_item['target'] for _item in data])
        self.assertNotIn('CHEMBL.COMPOUND:CHEMBL184618', [_item['target'] for _item in data])
        data1 = fetch_output('hgnc.symbol', 'CXCR4', 'chembl.compound', enable_semantic_search=True)
        self.assertIn('CHEMBL.COMPOUND:CHEMBL184618', [_item[-1]['output']['object']['id'] for _item in data1])
        data2 = fetch_output('hgnc.symbol', 'CX', 'chembl.compound')
        self.assertEqual([], data2)

if __name__ == '__main__':
    unittest.main()
