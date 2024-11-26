menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

print("Welcome to Kassan Cafe")

order_list = []

place_order = True
while place_order:
    i = 1
    menu_items = {}
    print("From which menu would you like to order?")
    
    for category_number, category_name in enumerate(menu.keys(), 1):
        print(f"{category_number}: {category_name}")
        menu_items[category_number] = category_name
        
    menu_category = input("Type menu number: ")
    
    if menu_category.isdigit() and int(menu_category) in menu_items:
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")
        i = 1
        item_selection = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        
        for item_name, price in menu[menu_category_name].items():
            if isinstance(price, dict):
                for sub_item_name, price in price.items():
                    combined_name = f"{item_name} - {sub_item_name}"
                    item_selection[i] = {"Item name": combined_name, "Price": price}
                    print(f"{i}      | {combined_name:<24} | ${price:.2f}")
                    i += 1
            else:
                item_selection[i] = {"Item name": item_name, "Price": price}
                print(f"{i}      | {item_name:<24} | ${price:.2f}")
                i += 1
        
        menu_selection = input("Select item number: ")
        
        if menu_selection.isdigit() and int(menu_selection) in item_selection:
            selected_item = item_selection[int(menu_selection)]
            quantity_input = input(f"How many {selected_item['Item name']} would you like? ")
            
            if quantity_input.isdigit():
                quantity = int(quantity_input)
            else:
                print("Invalid quantity. Defaulting to 1.")
                quantity = 1
            
            selected_item["Quantity"] = quantity
            order_list.append(selected_item)
            print(f"Added {quantity} x {selected_item['Item name']} to your order.")
        else:
            print("Invalid selection, please try again.")
    else:
        print("Invalid menu option, please try again.")
    
    while True:
        another_item = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
        if another_item in ['y', 'yes']:
            break
        elif another_item in ['n', 'no']:
            place_order = False
            break
        else:
            print("Please enter 'Y' for yes or 'N' for no.")

print("This is what we are preparing for you:")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for order_item in order_list:
    item_name = order_item["Item name"]
    price = order_item["Price"]
    quantity = order_item["Quantity"]

    spaces = " " * (26 - len(item_name))

    print(f"{item_name}{spaces} | ${price:.2f} | {quantity}")

# Calculate the total order price using list comprehension
total_price = sum(item["Price"] * item["Quantity"] for item in order_list)

# Print the total price
print(f"Total Price: ${total_price:.2f}")