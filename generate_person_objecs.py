import os
import aiohttp
import asyncio
from dotenv import load_dotenv
import random
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

age_population_mapper = {
    "Under 5 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_002E&for=county:075&in=state:06&key={API_KEY}",
    },
    "5 to 9 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_003E&for=county:075&in=state:06&key={API_KEY}",
    },
    "10 to 14 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_004E&for=county:075&in=state:06&key={API_KEY}",
    },
    "15 to 19 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_005E&for=county:075&in=state:06&key={API_KEY}",
    },
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
    "80 to 84 years": {
        "total": f"https://api.census.gov/data/2022/acs/acs5/subject?get=NAME,S0101_C01_019E&for=county:075&in=state:06&key={API_KEY}",
    },
}


async def fetch_population_data(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Error fetching data from {url}: {response.status}")
            return None
        try:
            data = await response.json()
            return data[1][1]
        except aiohttp.ContentTypeError:
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
        for (age_group, _), population in zip(age_population_mapper.items(), results):
            age_population_mapper[age_group]["total"] = population
        return age_population_mapper


async def get_age_and_gender():
    population_data = await get_all_population_data()
    people = []
    age_ranges = {
        "Under 5 years": (0, 5),
        "5 to 9 years": (5, 9),
        "10 to 14 years": (10, 14),
        "15 to 19 years": (15, 19),
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
        sample_size = total_population // 100
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
        "us_citizen": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0096PE&for=county:075&in=state:06&key={API_KEY}",
    }
    data = await asyncio.gather(*(fetch_data(url) for url in urls.values()))
    citizenship_data = {
        "not_us_citizen": data[0][1][1] if data[0] else "Data not available",
        "us_citizen": data[1][1][1] if data[1] else "Data not available",
    }
    return citizenship_data


async def get_median_and_mean_income():
    urls = {
        "median_income": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0062E&for=county:075&in=state:06&key={API_KEY}",
        "mean_income": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0063E&for=county:075&in=state:06&key={API_KEY}",
    }
    data = await asyncio.gather(*(fetch_data(url) for url in urls.values()))
    income_data = {
        "median_income": data[0][1][1] if data[0] else "Data not available",
        "mean_income": data[1][1][1] if data[1] else "Data not available",
    }
    return income_data


async def get_education():
    urls = {
        "high_school_graduate": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0062PE&for=county:075&in=state:06&key={API_KEY}",
        "some_college_no_degree": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0063PE&for=county:075&in=state:06&key={API_KEY}",
        "associate_degree": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0064PE&for=county:075&in=state:06&key={API_KEY}",
        "bachelor_degree": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0065PE&for=county:075&in=state:06&key={API_KEY}",
        "graduate_or_professional_degree": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0066PE&for=county:075&in=state:06&key={API_KEY}",
    }
    data = await asyncio.gather(
        *(fetch_data(url.format(API_KEY=API_KEY)) for url in urls.values())
    )
    education_data = {
        "high_school_graduate": data[0][1][1] if data[0] else "Data not available",
        "some_college_no_degree": data[1][1][1] if data[1] else "Data not available",
        "associate_degree": data[2][1][1] if data[2] else "Data not available",
        "bachelor_degree": data[3][1][1] if data[3] else "Data not available",
        "graduate_or_professional_degree": (
            data[4][1][1] if data[4] else "Data not available"
        ),
    }
    return education_data


async def employment_labor_force_status():
    """
    Population 16 years and over employment rate
    """
    url = f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0004PE&for=county:075&in=state:06&key={API_KEY}"
    data = await fetch_data(url)
    if data and len(data) > 1 and len(data[1]) > 1:
        employment_rate = data[1][1]
    else:
        employment_rate = "Data not available"
    return {"employment_rate": employment_rate}


async def get_industry():
    urls = {
        "Agriculture, forestry, fishing and hunting, and mining": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0033PE&for=county:075&in=state:06&key={API_KEY}",
        "Construction": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0034PE&for=county:075&in=state:06&key={API_KEY}",
        "Manufacturing": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0035PE&for=county:075&in=state:06&key={API_KEY}",
        "Wholesale trade": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0036PE&for=county:075&in=state:06&key={API_KEY}",
        "Retail trade": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0037PE&for=county:075&in=state:06&key={API_KEY}",
        "Transportation and warehousing, and utilities": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0038PE&for=county:075&in=state:06&key={API_KEY}",
        "Information": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0039PE&for=county:075&in=state:06&key={API_KEY}",
        "Finance and insurance, and real estate and rental and leasing": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0040PE&for=county:075&in=state:06&key={API_KEY}",
        "Professional, scientific, and management, and administrative and waste management services": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0041PE&for=county:075&in=state:06&key={API_KEY}",
        "Educational services, and health care and social assistance": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0042PE&for=county:075&in=state:06&key={API_KEY}",
        "Arts, entertainment, and recreation, and accommodation and food services": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0043PE&for=county:075&in=state:06&key={API_KEY}",
        "Other services, except public administration": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0044PE&for=county:075&in=state:06&key={API_KEY}",
        "Public administration": f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP03_0045PE&for=county:075&in=state:06&key={API_KEY}",
    }
    data = await asyncio.gather(
        *(fetch_data(url.format(API_KEY=API_KEY)) for url in urls.values())
    )
    industry_data = {
        category: data[i][1][1] if data[i] else "Data not available"
        for i, category in enumerate(urls)
    }
    return industry_data


async def get_married_status():
    url = f"https://api.census.gov/data/2022/acs/acs1/profile?get=NAME,DP02_0002PE&for=county:075&in=state:06&key={API_KEY}"
    data = await fetch_data(url.format(API_KEY=API_KEY))
    if data and len(data) > 1 and len(data[1]) > 1:
        married_status = data[1][1]
    else:
        married_status = "Data not available"
    return {"married_status": married_status}


async def main():
    native_foreign_data = await get_native_or_foreign_born()
    income_data = await get_median_and_mean_income()
    education_data = await get_education()
    employment_data = await employment_labor_force_status()
    industry_data = await get_industry()
    married_status_data = await get_married_status()
    people = await get_age_and_gender()
    not_us_citizen_percentage = float(native_foreign_data["not_us_citizen"])
    us_citizen_percentage = float(native_foreign_data["us_citizen"])
    employment_rate = float(employment_data["employment_rate"])
    married_status_percentage = float(married_status_data["married_status"])
    income_range_percentage = 20
    median_income = int(income_data["median_income"])
    json_objects = []
    for person in people:
        is_foreign_born = random.choices(
            ["Non US citizen", "US citizen"],
            weights=[not_us_citizen_percentage, us_citizen_percentage],
            k=1,
        )[0]
        person_data = {
            "age": person["age"],
            "gender": person["gender"],
            "native_or_foreign_born": is_foreign_born,
        }
        if person["age"] >= 25:
            income_variation = (
                random.randint(-income_range_percentage, income_range_percentage)
                / 100.0
            )
            income = int(median_income * (1 + income_variation))
            person_data["income"] = income
            education_levels = [
                "high_school_graduate",
                "some_college_no_degree",
                "associate_degree",
                "bachelor_degree",
                "graduate_or_professional_degree",
            ]
            weights = [float(education_data[level]) for level in education_levels]
            education = random.choices(education_levels, weights=weights, k=1)[0]
            person_data["degree"] = education
        if person["age"] >= 16:
            is_employed = random.choices(
                ["Employed", "Unemployed"],
                weights=[employment_rate, 100 - employment_rate],
                k=1,
            )[0]
            person_data["employment"] = is_employed
            if is_employed == "Employed":
                industry_names = list(industry_data.keys())
                industry_weights = [
                    float(industry_data[industry]) for industry in industry_names
                ]
                industry_assigned = random.choices(
                    industry_names, weights=industry_weights, k=1
                )[0]
                person_data["industry"] = industry_assigned
        if person["age"] >= 18:
            is_married = random.choices(
                ["Married", "Not Married"],
                weights=[married_status_percentage, 100 - married_status_percentage],
                k=1,
            )[0]
            person_data["married_status"] = is_married
        json_objects.append(person_data)
    json_data = json.dumps(json_objects, indent=4)
    with open("people_data.json", "w") as file:
        file.write(json_data)
    print("Data written to 'people_data.json'")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
