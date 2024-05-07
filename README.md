# city_population_simulation

i guess i can just take each age group and in the case i want to do any surveys i can just adjust them

- [x] attributes i want to take for the population
  - age (per age) - int -
  - sex - int -
  - ancestry - country -
  - Native and Foreign Born - yes/no -
  - median income - int -
  - education - degree title - ONLY APPLICAPLE FOR POPULATION 25 YEARS AND OLDER
  - employment and labor force status - employment rate for population 16 years and over 
  - industry - PART OF THE EMPLOYMENT RATE FROM ABOVE
  - married - yes or no --> only for folks > 18
- [x] all zip codes of san francisco
  - 94102
  - 94103
  - 94104
  - 94105
  - 94107
  - 94108
  - 94109
  - 94110
  - 94111
  - 94112
  - 94114
  - 94115
  - 94116
  - 94117
  - 94118
  - 94121
  - 94122
  - 94123
  - 94124
  - 94127
  - 94129
  - 94130
  - 94131
  - 94132
  - 94133
  - 94134
  - 94158
  - 94188
  - 94501
  - 94920
- [ ] generate all the json objects from the data
- [ ] generate a description for each person and than add the whole row to some data format
- [ ] repeat this for every single zip code
- [ ] upload dataset to kaggle and huggingface
- [ ] share what i just did on twitter

## hackathon goal

make a dataset of the population of san francisco and publish the dataset to kaggle & huggingface and prepare a presentation which shows the use cases of the dataset for defense.

## project description

We are creating a dataset of the population of San Francisco and will publish the dataset on Kaggle and Hugging Face. We will also prepare a presentation showcasing the various use cases of the dataset for defense purposes.

There is demographic data for every ZIP code in San Francisco. Here is an example: https://data.census.gov/profile/ZCTA5_80025?g=860XX00US80025. We need to find all the data via API. All APIs are documented here: https://www.census.gov/data/developers/data-sets.html.

We need to create JSON objects like (these are just random keys):

```json
person_id: {
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "gender": "Male",
  "zip_code": "94103",
  "occupation": "Software Engineer",
  "income": 90000,
  "education_level": "Bachelor's Degree",
  "marital_status": "Single"
}
```

Once we have the persona object, we can run a large language model over the object to create a description similar to how it was done in the following paper: https://arxiv.org/html/2402.17161v1. It will look like:

```md
You are an 85-year-old male, living alone. With a junior high school education, you have experienced a simpler time in life. As an elderly person, you may have children and grandchildren who have moved away, leaving you to navigate the challenges of aging independently.
```

San Francisco has around 800,000 people. We aim to create a synthetic population subset of about 1% of that number, as costs become prohibitively high otherwise. Basically, we try to simulate one percent of the total population from a ZIP code area. For example, visit https://data.census.gov/profile/ZCTA5_80025?g=860XX00US80025. 20% of the population is 65 years old or older; our 1% subset should represent the same statistics.
