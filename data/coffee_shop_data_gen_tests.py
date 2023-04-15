# Purpose: Test coffee shop sales data generator
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-13
# Usage: pytest coffee_shop_data_gen_tests.py -v


# write a python class that inherits from unittest.TestCase
# write a setUp method that creates a list of products
# write a unit test for the get_product function
# write a unit test for the get_sales_record function
# write a unit test for the write_sales_records function

import csv
import unittest
from datetime import datetime

from coffee_shop_data_gen_final import (
    get_product, 
    get_sales_record, 
    write_data
)


class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.products = [
            "Coffee", "Espresso", "Cappuccino", "Latte",
            "Americano", "Mocha", "Macchiato", "Hot Chocolate",
            "Tea", "Hot Water", "Scone", "Muffin",
            "Croissant", "Bagel", "Donut", "Danish",
            "Cookie", "Brownie", "Cinnamon Roll", "Pancakes",
            "Waffles", "Oatmeal", "Yogurt", "Fruit", "Cereal",
        ]

    # write a unit test for the get_product function
    def test_get_product(self):
        product = get_product()
        self.assertIn(product["id"], range(1, 26))
        self.assertIn(product["product"], self.products)
        self.assertIn(product["calories"], range(0, 1701))
        self.assertGreaterEqual(product["price"], 1.50)
        self.assertLessEqual(product["price"], 25.00)

    # write a unit test for the get_sales_record function
    def test_get_sales_record(self):
        sale = get_sales_record()
        self.assertIn(sale["id"], range(1, 1001))
        self.assertGreaterEqual(
            datetime.strptime(sale["date"], "%m/%d/%Y"),
            datetime.strptime("01/01/2022", "%m/%d/%Y"),
        )
        self.assertLessEqual(
            datetime.strptime(sale["date"], "%m/%d/%Y"),
            datetime.strptime("12/31/2022", "%m/%d/%Y"),
        )
        self.assertGreaterEqual(
            datetime.strptime(sale["time"], "%I:%M%p"),
            datetime.strptime("6:00am", "%I:%M%p"),
        )
        self.assertLessEqual(
            datetime.strptime(sale["time"], "%I:%M%p"),
            datetime.strptime("9:00pm", "%I:%M%p"),
        )
        self.assertIn(sale["product_id"], range(1, 26))
        self.assertIn(sale["product"], self.products)
        self.assertIn(sale["calories"], range(0, 1701))
        self.assertGreaterEqual(sale["price"], 1.00)
        self.assertLessEqual(sale["price"], 25.00)
        self.assertIn(sale["quantity"], range(1, 4))
        self.assertGreaterEqual(sale["amount"], 1.00 * 1)
        self.assertLessEqual(sale["amount"], 9.00 * 3)

    # write a unit test for the write_sales_records function
    def test_write_sales_records(self):
        write_data(10)
        with open("coffee_shop_sales.csv", "r") as csv_file:
            csv_reader = csv.reader(
                csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
            )
            self.assertEqual(len(list(csv_reader)), 11)


if __name__ == "__main__":
    unittest.main()
