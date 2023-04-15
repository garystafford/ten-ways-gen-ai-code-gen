# Purpose: Generate user data
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-14
# Usage: python3 user_data_gen.py 100
# Command-line argument(s): rec_count (number of records to generate as an integer)

# Write an application that create a random list of user data.
# Include first name, last name, dob, marital status, and ethinicity.
# Write the data to a csv file.

import random
import argparse
import csv
from datetime import date, timedelta


def main():
    parser = argparse.ArgumentParser(description="Generate user data")
    parser.add_argument(
        "rec_count", type=int, help="The number of records to generate", default=100
    )

    rec_count = parser.parse_args().rec_count
    write_data(rec_count)


# write a function that generates common feminine first names
# return random first name
def get_first_name_feminine():
    first_name_feminine = [
        "Mary",
        "Patricia",
        "Linda",
        "Barbara",
        "Elizabeth",
        "Jennifer",
        "Maria",
        "Susan",
        "Margaret",
        "Dorothy",
        "Lisa",
        "Nancy",
        "Karen",
        "Betty",
        "Helen",
        "Sandra",
        "Donna",
        "Carol",
        "Ruth",
        "Sharon",
        "Michelle",
        "Laura",
        "Sarah",
        "Kimberly",
        "Deborah",
        "Jessica",
        "Shirley",
        "Cynthia",
        "Angela",
        "Melissa",
        "Brenda",
        "Amy",
        "Anna",
        "Rebecca",
        "Virginia",
        "Kathleen",
        "Pamela",
        "Martha",
        "Debra",
        "Amanda",
        "Stephanie",
        "Carolyn",
        "Christine",
        "Marie",
        "Janet",
        "Catherine",
        "Frances",
        "Ann",
        "Joyce",
        "Diane",
        "Alice",
        "Julie",
        "Heather",
        "Teresa",
        "Doris",
        "Gloria",
    ]

    return random.choice(first_name_feminine)


# write a function that generates common masculine first names
# return random first name
def get_first_name_masculine():
    first_names_masculine = [
        "James",
        "John",
        "Robert",
        "Michael",
        "William",
        "David",
        "Richard",
        "Charles",
        "Joseph",
        "Thomas",
        "Christopher",
        "Daniel",
        "Paul",
        "Mark",
        "Donald",
        "George",
        "Kenneth",
        "Steven",
        "Edward",
        "Brian",
        "Ronald",
        "Anthony",
        "Kevin",
        "Jason",
        "Matthew",
        "Gary",
        "Timothy",
        "Jose",
        "Larry",
        "Jeffrey",
        "Frank",
        "Scott",
        "Eric",
        "Stephen",
        "Andrew",
        "Raymond",
        "Gregory",
        "Joshua",
        "Jerry",
        "Dennis",
        "Walter",
        "Patrick",
        "Peter",
        "Harold",
        "Douglas",
        "Henry",
        "Carl",
        "Arthur",
        "Ryan",
        "Roger",
    ]

    return random.choice(first_names_masculine)


# write a function that generates common last names
# return random last name
def get_last_names():
    last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Jones",
        "Brown",
        "Davis",
        "Miller",
        "Wilson",
        "Moore",
        "Taylor",
        "Anderson",
        "Thomas",
        "Jackson",
        "White",
        "Harris",
        "Martin",
        "Thompson",
        "Garcia",
        "Martinez",
        "Robinson",
        "Clark",
        "Rodriguez",
        "Lewis",
        "Lee",
        "Walker",
        "Hall",
        "Allen",
        "Young",
        "Hernandez",
        "King",
        "Wright",
        "Lopez",
        "Hill",
        "Scott",
        "Green",
        "Adams",
        "Baker",
        "Gonzalez",
        "Nelson",
        "Carter",
        "Mitchell",
        "Perez",
        "Roberts",
        "Turner",
        "Phillips",
        "Campbell",
        "Parker",
        "Evans",
        "Edwards",
        "Collins",
    ]

    return random.choice(last_names)


# write a function that returns a martial status
# return random martial status
# 50% chance of being single, 33% chance of being married, 17% chance of being unknown
def get_martial_status():
    martial_status = ["Single", "Single", "Single", "Married", "Married", "Unknown"]

    return random.choice(martial_status)


# write a function that returns a person's ethinicity
# return random ethinicity
# 50% chance of being white, 12.5% chance of being black, 12.5% chance of being hispanic, 12.5% chance of being asian, 12.5% chance of being other
def get_ethinicity():
    ethinicity = ["White", "White", "White", "Black", "Hispanic", "Asian", "Other"]

    return random.choice(ethinicity)


# write a function that generates a normal distribution
# with a mean of 40 and a standard deviation of 10
# return random age
def get_age():
    return int(random.normalvariate(40, 10))


# write a function that generates a random date of birth
# return random date of birth
# with a mean year of 1975 and a standard deviation of 10
def get_dob():
    day_of_year = random.randint(1, 365)
    year_of_birth = int(random.normalvariate(1975, 10))
    dob = date(int(year_of_birth), 1, 1) + timedelta(day_of_year - 1)
    dob = dob.strftime("%Y-%m-%d")
    return dob


# create a function to write the users records to a csv file called users.csv
# use an input parameter to specify the number of records to write
# the csv file must have a header row
# the csv file must be comma delimited
# string values must be enclosed in double quotes
def write_data(rec_count):
    user_id = 0

    with open("users.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
        )

        csv_writer.writerow(
            [
                "user_id",
                "first_name",
                "last_name",
                "dob",
                "martital_status",
                "ethinicity",
            ]
        )

        for i in range(rec_count):
            user_id += 1
            first_name = (
                get_first_name_feminine()
                if random.randint(1, 5) <= 2
                else get_first_name_masculine()
            )
            last_name = get_last_names()
            dob = get_dob()
            martial_status = get_martial_status()
            ethinicity = get_ethinicity()

            csv_writer.writerow(
                [
                    user_id,
                    first_name,
                    last_name,
                    dob,
                    martial_status,
                    ethinicity,
                ]
            )


if __name__ == "__main__":
    main()
