def main():
    print("1. Adding of Numbers")
    print("2. Subtracting of Numbers")
    print("3. Multiplication of Numbers")
    print("4. Division of Numbers")
        
operators = input("Enter an operator: ")

num1 = float(input("Enter the second number: "))
num2 = float(input("Enter the second number: "))


if operators == '+':
    result = num1 + num2
    print(round(result, 3))
elif operators == "-":
    result = num1 - num2
    print(round(result, 3))
elif operators == '*':
    result = num1 * num2
    print(round(result, 3))
elif operators == '/':
    result = num1 / num2
    print(round(result, 3))

if __name__ == '__main__':
    main()