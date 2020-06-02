import unittest
from db_get_dnac_devices import get_details

class get_test(unittest.TestCase):

    def test_get(self):
        getit = get_details()
        username = "dnacdev"
        password = "D3v93T@wK!"
        self.assertEqual(username, getit.username)
        self.assertEqual(password, getit.password)
        self.assertEqual(str, type(getit.token))
        self.assertEqual(dict, type(getit.db))

if __name__ == "__main__":
    unittest.main()
