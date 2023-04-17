# Purpose: Generate US residential address data
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-13
# Usage: python3 address_data_gen_final.py 100
# Command-line argument(s): rec_count (number of records to generate as an integer)

# Write an application that create a random list of united states addresses.
# Include address, city, state, zip code, country, and property type.
# Write the data to a csv file.


import csv
import random
import argparse

cities_final = []


def main():
    parser = argparse.ArgumentParser(description="Generate coffee shop sales data")
    parser.add_argument(
        "rec_count", type=int, help="The number of records to generate", default=100
    )

    # 1x at start
    cities = get_cities()
    prepare_cities(cities)

    rec_count = parser.parse_args().rec_count
    write_data(rec_count)


# write a function that creates a list of unique street names in the united states
# returns a random street name
def get_street_name():
    street_names = [
        "Ash",
        "Bend",
        "Bluff",
        "Branch",
        "Bridge",
        "Broadway",
        "Brook",
        "Burg",
        "Bury",
        "Canyon",
        "Cape",
        "Cedar",
        "Cove",
        "Creek",
        "Crest",
        "Crossing",
        "Dale",
        "Dam",
        "Divide",
        "Downs",
        "Elm",
        "Estates",
        "Falls",
        "Fifth",
        "First",
        "Fork",
        "Fourth",
        "Glen",
        "Green",
        "Grove",
        "Harbor",
        "Heights",
        "Hickory",
        "Hill",
        "Hollow",
        "Island",
        "Isle",
        "Knoll",
        "Lake",
        "Landing",
        "Lawn",
        "Main",
        "Manor",
        "Maple",
        "Meadow",
        "Meadows",
        "Mill",
        "Mills",
        "Mission",
        "Mount",
        "Mountain",
        "Oak",
        "Oaks",
        "Orchard",
        "Park",
        "Parkway",
        "Pass",
        "Path",
        "Pike",
        "Pine",
        "Place",
        "Plain",
        "Plains",
        "Port",
        "Prairie",
        "Ridge",
        "River",
        "Road",
        "Rock",
        "Rocks",
        "Second",
        "Seventh",
        "Shoals",
        "Shore",
        "Shores",
        "Sixth",
        "Skyway",
        "Spring",
        "Springs",
        "Spur",
        "Station",
        "Summit",
        "Sunset",
        "Terrace",
        "Third",
        "Trace",
        "Track",
        "Trail",
        "Tunnel",
        "Turnpike",
        "Vale",
        "Valley",
        "View",
        "Village",
        "Ville",
        "Vista",
        "Walk",
        "Way",
        "Well",
        "Wells",
        "Wood",
        "Woods",
        "Worth",
    ]

    return random.choice(street_names)


# write a function that creates a list of unique street types in the united states
# returns a random street type
def get_street_type():
    street_types = [
        "Alley",
        "Avenue",
        "Bend",
        "Bluff",
        "Boulevard",
        "Branch",
        "Bridge",
        "Brook",
        "Burg",
        "Circle",
        "Commons",
        "Court",
        "Drive",
        "Highway",
        "Lane",
        "Parkway",
        "Place",
        "Road",
        "Square",
        "Street",
        "Terrace",
        "Trail",
        "Way",
    ]

    return random.choice(street_types)


def prepare_cities(cities):
    total_population = 0  # 51,035,885
    for city in cities:
        total_population += city["population"]

    for city in cities:
        city["population_pcnt"] = city["population"] / total_population

    global cities_final
    cities_final = sorted(cities, key=lambda d: d["population"], reverse=True)

    running_total = 1
    for city in cities_final:
        running_total -= city["population_pcnt"]
        city["running_total"] = running_total


