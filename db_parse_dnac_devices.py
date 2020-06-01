import json


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
        

def main():
    parse = parser("data/dnac_devices.json")
    print(parse.parsed)

if __name__ == "__main__":
    main()