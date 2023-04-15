# Purpose: Generate us address data
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-13
# Usage: python3 address_data_gen_final.py 100
# Command-line argument(s): rec_count (number of records to generate as an integer)

# Write an application that create a random list of united states addresses.
# Include address, city, state, zip code, country, and property type.
# Write the data to a csv file.


import csv
import random
from datetime import datetime, timedelta
import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate coffee shop sales data")
    parser.add_argument(
        "rec_count", type=int, help="The number of records to generate", default=100
    )

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


# write a function that creates a list of dictionaries of the largest united states cities
# include the state abbreviations and actual ZIP codes
# returns a random city
def get_city_state_zip():
    city_state_zip = [
        {"city": "Albuquerque", "state": "NM", "zip": "87102"},
        {"city": "Anaheim", "state": "CA", "zip": "92801"},
        {"city": "Anchorage", "state": "AK", "zip": "99501"},
        {"city": "Arlington", "state": "TX", "zip": "76010"},
        {"city": "Atlanta", "state": "GA", "zip": "30303"},
        {"city": "Aurora", "state": "CO", "zip": "80010"},
        {"city": "Austin", "state": "TX", "zip": "78701"},
        {"city": "Bakersfield", "state": "CA", "zip": "93301"},
        {"city": "Baltimore", "state": "MD", "zip": "21202"},
        {"city": "Boston", "state": "MA", "zip": "02108"},
        {"city": "Buffalo", "state": "NY", "zip": "14202"},
        {"city": "Charlotte", "state": "NC", "zip": "28202"},
        {"city": "Chicago", "state": "IL", "zip": "60602"},
        {"city": "Cincinnati", "state": "OH", "zip": "45202"},
        {"city": "Cleveland", "state": "OH", "zip": "44113"},
        {"city": "Colorado Springs", "state": "CO", "zip": "80903"},
        {"city": "Columbus", "state": "OH", "zip": "43215"},
        {"city": "Dallas", "state": "TX", "zip": "75201"},
        {"city": "Denver", "state": "CO", "zip": "80202"},
        {"city": "Detroit", "state": "MI", "zip": "48226"},
        {"city": "El Paso", "state": "TX", "zip": "79901"},
        {"city": "Fort Worth", "state": "TX", "zip": "76102"},
        {"city": "Fresno", "state": "CA", "zip": "93721"},
        {"city": "Houston", "state": "TX", "zip": "77002"},
        {"city": "Indianapolis", "state": "IN", "zip": "46204"},
        {"city": "Jacksonville", "state": "FL", "zip": "32202"},
        {"city": "Kansas City", "state": "MO", "zip": "64102"},
        {"city": "Las Vegas", "state": "NV", "zip": "89101"},
        {"city": "Long Beach", "state": "CA", "zip": "90802"},
        {"city": "Los Angeles", "state": "CA", "zip": "90001"},
        {"city": "Louisville", "state": "KY", "zip": "40202"},
        {"city": "Memphis", "state": "TN", "zip": "38103"},
        {"city": "Mesa", "state": "AZ", "zip": "85201"},
        {"city": "Miami", "state": "FL", "zip": "33128"},
        {"city": "Milwaukee", "state": "WI", "zip": "53202"},
        {"city": "Minneapolis", "state": "MN", "zip": "55402"},
        {"city": "Nashville", "state": "TN", "zip": "37203"},
        {"city": "New York", "state": "NY", "zip": "10007"},
        {"city": "Newark", "state": "NJ", "zip": "07102"},
        {"city": "Oakland", "state": "CA", "zip": "94607"},
        {"city": "Oklahoma City", "state": "OK", "zip": "73102"},
        {"city": "Omaha", "state": "NE", "zip": "68102"},
        {"city": "Philadelphia", "state": "PA", "zip": "19107"},
        {"city": "Phoenix", "state": "AZ", "zip": "85003"},
        {"city": "Pittsburgh", "state": "PA", "zip": "15222"},
        {"city": "Portland", "state": "OR", "zip": "97201"},
        {"city": "Raleigh", "state": "NC", "zip": "27601"},
        {"city": "Sacramento", "state": "CA", "zip": "95814"},
        {"city": "San Antonio", "state": "TX", "zip": "78205"},
        {"city": "San Diego", "state": "CA", "zip": "92101"},
        {"city": "San Francisco", "state": "CA", "zip": "94102"},
        {"city": "San Jose", "state": "CA", "zip": "95113"},
        {"city": "Seattle", "state": "WA", "zip": "98101"},
        {"city": "St. Louis", "state": "MO", "zip": "63102"},
        {"city": "Tampa", "state": "FL", "zip": "33602"},
        {"city": "Tucson", "state": "AZ", "zip": "85701"},
        {"city": "Virginia Beach", "state": "VA", "zip": "23451"},
        {"city": "Washington", "state": "DC", "zip": "20001"},
    ]

    return random.choice(city_state_zip)


# write a function to return a random type of real estate
def get_property_type():
    property_types = [
        "Single Family",
        "Condo",
        "Townhouse",
        "Multi Family",
        "Mobile Home",
        "Vacant Land",
        "Farm",
        "Commercial",
    ]
    return random.choice(property_types)


# create a function to write the address records to a csv file called addresses.csv
# use an input parameter to specify the number of records to write
# the csv file must have a header row
# the csv file must be comma delimited
# string values must be enclosed in double quotes
def write_data(rec_count):
    address_id = 0
    with open("addresses.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
        )

        csv_writer.writerow(
            ["id", "address", "city", "state", "zip", "country", "property_type", "assessed_value"]
        )

        for i in range(rec_count):
            address_id += 1
            street_name = get_street_name()
            street_type = get_street_type()
            city_state_zip = get_city_state_zip()
            property_type = get_property_type()
            csv_writer.writerow(
                [
                    address_id,
                    f"{random.randint(1, 9999)} {street_name} {street_type}",
                    city_state_zip["city"],
                    city_state_zip["state"],
                    city_state_zip["zip"],
                    "United States",
                    property_type,
                    random.randint(50000, 1200000),
                ]
            )


if __name__ == "__main__":
    main()
