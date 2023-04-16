# Original OpenAI ChatGPT prompt:
# Create a Python3 program to generate 100 sales for 5 common items sold in a coffee shop.
# The data should be written to a CSV file. The file should include a header row.
# Each record should include the following fields:
#   - id (incrementing integer starting at 1)
#   - date (random date between 1/1/2022 and 12/31/2022)
#   - time (random time between 6:00am and 9:00pm in 1-minute increments)
#   - product_id (incrementing integer starting at 1)
#   - product
#   - calories
#   - price in USD
#   - type (drink or food)
#   - quantity  (random integer between 1 and 3)
#   - amount (price * quantity)
#   - payment type (cash, credit, debit, or gift card)

# Additional prompts:
# Create a function to return one random item from a list of dictionaries 
# containing 15 common drink items sold in a coffee shop including the id, name, calories, price, and type of 'drink'. 
# Capitalize the first letter of each product name. Start product id at 1.

# Create a function to return one random item from a list of dictionaries 
# containing 10 common food items sold in a coffee shop including the id, name, calories, price, and type of 'food'. 
# Capitalize the first letter of each product name. Start product id at 16.

import csv
import random
import datetime

# List of items sold in the coffee shop
items = [
    {"id": 1, "product": "Latte", "calories": 120, "price": 3.50, "type": "drink"},
    {"id": 2, "product": "Cappuccino", "calories": 100, "price": 3.00, "type": "drink"},
    {"id": 3, "product": "Americano", "calories": 5, "price": 2.50, "type": "drink"},
    {"id": 4, "product": "Espresso", "calories": 10, "price": 2.00, "type": "drink"},
    {"id": 5, "product": "Mocha", "calories": 250, "price": 4.00, "type": "drink"},
    {"id": 6, "product": "Iced Coffee", "calories": 80, "price": 2.50, "type": "drink"},
    {"id": 7, "product": "Hot Chocolate", "calories": 300, "price": 3.50, "type": "drink"},
    {"id": 8, "product": "Tea", "calories": 0, "price": 2.00, "type": "drink"},
    {"id": 9, "product": "Frappe", "calories": 450, "price": 5.00, "type": "drink"},
    {"id": 10, "product": "Smoothie", "calories": 200, "price": 4.00, "type": "drink"},
    {"id": 11, "product": "Iced Tea", "calories": 0, "price": 2.50, "type": "drink"},
    {"id": 12, "product": "Lemonade", "calories": 120, "price": 3.00, "type": "drink"},
    {"id": 13, "product": "Hot Tea", "calories": 0, "price": 2.00, "type": "drink"},
    {"id": 14, "product": "Chai Tea", "calories": 200, "price": 3.50, "type": "drink"},
    {"id": 15, "product": "Iced Chai", "calories": 250, "price": 4.00, "type": "drink"},
    {"id": 16, "product": "Croissant", "calories": 231, "price": 2.99, "type": "food"},
    {"id": 17, "product": "Bagel", "calories": 289, "price": 3.49, "type": "food"},
    {"id": 18, "product": "Muffin", "calories": 426, "price": 3.99, "type": "food"},
    {"id": 19, "product": "Sandwich", "calories": 512, "price": 6.99, "type": "food"},
    {"id": 20, "product": "Wrap", "calories": 388, "price": 5.99, "type": "food"},
    {"id": 21, "product": "Salad", "calories": 231, "price": 7.99, "type": "food"},
    {"id": 22, "product": "Quiche", "calories": 456, "price": 4.99, "type": "food"},
    {"id": 23, "product": "Scone", "calories": 335, "price": 2.49, "type": "food"},
    {"id": 24, "product": "Pastry", "calories": 397, "price": 3.99, "type": "food"},
    {"id": 25, "product": "Cake", "calories": 512, "price": 5.99, "type": "food"},
]


# Function to generate a random date between 1/1/2022 and 12/31/2022
def random_date():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)


# Function to generate a random time between 6:00am and 9:00pm in 1-minute increments
def random_time():
    hours = random.randint(6, 21)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return datetime.time(hour=hours, minute=minutes, second=seconds)


# Function to generate a random payment type
def random_payment_type():
    payment_types = ["cash", "credit", "debit", "gift card"]
    return random.choice(payment_types)


# Generate the sales data
sales = []
for i in range(100):
    item = random.choice(items)
    sales.append(
        {
            "id": i + 1,
            "date": random_date().strftime("%m/%d/%Y"),
            "time": random_time().strftime("%I:%M %p"),
            "product_id": i + 1,
            "product": item["product"],
            "calories": item["calories"],
            "price": item["price"],
            "type": item["type"],
            "quantity": random.randint(1, 3),
            "amount": item["price"] * (random.randint(1, 3)),
            "payment_type": random_payment_type(),
        }
    )

# Write the sales data to a CSV file
with open("output/coffee_shop_sales.csv", "w", newline="") as csvfile:
    fieldnames = [
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
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for sale in sales:
        writer.writerow(sale)
