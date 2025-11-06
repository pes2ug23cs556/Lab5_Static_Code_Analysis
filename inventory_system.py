"""Inventory Management System
Handles adding, removing, loading, saving, and displaying stock data securely.
"""

import json
from datetime import datetime

# Global variable to store inventory data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the inventory with a given quantity."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input: item must be a string and qty must be an integer.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specific quantity of an item from inventory."""
    try:
        if item not in stock_data:
            print(f"Item '{item}' not found in stock.")
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except Exception as e:
        print(f"Error removing item: {e}")


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found. Starting with empty inventory.")
    except json.JSONDecodeError:
        print("Invalid JSON format. Unable to load data.")


def save_data(file="inventory.json"):
    """Save stock data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")


def print_data():
    """Print all items and quantities in inventory."""
    print("\nItems Report:")
    if not stock_data:
        print("No items in inventory.")
    else:
        for item, qty in stock_data.items():
            print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantity below the given threshold."""
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """Main function to test the inventory system."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("mango", 1)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    print("Eval removed — no unsafe execution here.")


if __name__ == "__main__":
    main()
