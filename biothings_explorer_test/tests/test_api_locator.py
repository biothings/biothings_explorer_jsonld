from unittest import TestCase

import biothings_explorer_test

class TestAPILocator(TestCase):

    def test_locate_apis_by_input_output_semantic_types(self):
        locator = biothings_explorer_test.APILocator()
        # test cases when user give the wrong semantic type info
        self.assertEqual(locator.locate_apis_by_input_output_semantic_types('gene', 'chemical1'), [])
        # test cases when user give the right semantic type info and there are apis connecting them
        self.assertGreater(len(locator.locate_apis_by_input_output_semantic_types('gene', 'chemical')), 0)

    def test_locate_apis_by_input_semantic_type_only(self):
        locator = biothings_explorer_test.APILocator()
        test_result = locator.locate_apis_by_input_semantic_type_only('gene')
        subject_prefix_list = [_doc['object']['prefix'] for _doc in test_result]
        self.assertIn('pubchem.bioassay', subject_prefix_list)

    def test_locate_apis_by_output_semantic_type_only(self):
        locator = biothings_explorer_test.APILocator()
        test_result = locator.locate_apis_by_output_semantic_type_only('gene')
        subject_prefix_list = [_doc['object']['prefix'] for _doc in test_result]
        self.assertIn('reactome.complex', subject_prefix_list)

    def test_locate_apis_by_input_output_prefix(self):
        locator = biothings_explorer_test.APILocator()
        test_result = locator.locate_apis_by_input_output_prefix('ncbigene', 'uberon')
        self.assertIn('https://api.monarchinitiative.org/api/bioentity/gene/{geneid}/expression/anatomy', [_doc['endpoint'] for _doc in test_result])

    def test_locate_connected_apis_by_input_output_prefix(self):
        locator = biothings_explorer_test.APILocator()
        test_result = locator.locate_connected_apis_by_input_output_prefix('ncbigene', 'uberon', max_api=2)
        self.assertGreater(len(test_result), 0)
        self.assertEqual(test_result[0][0]['subject']['prefix'], 'ncbigene')
        self.assertEqual(test_result[-1][-1]['object']['prefix'], 'uberon')
        test_result1 = locator.locate_connected_apis_by_input_output_prefix('hgnc.symbol', 'uberon', max_api=1)
        self.assertEqual(len(test_result1), 0)

if __name__ == '__main__':
    unittest.main()
