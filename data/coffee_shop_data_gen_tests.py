# Purpose: Test coffee shop sales data generator
# Author: Gary A. Stafford and GitHub Copilot
# Date: 2023-04-13
# Usage: pytest coffee_shop_data_gen_tests.py -v

# write a python class that inherits from unittest.TestCase
# write a unit test for the get_product function
# write a unit test for the get_sales_record function
# write a unit test for the write_sales_records function

import csv
import unittest
from datetime import datetime

from coffee_shop_data_gen_final import get_product, get_sales_record, write_data


# write a python class that inherits from unittest.TestCase
class TestCoffeeShop(unittest.TestCase):
    # write a unit test for the get_product function
    def test_get_product(self):
        product = get_product()
        self.assertIn(product["id"], range(1, 25 + 1))
        self.assertGreaterEqual(len(product["product"]), 3)
        self.assertIn(product["calories"], range(0, 512 + 1))
        self.assertGreaterEqual(product["price"], 2.00)
        self.assertLessEqual(product["price"], 7.99)
        self.assertIn(product["type"], ["Food", "Drink"])

    # write a unit test for the get_sales_record function
    def test_get_sales_record(self):
        sale = get_sales_record()
        self.assertIn(sale["id"], range(1, 1000 + 1))
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
        self.assertIn(sale["product_id"], range(1, 25 + 1))
        self.assertGreaterEqual(len(sale["product"]), 3)
        self.assertIn(sale["calories"], range(0, 512 + 1))
        self.assertGreaterEqual(sale["price"], 2.00)
        self.assertLessEqual(sale["price"], 7.00)
        self.assertIn(sale["quantity"], range(1, 3 + 1))
        self.assertIn(sale["type"], ["Food", "Drink"])
        self.assertGreaterEqual(sale["amount"], 2.00 * 1)
        self.assertLessEqual(sale["amount"], 7.99 * 3)
        self.assertIn(sale["payment_type"], [
            "Cash", "Credit", "Debit", "Gift card", "Apple Pay", "Google Pay", "Venmo"])

    # write a unit test for the write_sales_records function
    def test_write_sales_records(self):
        file_name = "output/coffee_shop_sales_data_test.csv"
        write_data(10, file_name)
        
        with open(file_name, "r") as csv_file:
            csv_reader = csv.reader(
                csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
            )
            self.assertEqual(len(list(csv_reader)), 11)


if __name__ == "__main__":
    unittest.main()
