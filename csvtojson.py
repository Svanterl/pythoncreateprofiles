import csv
import json
import os

def csv_to_json(csv_file, json_file):
    # Ange den fullständiga sökvägen till CSV-filen
    csv_file_path = os.path.join(os.getenv('GITHUB_WORKSPACE', '.'), csv_file)

    # Öppna CSV-filen och läs innehållet med rätt teckenkodning
    with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Ange den fullständiga sökvägen till JSON-filen
    json_file_path = os.path.join(os.getenv('GITHUB_WORKSPACE', '.'), json_file)

    # Skriv JSON-data till json-filen med UTF-8 teckenkodning
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Ange sökvägen till CSV- och JSON-filerna
csv_file = 'profiles1.csv'
json_file = 'data.json'

# Konvertera CSV till JSON
csv_to_json(csv_file, json_file)