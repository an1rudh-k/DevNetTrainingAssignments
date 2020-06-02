import json
from db_get_dnac_devices import get_details 

class parser:

    def __init__ (self, filename):
        self.filename = filename
        self.parsed = None

        self.dnac_parser()
    
    def dnac_parser(self):
        file = self.filename

        reqd = ['family', 'type', 'id', 'managementIpAddress', 'softwareType']

        with open(file, 'r') as json_obj:
            json_dict = json.load(json_obj)
        
        devices = json_dict['response']

        parse_list = []

        for num in range(len(devices)):
            parse_dict = {}
            for key in devices[num]:
                if key in reqd:
                    parse_dict.update({key: devices[num][key]})
            parse_list.append(parse_dict)
        
        self.parsed = parse_list
        

if __name__ == "__main__":
    detail = get_details()
    parse = parser(detail.db_filename)
    print(parse.parsed)