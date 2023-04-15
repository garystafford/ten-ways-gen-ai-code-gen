# write a program that creates synthetic sales data for a coffee shop
# the program should accept a command line argument that specifies the number of records to generate
# the program should write the sales data to a file called coffee_shop_sales.csv# the program should contain a main function that calls the other functions
# the program should contain a function that returns one random product from a list of dictionaries
# the program should contain a function that returns a dictionary containing one sales record
# the program should contain a function that writes the sales records to a file

import csv
import random
from datetime import datetime, timedelta
import argparse

sale_id = 0


def main():
    # create a parser object
    parser = argparse.ArgumentParser(description="Generate coffee shop sales data")

    # add a command line argument to specify the number of records to generate
    parser.add_argument(
        "num_recs", type=int, help="The number of records to generate", default=100
    )

    num_recs = parser.parse_args().num_recs

    write_data(num_recs)


# create a function to return one random item from list of dictionaries
# containing 25 common items sold in a coffee shop
# including the product id, product name, calories, and price
# capilize the first letter of each product name
def get_product():
    products = [
        {"id": 1, "product": "Coffee", "calories": 4, "price": 1.50},
        {"id": 2, "product": "Espresso", "calories": 5, "price": 2.00},
        {"id": 3, "product": "Cappuccino", "calories": 20, "price": 3.00},
        {"id": 4, "product": "Latte", "calories": 20, "price": 3.00},
        {"id": 5, "product": "Americano", "calories": 5, "price": 2.00},
        {"id": 6, "product": "Mocha", "calories": 50, "price": 4.00},
        {"id": 7, "product": "Macchiato", "calories": 20, "price": 3.00},
        {"id": 8, "product": "Hot Chocolate", "calories": 100, "price": 3.00},
        {"id": 9, "product": "Tea", "calories": 0, "price": 1.50},
        {"id": 10, "product": "Hot Water", "calories": 0, "price": 1.00},
        {"id": 11, "product": "Scone", "calories": 300, "price": 2.00},
        {"id": 12, "product": "Muffin", "calories": 400, "price": 2.50},
        {"id": 13, "product": "Croissant", "calories": 500, "price": 3.00},
        {"id": 14, "product": "Bagel", "calories": 600, "price": 3.50},
        {"id": 15, "product": "Donut", "calories": 700, "price": 4.00},
        {"id": 16, "product": "Danish", "calories": 800, "price": 4.50},
        {"id": 17, "product": "Cookie", "calories": 900, "price": 5.00},
        {"id": 18, "product": "Brownie", "calories": 1000, "price": 5.50},
        {"id": 19, "product": "Cinnamon Roll", "calories": 1100, "price": 6.00},
        {"id": 20, "product": "Pancakes", "calories": 1200, "price": 6.50},
        {"id": 21, "product": "Waffles", "calories": 1300, "price": 7.00},
        {"id": 22, "product": "Oatmeal", "calories": 1400, "price": 7.50},
        {"id": 23, "product": "Yogurt", "calories": 1500, "price": 8.00},
        {"id": 24, "product": "Fruit", "calories": 1600, "price": 8.50},
        {"id": 25, "product": "Cereal", "calories": 1700, "price": 9.00},
    ]

    # return one random item from list of dictionaries
    return random.choice(products)


# create a function to return a random sales record
# the record should be a dictionary with the following fields:
#   - id (an incrementing integer starting at 1)
#   - date (a random date between 1/1/2022 and 12/31/2022)
#   - time (a random time between 6:00am and 9:00pm)
#   - product_id, product, calories, and price (from the get_product function)
#   - quantity (a random integer between 1 and 3)
#   - amount (price * quantity)
#   - payment type (cash, credit, debit, or gift card)
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
        seconds=random.randint(0, int((end_date - start_date).total_seconds())),
    )

    # get a random time between 6:00am and 9:00pm
    start_time = datetime.strptime("6:00am", "%I:%M%p")
    end_time = datetime.strptime("9:00pm", "%I:%M%p")
    random_time = start_time + timedelta(
        # Get a random number of seconds between 0 and the number of seconds between start_time and end_time
        seconds=random.randint(0, int((end_time - start_time).total_seconds())),
    )

    # get a random quantity between 1 and 3
    random_quantity = random.randint(1, 3)

    # get a random payment type (cash, credit, debit, or gift card)
    random_payment_type = random.choice(["cash", "credit", "debit", "gift card"])

    sales_record = {
        "id": sale_id,
        "date": random_date.strftime("%m/%d/%Y"),
        "time": random_time.strftime("%I:%M%p"),
        "product_id": product["id"],
        "product": product["product"],
        "calories": product["calories"],
        "price": product["price"],
        "quantity": random_quantity,
        "amount": product["price"] * random_quantity,
        "payment_type": random_payment_type,
    }

    return sales_record


# create a function to write the sales records to a csv file called coffee_shop_sales.csv
# use an input parameter to specify the number of records to write
# the csv file must have a header row
# the csv file must be comma delimited
# string values must be enclosed in double quotes
def write_data(rec_count):
    # open the file for writing
    with open("coffee_shop_sales.csv", "w", newline="") as csv_file:
        # create a csv writer object
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # write the header row
        csv_writer.writerow(
            [
                "id",
                "date",
                "time",
                "product_id",
                "product",
                "calories",
                "price",
                "quantity",
                "amount",
                "payment_type",
            ]
        )

        # write the sales records
        for i in range(rec_count):
            sale = get_sales_record()
            csv_writer.writerow(
                [
                    sale["id"],
                    sale["date"],
                    sale["time"],
                    sale["product_id"],
                    sale["product"],
                    sale["calories"],
                    sale["price"],
                    sale["quantity"],
                    sale["amount"],
                    sale["payment_type"],
                ]
            )


if __name__ == "__main__":
    main()