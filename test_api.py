# import requests

# url = "https://api.census.gov/data/2022/acs/acs5/subject"
# params = {
#     "get": "NAME,group(S0101)",
#     "for": "zip code tabulation area:94103",
#     "key": "2efba4d1408012ca6cee8294d57a121c87fe51b3",
# }

# response = requests.get(url, params=params)
# data = response.text
# print(data)

"""
https://api.census.gov/data/2022/acs/acs5?get=NAME,B01001_001E&for=zip%20code%20tabulation%20area:94103&key=2efba4d1408012ca6cee8294d57a121c87fe51b3

https://api.census.gov/data/2022/acs/acs5?get=NAME,B01001_001E&for=zip%20code%20tabulation%20area:94103&key=2efba4d1408012ca6cee8294d57a121c87fe51b3

https://api.census.gov/data/2022/acs/acs5?&/subject?get=NAME,S0101&for=zip%20code%20tabulation%20area:94109&key=2efba4d1408012ca6cee8294d57a121c87fe51b3

https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101&for=zip%20code%20tabulation%20area:94109&key=2efba4d1408012ca6cee8294d57a121c87fe51b3

[["NAME","B01001_001E","B01001_001EA","B01001_001M","B01001_001MA","B01001_002E","B01001_002EA","B01001_002M","B01001_002MA","B01001_003E","B01001_003EA","B01001_003M","B01001_003MA","B01001_004E","B01001_004EA","B01001_004M","B01001_004MA","B01001_005E","B01001_005EA","B01001_005M","B01001_005MA","B01001_006E","B01001_006EA","B01001_006M","B01001_006MA","B01001_007E","B01001_007EA","B01001_007M","B01001_007MA","B01001_008E","B01001_008EA","B01001_008M","B01001_008MA","B01001_009E","B01001_009EA","B01001_009M","B01001_009MA","B01001_010E","B01001_010EA","B01001_010M","B01001_010MA","B01001_011E","B01001_011EA","B01001_011M","B01001_011MA","B01001_012E","B01001_012EA","B01001_012M","B01001_012MA","B01001_013E","B01001_013EA","B01001_013M","B01001_013MA","B01001_014E","B01001_014EA","B01001_014M","B01001_014MA","B01001_015E","B01001_015EA","B01001_015M","B01001_015MA","B01001_016E","B01001_016EA","B01001_016M","B01001_016MA","B01001_017E","B01001_017EA","B01001_017M","B01001_017MA","B01001_018E","B01001_018EA","B01001_018M","B01001_018MA","B01001_019E","B01001_019EA","B01001_019M","B01001_019MA","B01001_020E","B01001_020EA","B01001_020M","B01001_020MA","B01001_021E","B01001_021EA","B01001_021M","B01001_021MA","B01001_022E","B01001_022EA","B01001_022M","B01001_022MA","B01001_023E","B01001_023EA","B01001_023M","B01001_023MA","B01001_024E","B01001_024EA","B01001_024M","B01001_024MA","B01001_025E","B01001_025EA","B01001_025M","B01001_025MA","B01001_026E","B01001_026EA","B01001_026M","B01001_026MA","B01001_027E","B01001_027EA","B01001_027M","B01001_027MA","B01001_028E","B01001_028EA","B01001_028M","B01001_028MA","B01001_029E","B01001_029EA","B01001_029M","B01001_029MA","B01001_030E","B01001_030EA","B01001_030M","B01001_030MA","B01001_031E","B01001_031EA","B01001_031M","B01001_031MA","B01001_032E","B01001_032EA","B01001_032M","B01001_032MA","B01001_033E","B01001_033EA","B01001_033M","B01001_033MA","B01001_034E","B01001_034EA","B01001_034M","B01001_034MA","B01001_035E","B01001_035EA","B01001_035M","B01001_035MA","B01001_036E","B01001_036EA","B01001_036M","B01001_036MA","B01001_037E","B01001_037EA","B01001_037M","B01001_037MA","B01001_038E","B01001_038EA","B01001_038M","B01001_038MA","B01001_039E","B01001_039EA","B01001_039M","B01001_039MA","B01001_040E","B01001_040EA","B01001_040M","B01001_040MA","B01001_041E","B01001_041EA","B01001_041M","B01001_041MA","B01001_042E","B01001_042EA","B01001_042M","B01001_042MA","B01001_043E","B01001_043EA","B01001_043M","B01001_043MA","B01001_044E","B01001_044EA","B01001_044M","B01001_044MA","B01001_045E","B01001_045EA","B01001_045M","B01001_045MA","B01001_046E","B01001_046EA","B01001_046M","B01001_046MA","B01001_047E","B01001_047EA","B01001_047M","B01001_047MA","B01001_048E","B01001_048EA","B01001_048M","B01001_048MA","B01001_049E","B01001_049EA","B01001_049M","B01001_049MA","GEO_ID","NAME","us"],

[["NAME","B01001_001E","zip code tabulation area"],

["ZCTA5 08701","134008","08701"]]

"B01001_001E": {
      "label": "Estimate!!Total:",
      "concept": "Sex by Age",
      "predicateType": "int",
      "group": "B01001",
      "limit": 0,
      "attributes": "B01001_001EA,B01001_001M,B01001_001MA"
}

[["NAME","B01001_001E","zip code tabulation area"],
["ZCTA5 08701","134008","08701"]]

- [ ] find the ten for me most interesting criterias
    - 
- [ ] get all the zip codes from SF
- [ ] create json objects
- [ ] generate descriptions 
"""

