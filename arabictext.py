import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sura_num = int(row['Sura'])
            verse_num = int(row['Verse'])
            english_text = row['English']
            arabic_text = row['Arabic']

            entry = {
                'sura_num': sura_num,
                'verse_num': verse_num,
                'arabic_text': arabic_text,
                'english_text': english_text,
                'persian_text': "",
            }
            data.append(entry)

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Replace 'input.csv' and 'output.json' with your CSV input file and desired JSON output file path
csv_to_json('ArabicEnglish.csv', 'translation.json')
