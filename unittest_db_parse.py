import unittest
from db_parse import parser

class testparser(unittest.TestCase):
    
    def test_json(self):
        filename = "data/db.json"
        parse = parser(filename)
        self.assertEqual(filename, parse.filename)
        self.assertEqual(dict, type(parse.parsed))
    
    def test_xml(self):
        filename = "data/db.xml"
        parse = parser(filename)
        self.assertEqual(filename, parse.filename)
        self.assertEqual(dict, type(parse.parsed))
    
    def test_yaml(self):
        filename = "data/db.yml"
        parse = parser(filename)
        self.assertEqual(filename, parse.filename)
        self.assertEqual(dict, type(parse.parsed))


if __name__ == "__main__":
    unittest.main()