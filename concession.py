menu = {
    "pizza": 4.00,
    "nachos": 3.50,
    "popcorn": 2.50,
    "fries": 6.40,
    "chips": 2.30,
    "pretzel": 4.75,
    "coke": 2.15,
    "pasta": 7.60
}
cart = []
total = 0 

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}") 
print("------------------------")

while True:
    food = input('select an item or (q to quit): ').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()
print(f"Total is ${total:.2f}")