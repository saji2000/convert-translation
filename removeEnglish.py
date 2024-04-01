import json

# Load the JSON data from the file
with open('translation.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate over each object in the array and remove the "English_text" key
for item in data:
    item.pop('english_text', None)

# Write the modified data back to the file
with open('new_translation.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
