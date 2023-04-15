# Purpose: Generate coffee shop sales data
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-12
# Usage: python3 coffee_shop_data_gen_final.py 100
# Command-line argument(s): rec_count (number of records to generate as an integer)

import csv
import random
from datetime import datetime, timedelta
import argparse

sale_id = 0


def main():
    parser = argparse.ArgumentParser(description="Generate coffee shop sales data")
    parser.add_argument(
        "rec_count", type=int, help="The number of records to generate", default=100
    )

    rec_count = parser.parse_args().rec_count
    write_data(rec_count)


def get_product():
    """Return one random item from list of dictionaries
    containing 25 common items sold in a coffee shop

    Returns:
        dict: A dictionary containing the product id, product name, calories, and price
    """

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

    return random.choice(products)


def get_sales_record():
    """Return a random sales record as a dictionary

    Returns:
        dict: A dictionary containing a random sales record
    """

    product = get_product()

    global sale_id
    sale_id += 1

    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())),
    )

    start_time = datetime.strptime("6:00am", "%I:%M%p")
    end_time = datetime.strptime("9:00pm", "%I:%M%p")
    random_time = start_time + timedelta(
        seconds=random.randint(0, int((end_time - start_time).total_seconds())),
    )

    random_quantity = random.randint(1, 3)

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


def write_data(rec_count):
    """Write the sales records to a file called coffee_shop_sales.csv

    Args:
        rec_count (int): The number of records to write

        Returns:
            None
    """

    with open("coffee_shop_sales.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
        )

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
