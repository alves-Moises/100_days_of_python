from time import time


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, times, cities):
    travel_log.append({"country": country, "Visits": times, "cities": cities})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)