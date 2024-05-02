import csv
import json

def csv_to_json(csv_file, json_file):
    # Öppna CSV-filen och läs innehållet med rätt teckenkodning
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Skriv JSON-data till json-filen med UTF-8 teckenkodning
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Ange sökvägen till CSV- och JSON-filerna
csv_file = r'C:\Users\svant\OneDrive\Skrivbord\Svante\Projekt\pyhtoncreateprofiles-main\profiles1.csv'
json_file = r'C:\Users\svant\OneDrive\Skrivbord\Svante\Projekt\pyhtoncreateprofiles-main\data.json'

# Konvertera CSV till JSON
csv_to_json(csv_file, json_file)