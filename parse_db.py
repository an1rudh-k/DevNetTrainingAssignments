import unittest
import json
import xml.etree.ElementTree as ET
import ruamel.yaml as yaml

        
def import_json():
    
    with open("data/db.json","r") as json_obj:
        json_users = json.load(json_obj)
    
    print(json_users)
    print("\n")
    return json_users

def import_xml():
    
    xml_users = ET.parse("data/db.xml")
    
    root = xml_users.getroot()
    for element in root:
        print (element.tag +  str(element.attrib)) 
        for subelement in element:
            print (subelement.tag + ": " + subelement.text)
    print("\n")

def import_yaml():

    with open("data/db.yml", "r") as yaml_obj:
        yaml_users = yaml.safe_load(yaml_obj)
    
    print(yaml_users)

    return yaml_users

def main():
    import_json()
    import_xml()
    import_yaml()
    

if __name__ == "__main__":
    main()