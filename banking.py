def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0:
        print("That's not possible")
        return 0
    else: 
        return amount
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawed: "))
    if amount > balance:
        print("Insuffecient amount")
        return 0
    if amount < 0:
        print("That's not possible")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("banking program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice between 1-4: ")

        if choice == '1':
            show_balance(balance) 
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That's not a valid choice")

    print("Have a nice day!")

if __name__ == '__main__':
    main()