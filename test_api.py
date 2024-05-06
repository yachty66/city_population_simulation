import os
import aiohttp
import asyncio
from dotenv import load_dotenv
import random
import json

# Load the environment variables from the .env file
load_dotenv()

# Now you can safely load your API key
API_KEY = os.getenv("API_KEY")
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
            print(
                f"Invalid content type from {url}: {response.headers['Content-Type']}"
            )
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


def get_age_and_gender():
    population_data = asyncio.run(get_all_population_data())
    people = []
    age_ranges = {
        "20 to 24 years": (20, 24),
        "25 to 29 years": (25, 29),
        "30 to 34 years": (30, 34),
        "35 to 39 years": (35, 39),
        "40 to 44 years": (40, 44),
        "45 to 49 years": (45, 49),
        "50 to 54 years": (50, 54),
        "55 to 59 years": (55, 59),
        "60 to 64 years": (60, 64),
        "65 to 69 years": (65, 69),
        "70 to 74 years": (70, 74),
        "75 to 79 years": (75, 79),
        "80 to 84 years": (80, 84),
    }
    for age_group, data in population_data.items():
        total_population = int(data["total"])
        sample_size = total_population // 100  # 1% of the total population
        for _ in range(sample_size):
            age_min, age_max = age_ranges[age_group]
            age = random.randint(age_min, age_max)
            gender = "Male" if random.random() < 0.5 else "Female"
            person = {"age": age, "gender": gender}
            people.append(person)
    return people


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to fetch data: {response.status}")
                return None

async def get_native_or_foreign_born():
    urls = {
        "not_us_citizen": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0097PE&for=county:075&in=state:06&key={API_KEY}",
        "us_citizen": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0096PE&for=county:075&in=state:06&key={API_KEY}"
    }
    # Fetch data concurrently
    data = await asyncio.gather(
        *(fetch_data(url) for url in urls.values())
    )
    # Map fetched data back to their respective categories
    citizenship_data = {
        "not_us_citizen": data[0][1][1] if data[0] else 'Data not available',
        "us_citizen": data[1][1][1] if data[1] else 'Data not available'
    }
    return citizenship_data

async def get_median_and_mean_income():
    urls = {
        "median_income": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0062E&for=county:075&in=state:06&key={API_KEY}",
        "mean_income": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0063E&for=county:075&in=state:06&key={API_KEY}"
    }
    # Fetch data concurrently
    data = await asyncio.gather(
        *(fetch_data(url) for url in urls.values())
    )
    # Map fetched data back to their respective categories
    income_data = {
        "median_income": data[0][1][1] if data[0] else 'Data not available',
        "mean_income": data[1][1][1] if data[1] else 'Data not available'
    }
    return income_data

async def get_education():
    urls = {
        "high_school_graduate": "https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0062PE&for=county:075&in=state:06&key={API_KEY}",
        "some_college_no_degree": "https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0063PE&for=county:075&in=state:06&key={API_KEY}",
        "associate_degree": "https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0064PE&for=county:075&in=state:06&key={API_KEY}",
        "bachelor_degree": "https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0065PE&for=county:075&in=state:06&key={API_KEY}",
        "graduate_or_professional_degree": "https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0066PE&for=county:075&in=state:06&key={API_KEY}"
    }
    # Fetch data concurrently
    data = await asyncio.gather(
        *(fetch_data(url.format(API_KEY=API_KEY)) for url in urls.values())
    )
    # Map fetched data back to their respective categories
    education_data = {
        "high_school_graduate": data[0][1][1] if data[0] else 'Data not available',
        "some_college_no_degree": data[1][1][1] if data[1] else 'Data not available',
        "associate_degree": data[2][1][1] if data[2] else 'Data not available',
        "bachelor_degree": data[3][1][1] if data[3] else 'Data not available',
        "graduate_or_professional_degree": data[4][1][1] if data[4] else 'Data not available'
    }
    return education_data

# Run the async function and print the results
if __name__ == "__main__":
    result = asyncio.run(get_education())
    print(result)

