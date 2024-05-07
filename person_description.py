import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_person_description(person):
    prompt = f"""
    You are an expert ML researcher and prompt engineer. You have been asked with creating a prompt which can be used to simulate a fictional resident of the city San Francisco, USA. 
    This prompt needs to include the attributes from the personality object from {person} — Be as detailed as you need to. 
    You will generate the prompt as a one liner starting with “You are “. Please only return the prompt to use.
    """
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=0.7,
    )
    return chat_completion.choices[0].message.content

def update_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    for person in data:
        person["description"] = generate_person_description(person)
        with open(file_path, "w") as file_to_write:
            json.dump(data, file_to_write, indent=4)

file_path = "people_data.json"
update_json_file(file_path)