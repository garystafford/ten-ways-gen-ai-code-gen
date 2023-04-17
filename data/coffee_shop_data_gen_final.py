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
    parser = argparse.ArgumentParser(
        description="Generate coffee shop sales data")
    parser.add_argument("rec_count",
                        type=int,
                        help="The number of records to generate",
                        default=100)

    rec_count = parser.parse_args().rec_count
    write_data(rec_count)


def get_product():
    """Return one random item from list of dictionaries containing 25 common items sold in a coffee shop

    Returns:
        dict: A dictionary containing the product id, product name, calories, price, and type (food or drink)
    """

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
    random_date = start_date + timedelta(seconds=random.randint(
        0, int((end_date - start_date).total_seconds())), )

    start_time = datetime.strptime("6:00am", "%I:%M%p")
    end_time = datetime.strptime("9:00pm", "%I:%M%p")
    random_time = start_time + timedelta(seconds=random.randint(
        0, int((end_time - start_time).total_seconds())), )

    random_quantity = random.randint(1, 3)

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


def write_data(rec_count, file_name="output/coffee_shop_sales_data.csv"):
    """Write the sales records to a CSV file

    Args:
        rec_count (int): The number of records to write
        file_name (str, optional): The name of the file to write to. Defaults to "output/coffee_shop_sales_data.csv".

        Returns:
            None
    """

    with open(file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file,
                                delimiter=",",
                                quotechar='"',
                                quoting=csv.QUOTE_NONNUMERIC)

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
