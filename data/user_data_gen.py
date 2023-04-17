# Purpose: Generate user data
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-14
# Usage: python3 user_data_gen.py 100
# Command-line argument(s): rec_count (number of records to generate as an integer)

# Write an application that create a random list of user data.
# The application should accept a command line argument that specifies the number of records to generate.
# The application should write the user data to a file called 'user_data.csv'.
# The application should contain the following functions:
#   - main() function that calls the other functions
#   - function that returns a random first name
#   - function that returns a random last name
#   - function that returns a random date of birth
#   - function that returns a random gender
#   - function that returns a random regilious affiliation
#   - function that returns a random race


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


# Write a function that generates common feminine first names in the United States.
# List should be in alphabetical order.
# Each name should be unique.
# Return random first name.
def get_first_name_feminine():
    first_name_feminine = [
        "Alice", "Amanda", "Amy", "Angela", "Ann", "Anna", "Barbara", "Betty",
        "Brenda", "Carol", "Carolyn", "Catherine", "Christine", "Cynthia", "Deborah", "Debra",
        "Diane", "Donna", "Doris", "Dorothy", "Elizabeth", "Frances", "Gloria", "Heather",
        "Helen", "Janet", "Jennifer", "Jessica", "Joyce", "Julie", "Karen", "Kathleen", "Kimberly",
        "Laura", "Linda", "Lisa", "Margaret", "Maria", "Marie", "Martha", "Mary", "Melissa",
        "Michelle", "Nancy", "Pamela", "Patricia", "Rebecca", "Ruth", "Sandra", "Sarah", "Sharon",
        "Shirley", "Stephanie", "Susan", "Teresa", "Virginia",
    ]

    return random.choice(first_name_feminine)


# Write a function that generates common masculine first names in the United States.
# List should be in alphabetical order.
# Each name should be unique.
# Return random first name.
def get_first_name_masculine():
    first_names_masculine = [
        "Adams", "Alexander", "Allen", "Anderson", "Bailey", "Baker", "Barnes", "Bell",
        "Bennett", "Brooks", "Brown", "Bryant", "Butler", "Campbell", "Carter", "Clark",
        "Coleman", "Collins", "Cook", "Cooper", "Cox", "Davis", "Edwards", "Evans",
        "Flores", "Foster", "Garcia", "Gonzales", "Gonzalez", "Gray", "Green", "Griffin",
        "Hall", "Harris", "Henderson", "Hernandez", "Hill", "Howard", "Hughes", "Jackson",
        "James", "Jenkins", "Johnson", "Jones", "Kelly", "King", "Lee", "Lewis", "Long",
        "Lopez", "Martin", "Martinez", "Miller", "Mitchell", "Moore", "Morgan", "Morris",
        "Murphy", "Nelson", "Parker", "Patterson", "Perez", "Perry", "Peterson", "Phillips",
        "Powell", "Price", "Ramirez", "Reed", "Richardson", "Rivera", "Roberts", "Robinson",
        "Rodriguez", "Rogers", "Ross", "Russell", "Sanchez", "Sanders", "Scott", "Simmons",
        "Smith", "Stewart", "Taylor", "Thomas", "Thompson", "Torres", "Turner", "Walker",
        "Ward", "Washington", "Watson", "White", "Williams", "Wilson", "Wood", "Wright", "Young"
    ]

    return random.choice(first_names_masculine)


# Write a function that returns a person's gender.
# Return a random gender.
# Accept a random value between 0 and 1 as an input parameter.
# The function must return one of the following values based on the %:
# 53% Male, 40% Female, 6% Other, 1% Transgender
def get_gender(rnd_value):
    if rnd_value < 0.53:
        return "Male"
    elif rnd_value < 0.93:
        return "Feamle"
    elif rnd_value < 0.99:
        return "Other"
    else:
        return "Transgener"

# Write a function that returns a feminine or masculine first name.
# Return random first name.
# Accept a random value between 0 and 1 as an input parameter.
# The function must return one of the following values based on the %:
# 53% chance of being feminine, 40% chance of being masculine
def get_first_name(rnd_value):
    if rnd_value < 0.53:
        return get_first_name_masculine()
    elif rnd_value < 0.93:
        return get_first_name_feminine()
    elif rnd_value < 0.97:
        return get_first_name_masculine()
    else:
        return get_first_name_feminine()


