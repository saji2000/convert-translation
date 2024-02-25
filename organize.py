import json

import json
import unicodedata

def split_quran_translation(input_file, output_folder):
    """Splits a large Quran translation JSON file into separate files for each chapter,
    fixing potential Arabic and Persian text encoding issues.

    Args:
        input_file (str): Path to the input JSON file.
        output_folder (str): Path to the folder where the chapter files will be saved.
    """

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        sura_num = item['sura_num']
        output_filename = f"{output_folder}/chapter_{sura_num}.json"

        # Create a new list containing only verses from this chapter
        chapter_data = [verse for verse in data if verse['sura_num'] == sura_num]

        # Apply text normalization to Arabic and Persian text
        for verse in chapter_data:
            verse['arabic_text'] = unicodedata.normalize('NFC', verse['arabic_text'])
            verse['persian_text'] = unicodedata.normalize('NFC', verse['persian_text'])

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            json.dump(chapter_data, outfile, ensure_ascii=False)

if __name__ == "__main__":
    input_file = "translation.json"  # Your input file name
    output_folder = "quran_chapters"       # Folder to store the split files
    split_quran_translation(input_file, output_folder)