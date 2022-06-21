import csv
import datetime

#CONSTANTS
FILENAME = "Inventory_Tracking.csv"
TODAY = datetime.date.today()
DATE = str(TODAY.month) + "/" + str(TODAY.day) + "/" + str(TODAY.year)

#FUNCTIONS
def list_options():
    """Get the user input and call the corresponding function"""
    print("\n" + "Inventory Tracking - Main Menu" + "\n")
    print("1 - View today's inventory")
    print("2 - Update inventory")
    print("3 - Add new product to inventory")
    print("4 - Remove product from inventory")
    print("5 - Quit")
    user_input = int(input("Please select an option:"))
    if user_input == 1:
        view_inventory()
    elif user_input == 2:
        update_inventory()
    elif user_input == 3:
        add_product()
    elif user_input == 4:
        remove_product()
    elif user_input == 5:
        quit_app()
    else:
        print("Not a valid option, please try again")
        list_options()

def view_inventory():
    """Print the current inventory for today"""
    print("\n" + "Inventory Tracking - View Inventory" + "\n")
    print("Inventory for " + DATE + ":")
    print("\n" + "Master List of Products:" + "\n")
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                print(row['Product'])
                print("Quantity: " + row['Quantity'])
                print("\n")
    print("\n" + "Warehouse List:" + "\n")
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                print(row['Product'])
                print("Quantity: " + row['Quantity'])
                print("\n")
    print("\n" + "Location 1 Inventory:" + "\n")
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                print(row['Product'])
                print("Quantity: " + row['Quantity'])
                print("\n")
    print("\n" + "Location 2 Inventory:" + "\n")
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                print(row['Product'])
                print("Quantity: " + row['Quantity'])
                print("\n")
    list_options()

def update_inventory():
    """Update the inventory for a specified location"""
    print("\n" + "Inventory Tracking - Update Inventory" + "\n")
    print("Where would you like to update inventory?")
    print("1 - Master List")
    print("2 - Warehouse")
    print("3 - Location 1")
    print("4 - Location 2")
    print("5 - Return to main menu")
    user_input = int(input("Please select an option:"))
    if user_input == 1:
        update_master_list()
    elif user_input == 2:
        update_warehouse()
    elif user_input == 3:
        update_location1()
    elif user_input == 4:
        update_location2()
    elif user_input == 5:
        list_options()
    else:
        print("Not a valid option, please try again")
        update_inventory()

def update_master_list():
    """Update the master list"""
    print("\n" + "Inventory Tracking - Update Master List" + "\n")
    product_list = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                product_list.append(row['Product'])
    print("Please select a product to update:")
    for product in product_list:
        print(product)
    product = input("Please enter a product:")
    if product not in product_list:
        print("Not a valid product, please try again")
        update_master_list()
    print("How many would you like to add?")
    add_quantity = int(input("Please enter a number:"))
    remove_quantity = int(input("How many would you like to remove?"))
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open(FILENAME, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Product', 'Quantity'])
        writer.writeheader()
        for row in rows:
            if row['Date'] == DATE and row['Product'] == product:
                new_quantity = int(row['Quantity']) + add_quantity - remove_quantity
                row['Quantity'] = str(new_quantity)
            writer.writerow(row)
    print("Inventory updated")
    update_inventory()

def update_warehouse():
    """Update the warehouse inventory"""
    print("\n" + "Inventory Tracking - Update Warehouse" + "\n")
    product_list = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                product_list.append(row['Product'])
    print("Please select a product to update:")
    for product in product_list:
        print(product)
    product = input("Please enter a product:")
    if product not in product_list:
        print("Not a valid product, please try again")
        update_warehouse()
    print("How many would you like to add?")
    add_quantity = int(input("Please enter a number:"))
    remove_quantity = int(input("How many would you like to remove?"))
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open(FILENAME, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Product', 'Quantity'])
        writer.writeheader()
        for row in rows:
            if row['Date'] == DATE and row['Product'] == product:
                new_quantity = int(row['Quantity']) + add_quantity - remove_quantity
                row['Quantity'] = str(new_quantity)
            writer.writerow(row)
    print("Inventory updated")
    update_inventory()

def update_location1():
    """Update the Location 1 inventory"""
    print("\n" + "Inventory Tracking - Update Location 1" + "\n")
    product_list = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                product_list.append(row['Product'])
    print("Please select a product to update:")
    for product in product_list:
        print(product)
    product = input("Please enter a product:")
    if product not in product_list:
        print("Not a valid product, please try again")
        update_location1()
    print("How many would you like to add?")
    add_quantity = int(input("Please enter a number:"))
    remove_quantity = int(input("How many would you like to remove?"))
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open(FILENAME, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Product', 'Quantity'])
        writer.writeheader()
        for row in rows:
            if row['Date'] == DATE and row['Product'] == product:
                new_quantity = int(row['Quantity']) + add_quantity - remove_quantity
                row['Quantity'] = str(new_quantity)
            writer.writerow(row)
    print("Inventory updated")
    update_inventory()

def update_location2():
    """Update the Location 2 inventory"""
    print("\n" + "Inventory Tracking - Update Location 2" + "\n")
    product_list = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                product_list.append(row['Product'])
    print("Please select a product to update:")
    for product in product_list:
        print(product)
    product = input("Please enter a product:")
    if product not in product_list:
        print("Not a valid product, please try again")
        update_location2()
    print("How many would you like to add?")
    add_quantity = int(input("Please enter a number:"))
    remove_quantity = int(input("How many would you like to remove?"))
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open(FILENAME, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Product', 'Quantity'])
        writer.writeheader()
        for row in rows:
            if row['Date'] == DATE and row['Product'] == product:
                new_quantity = int(row['Quantity']) + add_quantity - remove_quantity
                row['Quantity'] = str(new_quantity)
            writer.writerow(row)
    print("Inventory updated")
    update_inventory()

def add_product():
    """Add a new product"""
    print("\n" + "Inventory Tracking - Add New Product" + "\n")
    print("Please enter the product you would like to add:")
    product = input("Product:")
    print("Please enter the quantity of the product you would like to add:")
    quantity = int(input("Quantity:"))
    with open(FILENAME, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Product', 'Quantity'])
        writer.writerow({'Date': DATE, 'Product': product, 'Quantity': quantity})
    print("Product " + product + " added to inventory")
    list_options()

def remove_product():
    """Remove a product from inventory"""
    print("\n" + "Inventory Tracking - Remove Product" + "\n")
    product_list = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == DATE:
                product_list.append(row['Product'])
    print("Please select a product to remove:")
    for product in product_list:
        print(product)
    product = input("Please enter a product:")
    if product not in product_list:
        print("Not a valid product, please try again")
        remove_product()
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open(FILENAME, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Product', 'Quantity'])
        writer.writeheader()
        for row in rows:
            if row['Date'] == DATE and row['Product'] != product:
                writer.writerow(row)
    print("Product " + product + " removed from inventory")
    list_options()

def quit_app():
    """Exit the program"""
    print("\n" + "Inventory Tracking - Quit" + "\n")
    print("Are you sure you want to quit? All unsaved changes will be lost.")
    print("1 - Yes")
    print("2 - No")
    user_input = int(input("Please select an option:"))
    if user_input == 1:
        exit()
    elif user_input == 2:
        list_options()
    else:
        print("Not a valid option, please try again")
        quit_app()

#PROGRAM START
list_options()
