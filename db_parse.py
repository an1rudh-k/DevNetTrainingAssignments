import json
import xml.etree.ElementTree as ET
import ruamel.yaml as yaml

class parser:

    def __init__(self, filename):
        self.filename = filename
        self.parsed = None
        
        if filename == "data/db.json":
            self.json_parser()
        
        elif filename == "data/db.xml":
            self.xml_parser()
        
        elif filename == "data/db.yml":
            self.yaml_parser()

    def json_parser(self):
        file = self.filename
        
        with open(file, 'r') as json_obj:
            json_dict = json.load(json_obj)
        
        self.parsed = json_dict

    def xml_parser(self):
        file = self.filename

        parse_xml = ET.parse(file)
        root = parse_xml.getroot()
        
        xml_dict = {}

        for elements in root:
            xml_dict[elements.tag] = {}
            
            if elements.attrib:
                xml_dict[elements.tag]['attribute'] = elements.attrib
            
            for subelements in elements:
                xml_dict[elements.tag][subelements.tag] = subelements.text
        
        self.parsed = xml_dict

    def yaml_parser(self):
        file = self.filename

        with open(file, 'r') as yaml_obj:
            yaml_dict = yaml.safe_load(yaml_obj)
        
        self.parsed = yaml_dict

def main():
    parsed_dict = {}
    parse = parser("data/db.json")
    parsed_dict.update(parse.parsed)
    parse = parser('data/db.xml')
    parsed_dict.update(parse.parsed)
    parse = parser("data/db.yml")
    parsed_dict.update(parse.parsed)
    print(parsed_dict)

if __name__ == "__main__":
    main()