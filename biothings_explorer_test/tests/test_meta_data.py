from unittest import TestCase

import biothings_explorer_test

class TestMetaData(TestCase):

    def test_list_all_api_resources(self):
        metadata = biothings_explorer_test.MetaData()
        self.assertIn('MyGene.info API', metadata.list_all_api_resources())
        self.assertIn('Pharos API', metadata.list_all_api_resources())

    def test_list_all_endpoints(self):
        metadata = biothings_explorer_test.MetaData()
        self.assertIn("http://MyChem.info/v1/drug/{drugid}", metadata.list_all_endpoints())
        self.assertIn("https://pharos.nih.gov/idg/api/v1/diseases({diseaseid})", metadata.list_all_endpoints())

    def test_list_all_prefixes(self):
        metadata = biothings_explorer_test.MetaData()
        self.assertIn("gene", metadata.list_all_prefixes())
        self.assertIn("ncbigene", metadata.list_all_prefixes()['gene'])
        self.assertIn("uniprot", metadata.list_all_prefixes(group_by_semantic_type=False))

    def test_list_all_semantic_types(self):
        metadata = biothings_explorer_test.MetaData()
        self.assertIn("gene", metadata.list_all_semantic_types())
        self.assertIn("pathway", metadata.list_all_semantic_types())

    def test_list_all_predicates(self):
        metadata = biothings_explorer_test.MetaData()
        self.assertIn("DiseaseOntologyToParentDiseaseOntologyAssociation", metadata.list_all_predicates())
        self.assertIn("EquivalentAssociation", metadata.list_all_predicates())

if __name__ == '__main__':
    unittest.main()
