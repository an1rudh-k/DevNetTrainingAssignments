import unittest
import json

# class parse_test(unittest.TestCase):


def import_json():

    with open ("dnac_devices.json", "r") as json_obj:
        devices = json.load(json_obj)
    
    return devices['response']

def parse_dict(devices):
    reqd = ["id", "type", "family", "softwareType", "managementIpAddress"]
    for number in range(len(devices)):
        for key in devices[number]:
            if key in reqd:
                print(key + ": " +str(devices[number][key]))
        print("\n")

if __name__ == "__main__":
    devices = import_json()
    parse_dict(devices)
    