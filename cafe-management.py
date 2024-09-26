dict={
    "pizza": 20,
    "burger": 30,
    "pasta": 10,
    "tenders": 20,
    "chocolate": 30,
    "milk": 20,
    "dark chocolate": 30,
}

cart = []
total = 0 

for key, value in dict.items():
    print(f"{key:10}: ${value:.2f}") 
while True:
    food = input('select an item or (q to quit): ').lower()
    if food == 'q':
        break
    elif dict.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total + dict.get(food)
    print(food, end=" ")

print()
print(f"Total is ${total:.2f}")