import unittest
import csv
import json

class TestFileContents(unittest.TestCase):

    def test_csv_columns(self):
        with open('profiles1.csv', 'r') as file:
            reader = csv.reader(file)
            columns = next(reader)
            self.assertEqual(len(columns), 12)

    def test_csv_rows(self):
        with open('profiles1.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertTrue(len(rows) >= 900)

    # def test_json_properties(self):
    #     with open('data.json', 'r') as file:
    #         data = json.load(file)
    #         expected_properties = [
    #             "Givenname",
    #             "Surname",
    #             "Streetaddress",
    #             "City",
    #             "Zipcode",
    #             "Country",
    #             "CountryCode",
    #             "NationalId",
    #             "TelephoneCountryCode",
    #             "Telephone",
    #             "Birthday",
    #             "ConsentToContact"
    #         ]
    #         self.assertTrue(all(prop in data for prop in expected_properties))

    def test_json_properties(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            print("Data in JSON file:", data)
            expected_properties = [
                "Givenname",
                "Surname",
                "Streetaddress",
                "City",
                "Zipcode",
                "Country",
                "CountryCode",
                "NationalId",
                "TelephoneCountryCode",
                "Telephone",
                "Birthday",
                "ConsentToContact"
            ]
            print("Expected properties:", expected_properties)
            for obj in data:
                print("Object properties:", obj.keys())
            self.assertTrue(all(prop in obj for obj in data for prop in expected_properties))

    def test_json_rows(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            self.assertTrue(len(data) >= 900)


if __name__ == '__main__':
    unittest.main()