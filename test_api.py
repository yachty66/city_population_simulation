import requests

url = "https://api.census.gov/data/2022/acs/acs5/subject"
params = {
    "get": "NAME,group(S0101)",
    "for": "zip code tabulation area:94103",
    "key": "2efba4d1408012ca6cee8294d57a121c87fe51b3",
}

response = requests.get(url, params=params)
data = response.text
print(data)

"""
goal: get all the data for each zip i can see in the GUI via the api

https://api.census.gov/data/2022/acs/acs5?get=NAME,B01001_001E&for=zip%20code%20tabulation%20area:08701&key=2efba4d1408012ca6cee8294d57a121c87fe51b3

[["NAME","B01001_001E","zip code tabulation area"],
["ZCTA5 08701","134008","08701"]]

once i requested data, how can i use the response for seeing the actual useful data? 

https://api.census.gov/data/2022/acs/acs5/profile

we need to get the data from the 
"""