# Write a function that generates common last names in the United States.
# List should be in alphabetical order.
# Each name should be unique.
# Return random last name.
def get_last_name():
    last_names = [
        "Adams", "Alexander", "Allen", "Anderson", "Bailey", "Baker", "Barnes", "Bell",
        "Bennett", "Brooks", "Brown", "Bryant", "Butler", "Campbell", "Carter", "Clark",
        "Coleman", "Collins", "Cook", "Cooper", "Cox", "Davis", "Edwards", "Evans", "Flores",
        "Foster", "Garcia", "Gonzales", "Gonzalez", "Gray", "Green", "Griffin", "Hall",
        "Harris", "Henderson", "Hernandez", "Hill", "Howard", "Hughes", "Jackson", "James",
        "Jenkins", "Johnson", "Jones", "Kelly", "King", "Lee", "Lewis", "Long", "Lopez",
        "Martin", "Martinez", "Miller", "Mitchell", "Moore", "Morgan", "Morris", "Murphy",
        "Nelson", "Parker", "Patterson", "Perez", "Perry", "Peterson", "Phillips", "Powell",
        "Price", "Ramirez", "Reed", "Richardson", "Rivera", "Roberts", "Robinson", "Rodriguez",
        "Rogers", "Ross", "Russell", "Sanchez", "Sanders", "Scott", "Simmons", "Smith", "Stewart",
        "Taylor", "Thomas", "Thompson", "Torres", "Turner", "Walker", "Ward", "Washington", "Watson",
        "White", "Williams", "Wilson", "Wood", "Wright", "Young",
    ]

    return random.choice(last_names)


# Write a function that returns a martial status.
# Return random martial status.
# Accept a random value between 0 and 1 as an input parameter.
# The function must return one of the following values based on the %:
# 50% Married, 33% Single, 17% Unknown
def get_martial_status(rnd_value):
    if rnd_value < 0.50:
        return "Married"
    elif rnd_value < 0.83:
        return "Single"
    else:
        return "Unknown"


# Write a function that returns a person's race.
# Return random race.
# Accept a random value between 0 and 1 as an input parameter.
# The function must return one of the following values based on the %:
# 58% White, 19% Hispanic, 12% Black, 6% Asian, 4% Multiracial
def get_race(rnd_value):
    if rnd_value < 0.58:
        return "White"
    elif rnd_value < 0.77:
        return "Hispanic"
    elif rnd_value < 0.89:
        return "Black"
    elif rnd_value < 0.95:
        return "Asian"
    else:
        return "Multiracial"


# Write a function that returns a person's regilion.
# Return random regilion.
# Accept a random value between 0 and 1 as an input parameter.
# The function must return one of the following values based on the %:
# 70% Christian, 20% Agnostic, 3% Atheist, 2% Jewish,
# 2% Other, 1% Muslim, 1% Hindu, 1% Buddhist
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


# Write a function that returns a person's gender.
# Return a random gender.
# Accept a random value between 0 and 1 as an input parameter.
# The function must return one of the following values based on the %:
# 53% Male, 40% Female, 6% Other, 1% Transgender
def get_gender(rnd_value):
    if rnd_value < 0.53:
        return "Male"
    elif rnd_value < 0.93:
        return "Feamle"
    elif rnd_value < 0.99:
        return "Other"
    else:
        return "Transgener"


# Write a function that generates a normal distribution of ages.
# Using normalvariate() from the random module
# with a mean of 40 and a standard deviation of 10.
# Return random age as an integer.
def get_age():
    return int(random.normalvariate(40, 10))


# Write a function that generates a random date of birth.
# Return random date of birth as a string in the format YYYY-MM-DD
# with a mean year of 1975 and a standard deviation of 10.
def get_dob():
    day_of_year = random.randint(1, 365)
    year_of_birth = int(random.normalvariate(1975, 10))
    dob = date(int(year_of_birth), 1, 1) + timedelta(day_of_year - 1)
    dob = dob.strftime("%Y-%m-%d")
    return dob


# Create a function to write the users records to a csv file called 'users.csv'.
# Use an input parameter to specify the number of records to write.
# The csv file must have a header row and be comma delimited.
# String values must be enclosed in double quotes.
def write_data(rec_count):
    user_id = 0

    with open("output/user_data.csv", "w", newline="") as csv_file:
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
                "religion"
            ]
        )

        for i in range(rec_count):
            rnd_gender = random.random()

            user_id += 1
            first_name = get_first_name(rnd_gender)
            last_name = get_last_name()
            dob = get_dob()
            gender = get_gender(rnd_gender)
            martial_status = get_martial_status(random.random())
            race = get_race(random.random())
            religion = get_regilion(random.random())

            csv_writer.writerow(
                [
                    user_id,
                    first_name,
                    last_name,
                    dob,
                    gender,
                    martial_status,
                    race,
                    religion
                ]
            )


if __name__ == "__main__":
    main()
