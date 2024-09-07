unit = input("Is this temperature in (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in F is {temp}°F")
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in C is {temp}°C")
else:
    print(f"{unit} is invalid.")