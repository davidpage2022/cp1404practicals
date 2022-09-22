"""

Get number of items
For each item
    Get item price
    Add item price to total price
If total price > 100
    Apply discount to total price
Print total price

"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):
    item_price = float(input("Price of item: $"))
    total_price += item_price
if total_price > 100:
    total_price -= total_price * 0.1
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