"""
need to get the data from api, i.e. i need to map data to the url from where i am getting the data from:

for modelling age correctly i need to get the amount of people which are female and amount which is male and than i can calculate the percentage. what i want to do is to 

instead of doing it zip code specific i might just do it city specific cause than i dont have missing data. what can i do now. 

for city simulation i need to take the data from https://data.census.gov/profile/San_Francisco_County,_California?g=050XX00US06075 and than i can 


- age (per age) - int = total population (https://api.census.gov/data/2022/acs/acs5?get=NAME,B01001_001E&for=zip%20code%20tabulation%20area:94103&key=2efba4d1408012ca6cee8294d57a121c87fe51b3) 
- sex - int 
- ancestry - country
- Native and Foreign Born - yes/no
- median income - int
- education - degree title
- commuting
- industry
- rent - int
- disability - kind of disability
- health insurance - yes or no
- married - yes or no
- children - number of children
"""
number_total_population = None

# [["NAME","S0101_C01_001E","state","county"],
# ["San Francisco County, California","851036","06","075"],
# https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_001E&for=county:*&key=YOUR_KEY_GOES_HERE
# https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_001E&for=county:06&key=2efba4d1408012ca6cee8294d57a121c87fe51b3


#https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_006E&for=county:075&in=state:06&key=2efba4d1408012ca6cee8294d57a121c87fe51b3

#well than i will make the male and female ratio 50/50, thn

import os
import aiohttp
import asyncio
from dotenv import load_dotenv
import random
import json

# Load the environment variables from the .env file
load_dotenv()

# Now you can safely load your API key
API_KEY = os.getenv('API_KEY')
print(API_KEY)  # This should pr

age_population_mapper = {
    "20 to 24 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_006E&for=county:075&in=state:06&key={API_KEY}",
    },
    "25 to 29 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_007E&for=county:075&in=state:06&key={API_KEY}",
    },
    "30 to 34 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_008E&for=county:075&in=state:06&key={API_KEY}",
    },
    "35 to 39 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_009E&for=county:075&in=state:06&key={API_KEY}",
    },
    "40 to 44 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_010E&for=county:075&in=state:06&key={API_KEY}",
    },
    "45 to 49 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_011E&for=county:075&in=state:06&key={API_KEY}",
    },
    "50 to 54 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_012E&for=county:075&in=state:06&key={API_KEY}",
    },
    "55 to 59 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_013E&for=county:075&in=state:06&key={API_KEY}",
    },
    "60 to 64 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_014E&for=county:075&in=state:06&key={API_KEY}",
    },
    "65 to 69 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_015E&for=county:075&in=state:06&key={API_KEY}",
    },
    "70 to 74 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_016E&for=county:075&in=state:06&key={API_KEY}",
    },
    "75 to 79 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_017E&for=county:075&in=state:06&key={API_KEY}",
    },
    "80 to 84 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_018E&for=county:075&in=state:06&key={API_KEY}",
    },
}

async def fetch_population_data(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            # Log the error or handle it according to your needs
            print(f"Error fetching data from {url}: {response.status}")
            return None
        try:
            data = await response.json()
            return data[1][1]  # Extract the population value
        except aiohttp.ContentTypeError:
            # Handle cases where the content type is not application/json
            print(f"Invalid content type from {url}: {response.headers['Content-Type']}")
            return None

async def get_all_population_data():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for age_group, data in age_population_mapper.items():
            url = data["total"]
            task = asyncio.create_task(fetch_population_data(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        # Update the dictionary with actual population data
        for (age_group, _), population in zip(age_population_mapper.items(), results):
            age_population_mapper[age_group]["total"] = population
        return age_population_mapper
    
def generate_json_object():
    population_data = asyncio.run(get_all_population_data())
    people = []

    age_ranges = {
        '20 to 24 years': (20, 24),
        '25 to 29 years': (25, 29),
        '30 to 34 years': (30, 34),
        '35 to 39 years': (35, 39),
        '40 to 44 years': (40, 44),
        '45 to 49 years': (45, 49),
        '50 to 54 years': (50, 54),
        '55 to 59 years': (55, 59),
        '60 to 64 years': (60, 64),
        '65 to 69 years': (65, 69),
        '70 to 74 years': (70, 74),
        '75 to 79 years': (75, 79),
        '80 to 84 years': (80, 84)
    }

    for age_group, data in population_data.items():
        total_population = int(data['total'])
        sample_size = total_population // 100  # 1% of the total population

        for _ in range(sample_size):
            age_min, age_max = age_ranges[age_group]
            age = random.randint(age_min, age_max)
            gender = 'Male' if random.random() < 0.5 else 'Female'
            person = {
                'age': age,
                'gender': gender
            }
            people.append(person)

    # Convert the list of people to JSON
    json_output = json.dumps(people, indent=4)
    print(json_output)
    return json_output



generate_json_object()

