# Purpose: Generate user data
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-14
# Usage: python3 user_data_gen.py 100
# Command-line argument(s): rec_count (number of records to generate as an integer)

# Write an application that create a random list of user data.
# Include first name, last name, dob, gender, religion, and race
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


# write a function that generates common feminine first names in the United States
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


# write a function that generates common masculine first names in the United States
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
        "Joe",
        "Juan",
        "Jack",
        "Albert",
        "Jonathan",
        "Justin",
        "Terry",
        "Gerald",
        "Keith",
        "Samuel",
        "Willie",
        "Ralph",
        "Lawrence",
        "Nicholas",
        "Roy",
    ]

    return random.choice(first_names_masculine)


# write a function that returns a feminine or masculine first name
# return random first name
# accept a random value between 0 and 1
# 32% chance of being feminine, 68% chance of being masculine
def get_first_name(rnd_value):
    if rnd_value < 0.32:
        return get_first_name_feminine()
    else:
        return get_first_name_masculine()


# write a function that generates common last names in the United States
# return random last name
def get_last_name():
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
        "Stewart",
        "Sanchez",
        "Morris",
        "Rogers",
        "Reed",
        "Cook",
        "Morgan",
        "Bell",
        "Murphy",
        "Bailey",
        "Rivera",
        "Cooper",
        "Richardson",
        "Cox",
        "Howard",
        "Ward",
        "Torres",
        "Peterson",
        "Gray",
        "Ramirez",
        "James",
        "Watson",
        "Brooks",
        "Kelly",
        "Sanders",
        "Price",
        "Bennett",
        "Wood",
        "Barnes",
        "Ross",
        "Henderson",
        "Coleman",
        "Jenkins",
        "Perry",
        "Powell",
        "Long",
        "Patterson",
        "Hughes",
        "Flores",
        "Washington",
        "Butler",
        "Simmons",
        "Foster",
        "Gonzales",
        "Bryant",
        "Alexander",
        "Russell",
        "Griffin",
    ]

    return random.choice(last_names)


# write a function that returns a martial status
# return random martial status
# accept a random value between 0 and 1
# 50% chance of being married,
# 33% chance of being single,
# 17% chance of being unknown
def get_martial_status(rnd_value):
    if rnd_value < 0.50:
        return "Married"
    elif rnd_value < 0.83:
        return "Single"
    else:
        return "Unknown"


# write a function that returns a person's rache
# return random race
# accept a random value between 0 and 1
# 58% chance of being white,
# 19% chance of being hispanic,
# 12% chance of being black,
# 6% chance of being asian,
# 4% chance of being multiracial
def get_race(rnd_value):
    if rnd_value < .58:
        return "White"
    elif rnd_value < .77:
        return "Hispanic"
    elif rnd_value < .89:
        return "Black"
    elif rnd_value < .95:
        return "Asian"
    else:
        return "Multiracial"


# write a function that returns a person's regilion
# return random regilion
# accept a random value between 0 and 1
# 70% chance of being christian,
# 20% chance of being agnostic,
# 3% chance of being atheist,
# 2% chance of being jewish,
# 2% chance of being other,
# 1% chance of being muslim,
# 1% chance of being hindu,
# 1% chance of being buddhist
def get_regilion(rnd_value):
    if rnd_value < 0.7:
        return "Christian"
    elif rnd_value < 0.9:
        return "Agnostic"
    elif rnd_value < 0.93:
        return "Atheist"
    elif rnd_value < 0.95:
        return "Jewish"
    elif rnd_value < 0.97:
        return "Other"
    elif rnd_value < 0.98:
        return "Muslim"
    elif rnd_value < 0.99:
        return "Hindu"
    else:
        return "Buddhist"


# write a function that returns a person's gender
# return a random gender
# accept a random value between 0 and 1
# 40% chace of being female,
# 53% chance of being male,
# 6% chance of being other,
# 1% chance of being transgender
def get_gender(rnd_value):
    if rnd_value < 0.53:
        return "Male"
    elif rnd_value < 0.93:
        return "Feamle"
    elif rnd_value < 0.99:
        return "Other"
    else:
        return "Transgener"


# # write a function that generates a normal distribution
# # with a mean of 40 and a standard deviation of 10
# # return random age
# def get_age():
#     return int(random.normalvariate(40, 10))


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

    with open("output/users.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
        )

        csv_writer.writerow(
            [
                "user_id",
                "first_name",
                "last_name",
                "dob",
                "gender",
                "martital_status",
                "race",
            ]
        )

        for i in range(rec_count):
            rnd_value = random.random()

            user_id += 1
            first_name = get_first_name(rnd_value)
            last_name = get_last_name()
            dob = get_dob()
            gender = get_gender(rnd_value)
            martial_status = get_martial_status(rnd_value)
            race = get_race(rnd_value)

            csv_writer.writerow(
                [
                    user_id,
                    first_name,
                    last_name,
                    dob,
                    gender,
                    martial_status,
                    race,
                ]
            )


if __name__ == "__main__":
    main()
