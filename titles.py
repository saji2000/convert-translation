import csv
import json

def csv_to_json(csv_file, json_file):
    data = {}
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            chapter_number = int(row['chapter_number'])
            if chapter_number not in data:
                chapter_title_english = row['chapter_title_english']
                chapter_title_arabic = row['chapter_title_arabic']
                chapter_title_persian = row['chapter_title_persian']

                entry = {
                    'chapter_number': chapter_number,
                    'chapter_title_english': chapter_title_english,
                    'chapter_title_arabic': chapter_title_arabic,
                    'chapter_title_persian': chapter_title_persian
                }
                data[chapter_number] = entry

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(list(data.values()), file, indent=4, ensure_ascii=False)

# Replace 'chapter_titles.csv' and 'output.json' with your CSV input file and desired JSON output file path
csv_to_json('PersianEnglish.csv', 'titles.json')
