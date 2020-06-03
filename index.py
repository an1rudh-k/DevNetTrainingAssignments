#!/usr/bin/python3
print("Content-Type:text/html")
print("")

import cgi,cgitb
cgitb.enable() # Enable debugging
print("<h1>Below is the execution output of the script</h1>")
print("------------------------------------<br>")

##-------PASTE YOUR SCRIPT BELOW---------#######

import requests 
import json
import base64

class get_details:

    def __init__(self):
        self.token = None
        self.db_filename = "db_dnac_api.json"
        self.db = None

        self.url = "https://sandboxdnac2.cisco.com/"
        self.username = "dnacdev"
        self.password = "D3v93T@wK!"

        self.get_token()

        self.get_db()
    
    def get_token(self):

        url = self.url + "api/system/v1/auth/token"
        authentication = requests.auth.HTTPBasicAuth(self.username, self.password)

        response = requests.post(url, auth=authentication)
        
        self.token = response.json()['Token']
        
    def get_db(self):

        url = self.url + "dna/intent/api/v1/network-device"
        header = {'x-auth-token': self.token}

        response = requests.get(url, headers=header)

        self.db = response.json()
    
if __name__ == "__main__":
    get_dnac = get_details()
    print("<h1>Token: {}</h1>".format(get_dnac.token))