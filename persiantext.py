import csv
import json

def update_json_with_persian(csv_file, json_file):
    # Load existing JSON data
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Read Persian data from CSV file and update JSON data
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            chapter_num = int(row['chapter_number'])
            verse_num = int(row['verse_number'])
            persian_text = row['verse_text_persian']
            subtitle = row['verse_subtitle_english']
            footnote = row['verse_footnote_english']

            # Find the corresponding entry in the JSON data and update it
            for entry in data:
                if entry['sura_num'] == chapter_num and entry['verse_num'] == verse_num:
                    entry['persian_text'] = persian_text
                    entry['subtitle'] = subtitle
                    entry['footnote'] = footnote
                    break

    # Write the updated JSON data back to the file
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Replace 'persian_data.csv' and 'output.json' with your Persian CSV input file and the JSON output file path
update_json_with_persian('PersianEnglish.csv', 'output.json')
