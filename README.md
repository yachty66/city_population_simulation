# City Population Simulation

This repository provides a dataset of synthetic residents of San Francisco.

## Method

The dataset is created based on US Census Bureau data at [San Francisco County, California Census Data](https://data.census.gov/profile/San_Francisco_County,_California?g=050XX00US06075). In the first step, JSON objects representing the real data were created. The keys of a full object consist of age, gender, native_or_foreign_born, income, degree, employment, industry, and married_status. An example is:

```json
{
    "age": 26,
    "gender": "Male",
    "native_or_foreign_born": "US citizen",
    "income": 164030,
    "degree": "graduate_or_professional_degree",
    "employment": "Employed",
    "industry": "Educational services, and health care and social assistance",
    "married_status": "Married"
}
```

Not all objects contain the same keys due to the following conditional logic applied during their generation:

-  **Income and Education**: These attributes are only included for residents aged 25 and above.
-  **Employment**: Included for residents aged 16 and above.
-  **Marital Status**: Only considered for residents aged 18 and above.
-  **Industry**: Only considered if the resident is also employed.
-  **Degree**: This attribute is included for individuals aged 25 and above.

This conditional inclusion of attributes ensures that the dataset realistically mirrors the varying availability of demographic data across different age groups.

The created objects represent 1% of the real society of San Francisco to save money for the LLM use later. After all objects were created, an LLM is used to create descriptions for each individual JSON object based on its values. An example object with a simulated persona looks as follows:

```json
{
    "age": 26,
    "gender": "Male",
    "native_or_foreign_born": "US citizen",
    "income": 164030,
    "degree": "graduate_or_professional_degree",
    "employment": "Employed",
    "industry": "Educational services, and health care and social assistance",
    "married_status": "Married",
    "description": "You are a 26-year-old male resident of San Francisco, USA, who is a US citizen with an income of $164,030. You hold a graduate or professional degree, are employed in the educational services, health care, and social assistance industry, and are married."
}
```




