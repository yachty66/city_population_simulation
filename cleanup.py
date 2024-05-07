"""
"description": "\"You are a 68-year-old female resident of San Francisco, USA, who is a US citizen with an income of $112,087. You hold a bachelor's degree, are employed in the finance and insurance, and real estate and rental and leasing industry, and are not married.\""
"""
import json

def clean_description(file_path):
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    # Iterate through each object in the JSON data
    for person in data:
        description = person.get('description', '')
        # Check if the description starts and ends with unwanted characters
        if description.startswith('\"') and description.endswith('\"'):
            # Remove the leading and trailing characters
            person['description'] = description[1:-1]
    # Write the updated JSON data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Call the function with the path to your JSON file
clean_description('people_data.json')