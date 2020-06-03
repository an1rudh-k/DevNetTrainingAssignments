#!/usr/bin/python3
print("Content-Type:text/html")
print("")

import cgi,cgitb
cgitb.enable() # Enable debugging
print("<h1>Below is the execution output of the script</h1>")
print("------------------------------------<br>")

##-------PASTE YOUR SCRIPT BELOW---------#######

import json
from db_get_dnac_devices import get_details 

class parser:

    def __init__ (self, database):
        self.db = database
        self.parsed = None

        self.dnac_parser()
    
    def dnac_parser(self):

        reqd = ['family', 'type', 'id', 'managementIpAddress', 'softwareType']

        json_dict = self.db
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
    parse = parser(detail.db)
    print("<p1>Token: {}</p2>".format(detail.token))
    print("<p2>Required response: {}</p2>".format(parse.parsed))