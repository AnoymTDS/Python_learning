


# item2 = {
#     "quantity": 20,
#     "p_price": 140,
#     "s_price": 300
# }

# dict = {x: item2[x] for x in item2 if item2[x] < 200}
# print(dict)



# item4 = {
#     "name": "motherboard",
#     "quantity": 10,
#     "p_price": 120,
#     "s_price": 200 
# }

# reverse_dict = {x: item4 for item4, x in item4.items()}
# print(reverse_dict)



#Canteen
print("Welcome To Tobi's Canteen: ")
canteen_menu = {
    "food": { 
        "jollof": 500,
        "salad": 650,
        "pasta": 960,
        "gizzed dodo":1000
    },
    "protein": {
        "chicken": 1000,
        "beef": 1200,
        "fish": 1500,
        "sea food": 2500,
        "pork": 1100
    },
    "drinks": {
        "water": 150,
        "soda": 200,
        "juice": 500,
        "coffee": 170,
        "tea": 200
    }
}
orders = {}

print("Here is our menu:")
print("Food Menu:")
for item, price in canteen_menu['food'].items():
    print(f"{item.capitalize()}: N{price}")
print("\nProtein Menu:")
for item, price in canteen_menu['protein'].items():
    print(f"{item.capitalize()}: N{price}")
print("\nDrinks Menu:")
for item, price in canteen_menu['drinks'].items():
    print(f"{item.capitalize()}: N{price}")

num_customers = int(input("\nHow many customers are ordering? "))

for _ in range(num_customers):
    customer_name = input("May I know your name? ")
    cus_order = {}
    
    while True:
        food_choice = input("What food would you like to order? (jollof/salad/pasta/gizzed dodo): ").lower()
        if food_choice in canteen_menu['food']:
            cus_order['food'] = food_choice
            break
        else:
            print("Invalid choice! Please choose from the available options.")
    
    while True:
        protein_choice = input("What protein would you like? (chicken/beef/fish/sea food/pork): ").lower()
        if protein_choice in canteen_menu['protein']:
            cus_order['protein'] = protein_choice
            break
        else:
            print("Invalid choice! Please choose from the available options.")
    
    while True:
        drink_choice = input("What drink would you like? (water/soda/juice/coffee/tea): ").lower()
        if drink_choice in canteen_menu['drinks']:
            cus_order['drinks'] = drink_choice
            break
        else:
            print("Invalid choice! Please choose from the available options.")
    
    orders[customer_name] = orders
print(orders)
print("\nOrder Summary:")
for customer, order in orders.items():
    print(f"\nCustomer: {customer}")
    print("Items Ordered: ")
    total_bill = 0
    for category, item in cus_order.items():
        print(f"{category}: {item} - N{canteen_menu[category][item]}")
        total_bill += canteen_menu[category][item]
    print("Total Bill: N", total_bill)

    