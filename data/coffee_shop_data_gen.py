# Purpose: Generate coffee shop sales data
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-12
# Usage: python3 coffee_shop_data_gen.py 100
# Command-line argument(s): rec_count (number of records to generate as an integer)

# Write a program that creates synthetic sales data for a coffee shop.
# The program should accept a command line argument that specifies the number of records to generate.
# The program should write the sales data to a file called 'coffee_shop_sales.csv'.
# The program should contain a main function that calls the other functions.
# The program should contain a function that returns one random product from a list of dictionaries.
# The program should contain a function that returns a dictionary containing one sales record.
# The program should contain a function that writes the sales records to a file.

import csv
import random
from datetime import datetime, timedelta
import argparse

sale_id = 0


def main():
    # create a parser object
    parser = argparse.ArgumentParser(
        description="Generate coffee shop sales data")

    # add a command line argument to specify the number of records to generate
    parser.add_argument("num_recs",
                        type=int,
                        help="The number of records to generate",
                        default=100)

    num_recs = parser.parse_args().num_recs

    write_data(num_recs)


# Write a function to create list of dictionaries.
# The list of dictionaries should contain 15 drink items and 10 food items sold in a coffee shop.
# Include the product id, product name, calories, price, and type (food or drink).
# Capilize the first letter of each product name.
# Return a random item from the list of dictionaries.
def get_product():
    products = [
        {"id": 1, "product": "Latte", "calories": 120, "price": 3.50, "type": "Drink"},
        {"id": 2, "product": "Cappuccino", "calories": 100, "price": 3.00, "type": "Drink"},
        {"id": 3, "product": "Americano", "calories": 5, "price": 2.50, "type": "Drink"},
        {"id": 4, "product": "Espresso", "calories": 10, "price": 2.00, "type": "Drink"},
        {"id": 5, "product": "Mocha", "calories": 250, "price": 4.00, "type": "Drink"},
        {"id": 6, "product": "Iced Coffee", "calories": 80, "price": 2.50, "type": "Drink"},
        {"id": 7, "product": "Hot Chocolate", "calories": 300, "price": 3.50, "type": "Drink"},
        {"id": 8, "product": "Tea", "calories": 0, "price": 2.00, "type": "Drink"},
        {"id": 9, "product": "Frappe", "calories": 450, "price": 5.00, "type": "Drink"},
        {"id": 10, "product": "Smoothie", "calories": 200, "price": 4.00, "type": "Drink"},
        {"id": 11, "product": "Iced Tea", "calories": 0, "price": 2.50, "type": "Drink"},
        {"id": 12, "product": "Lemonade", "calories": 120, "price": 3.00, "type": "Drink"},
        {"id": 13, "product": "Hot Tea", "calories": 0, "price": 2.00, "type": "Drink"},
        {"id": 14, "product": "Chai Tea", "calories": 200, "price": 3.50, "type": "Drink"},
        {"id": 15, "product": "Iced Chai", "calories": 250, "price": 4.00, "type": "Drink"},
        {"id": 16, "product": "Croissant", "calories": 231, "price": 2.99, "type": "Food"},
        {"id": 17, "product": "Bagel", "calories": 289, "price": 3.49, "type": "Food"},
        {"id": 18, "product": "Muffin", "calories": 426, "price": 3.99, "type": "Food"},
        {"id": 19, "product": "Sandwich", "calories": 512, "price": 6.99, "type": "Food"},
        {"id": 20, "product": "Wrap", "calories": 388, "price": 5.99, "type": "Food"},
        {"id": 21, "product": "Salad", "calories": 231, "price": 7.99, "type": "Food"},
        {"id": 22, "product": "Quiche", "calories": 456, "price": 4.99, "type": "Food"},
        {"id": 23, "product": "Scone", "calories": 335, "price": 2.49, "type": "Food"},
        {"id": 24, "product": "Pastry", "calories": 397, "price": 3.99, "type": "Food"},
        {"id": 25, "product": "Cake", "calories": 512, "price": 5.99, "type": "Food"},
    ]

    # return one random item from list of dictionaries
    return random.choice(products)


# Write a function to return a random sales record.
# The record should be a dictionary with the following fields:
#   - id (an incrementing integer starting at 1)
#   - date (a random date between 1/1/2022 and 12/31/2022)
#   - time (a random time between 6:00am and 9:00pm in 1 minute increments)
#   - product_id, product, calories, price, and type (from the get_product function)
#   - quantity (a random integer between 1 and 3)
#   - amount (price * quantity)
#   - payment type (Cash, Credit, Debit, Gift Card, Apple Pay, Google Pay, or Venmo)
def get_sales_record():
    # get a random product
    product = get_product()

    # sale_id is an incrementing integer starting at 1
    global sale_id
    sale_id += 1

    # get a random date between 1/1/2022 and 12/31/2022
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_date = start_date + timedelta(
        # Get a random number of seconds between 0 and the number of seconds between start_date and end_date
        seconds=random.randint(0, int(
            (end_date - start_date).total_seconds())), )

    # get a random time between 6:00am and 9:00pm
    start_time = datetime.strptime("6:00am", "%I:%M%p")
    end_time = datetime.strptime("9:00pm", "%I:%M%p")
    random_time = start_time + timedelta(
        # Get a random number of seconds between 0 and the number of seconds between start_time and end_time
        seconds=random.randint(0, int(
            (end_time - start_time).total_seconds())), )

    # get a random quantity between 1 and 3
    random_quantity = random.randint(1, 3)

    # get a random payment type:
    # Cash, Credit, Debit, Gift card, Apple Pay, Google Pay, Venmo
    random_payment_type = random.choice(
        ["Cash", "Credit", "Debit", "Gift card", "Apple Pay", "Google Pay", "Venmo"])

    sales_record = {
        "id": sale_id,
        "date": random_date.strftime("%m/%d/%Y"),
        "time": random_time.strftime("%I:%M%p"),
        "product_id": product["id"],
        "product": product["product"],
        "calories": product["calories"],
        "price": product["price"],
        "type": product["type"],
        "quantity": random_quantity,
        "amount": product["price"] * random_quantity,
        "payment_type": random_payment_type,
    }

    return sales_record


# Write a function to write the sales records to a CSV file called 'coffee_shop_sales.csv'.
# Use an input parameter to specify the number of records to write.
# The CSV file must have a header row and be comma delimited.
# All string values must be enclosed in double quotes.
def write_data(rec_count):
    # open the file for writing
    with open("output/coffee_shop_sales.csv", "w", newline="") as csv_file:
        # create a csv writer object
        csv_writer = csv.writer(csv_file,
                                delimiter=",",
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        # write the header row
        # id,date,time,product_id,product,calories,price,type,quantity,amount,payment_type
        csv_writer.writerow([
            "id",
            "date",
            "time",
            "product_id",
            "product",
            "calories",
            "price",
            "type",
            "quantity",
            "amount",
            "payment_type",
        ])

        # write the sales records
        for i in range(rec_count):
            sale = get_sales_record()
            csv_writer.writerow([
                sale["id"],
                sale["date"],
                sale["time"],
                sale["product_id"],
                sale["product"],
                sale["calories"],
                sale["price"],
                sale["type"],
                sale["quantity"],
                sale["amount"],
                sale["payment_type"],
            ])


if __name__ == "__main__":
    main()
