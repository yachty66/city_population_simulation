# city_population_simulation

- [ ] find api for getting the same data for each zip code wich is available on gov site
  - [ ] make sample request for getting data from an specified zip code
- [ ] create personality profile template for all the data which is available in the api
- [ ] find out what a good number of % is from the zip code for modelling
- [ ] use this percentage for creating the subpopulation
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