# write a function that creates a list of dictionaries
# of the largest cities in the united states
# include the city, state abbreviation, zip code, and population
# return all cities
def get_cities():
    cities = [
        {"city": "Albuquerque", "state": "NM", "zip": "87102", "population": 559277},
        {"city": "Anaheim", "state": "CA", "zip": "92801", "population": 345012},
        {"city": "Anchorage", "state": "AK", "zip": "99501", "population": 291826},
        {"city": "Arlington", "state": "TX", "zip": "76010", "population": 398121},
        {"city": "Atlanta", "state": "GA", "zip": "30303", "population": 486290},
        {"city": "Aurora", "state": "CO", "zip": "80010", "population": 325078},
        {"city": "Austin", "state": "TX", "zip": "78701", "population": 931830},
        {"city": "Bakersfield", "state": "CA", "zip": "93301", "population": 372576},
        {"city": "Baltimore", "state": "MD", "zip": "21202", "population": 602495},
        {"city": "Boston", "state": "MA", "zip": "02108", "population": 667137},
        {"city": "Buffalo", "state": "NY", "zip": "14202", "population": 258959},
        {"city": "Charlotte", "state": "NC", "zip": "28202", "population": 872498},
        {"city": "Chicago", "state": "IL", "zip": "60602", "population": 2695598},
        {"city": "Cincinnati", "state": "OH", "zip": "45202", "population": 296943},
        {"city": "Cleveland", "state": "OH", "zip": "44113", "population": 390113},
        {"city": "Colorado Springs", "state": "CO", "zip": "80903", "population": 456568},
        {"city": "Columbus", "state": "OH", "zip": "43215", "population": 822553},
        {"city": "Dallas", "state": "TX", "zip": "75201", "population": 1345047},
        {"city": "Denver", "state": "CO", "zip": "80202", "population": 682545},
        {"city": "Detroit", "state": "MI", "zip": "48226", "population": 672662},
        {"city": "El Paso", "state": "TX", "zip": "79901", "population": 674433},
        {"city": "Fort Worth", "state": "TX", "zip": "76102", "population": 792727},
        {"city": "Fresno", "state": "CA", "zip": "93721", "population": 509924},
        {"city": "Houston", "state": "TX", "zip": "77002", "population": 2296224},
        {"city": "Indianapolis", "state": "IN", "zip": "46204", "population": 843393},
        {"city": "Jacksonville", "state": "FL", "zip": "32202", "population": 842583},
        {"city": "Kansas City", "state": "MO", "zip": "64102", "population": 467007},
        {"city": "Las Vegas", "state": "NV", "zip": "89101", "population": 603488},
        {"city": "Long Beach", "state": "CA", "zip": "90802", "population": 462257},
        {"city": "Los Angeles", "state": "CA", "zip": "90001", "population": 3971883},
        {"city": "Louisville", "state": "KY", "zip": "40202", "population": 609893},
        {"city": "Memphis", "state": "TN", "zip": "38103", "population": 653450},
        {"city": "Mesa", "state": "AZ", "zip": "85201", "population": 508958},
        {"city": "Miami", "state": "FL", "zip": "33128", "population": 463347},
        {"city": "Milwaukee", "state": "WI", "zip": "53202", "population": 594833},
        {"city": "Minneapolis", "state": "MN", "zip": "55402", "population": 410939},
        {"city": "Nashville", "state": "TN", "zip": "37203", "population": 654610},
        {"city": "New York", "state": "NY", "zip": "10007", "population": 8405837},
        {"city": "Newark", "state": "NJ", "zip": "07102", "population": 281944},
        {"city": "Oakland", "state": "CA", "zip": "94607", "population": 406253},
        {"city": "Oklahoma City", "state": "OK", "zip": "73102", "population": 631346},
        {"city": "Omaha", "state": "NE", "zip": "68102", "population": 434353},
        {"city": "Philadelphia", "state": "PA", "zip": "19107", "population": 1526006},
        {"city": "Phoenix", "state": "AZ", "zip": "85003", "population": 1445632},
        {"city": "Pittsburgh", "state": "PA", "zip": "15222", "population": 305841},
        {"city": "Portland", "state": "OR", "zip": "97201", "population": 609456},
        {"city": "Raleigh", "state": "NC", "zip": "27601", "population": 403892},
        {"city": "Sacramento", "state": "CA", "zip": "95814", "population": 479686},
        {"city": "San Antonio", "state": "TX", "zip": "78205", "population": 1327407},
        {"city": "San Diego", "state": "CA", "zip": "92101", "population": 1307402},
        {"city": "San Francisco", "state": "CA", "zip": "94102", "population": 805235},
        {"city": "San Jose", "state": "CA", "zip": "95113", "population": 998537},
        {"city": "Seattle", "state": "WA", "zip": "98101", "population": 608660},
        {"city": "St. Louis", "state": "MO", "zip": "63102", "population": 319294},
        {"city": "Tampa", "state": "FL", "zip": "33602", "population": 335709},
        {"city": "Tucson", "state": "AZ", "zip": "85701", "population": 520116},
        {"city": "Virginia Beach", "state": "VA", "zip": "23451", "population": 448479},
        {"city": "Washington", "state": "DC", "zip": "20001", "population": 601723},
    ]

    return cities

# write a function to return a random city
# accept a random value between 0 and 1 as an input parameter
def get_city(rnd_value):
    for city in cities_final:
        if rnd_value >= city["running_total"]:
            return city


# write a function to return a random type of real estate
# the function must return one of the following values:
# 63% single-family,
# 26% multi-family,
# 4% condo,
# 3% townhouse,
# 2% mobile home,
# 1% farm
# 1% other
# accept a random value between 0 and 1 as an input parameter
def get_property_type(rnd_value):
    if rnd_value < 0.63:
        return "Single-family"
    elif rnd_value < 0.89:
        return "Multi-family"
    elif rnd_value < 0.93:
        return "Condo"
    elif rnd_value < 0.96:
        return "Townhouse"
    elif rnd_value < 0.98:
        return "Mobile home"
    elif rnd_value < 0.99:
        return "Farm"
    else:
        return "Other"


# create a function to write the address records to a csv file called addresses.csv
# use an input parameter to specify the number of records to write
# the csv file must have a header row
# the csv file must be comma delimited
# string values must be enclosed in double quotes
def write_data(rec_count):
    address_id = 0
    with open("output/addresses.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
        )

        csv_writer.writerow(
            [
                "id",
                "address",
                "city",
                "state",
                "zip",
                "country",
                "property_type",
                "assessed_value",
            ]
        )

        for i in range(rec_count):
            rnd_value = random.random()
            address_id += 1
            street_name = get_street_name()
            street_type = get_street_type()
            street_address = f"{random.randint(1, 9999)} {street_name} {street_type}"
            city_state_zip = get_city(rnd_value)
            country = "United States"
            property_type = get_property_type(rnd_value)
            assessed_value = random.randint(50000, 1200000)

            csv_writer.writerow(
                [
                    address_id,
                    street_address,
                    city_state_zip["city"],
                    city_state_zip["state"],
                    city_state_zip["zip"],
                    country,
                    property_type,
                    assessed_value,
                ]
            )


if __name__ == "__main__":
    main()
