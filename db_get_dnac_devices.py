import requests 
import json
import base64

class get_details:

    def __init__(self):
        self.token = None
        self.db_filename = "data/db_dnac_api.json"
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
        
        self.token = json.loads(response.text.encode('utf8'))['Token']
        
    def get_db(self):

        url = self.url + "dna/intent/api/v1/network-device"
        header = {'x-auth-token': self.token}

        response = requests.get(url, headers=header)

        self.db = json.loads(response.text.encode('utf8'))

        with open(self.db_filename, "w") as json_obj:
            json.dump(self.db, json_obj, indent=4)

    
if __name__ == "__main__":
    get_dnac = get_details()