import unittest
from parse_db import import_json
from parse_db import import_yaml

class test_parse(unittest.TestCase):
    def test_import_json(self):
        return_type = import_json()
        self.assertEqual(dict, type(return_type))
    
    def test_import_yaml(self):
        return_type = import_yaml()
        self.assertEqual(dict, type(return_type))
    
if __name__ == "__main__":
    unittest.main()