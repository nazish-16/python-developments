import random

def spin_row():
    symbols = ['🍒','🍐', '🍉', '⭐', '🔔']
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print(" | ".join(row))
def get_payout(row, bet): 
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 5
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '⭐':
            return bet * 8
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🍐':
            return bet * 7
    return 0
def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0:
        print("That's not possible")
        return 0
    else: 
        return amount
def main():
    balance = 0
    print("----------------------")
    print("Welcome to py-gamble")
    print("Symbols: 🍒 🍐 🍉 ⭐ 🔔")
    print("----------------------")

    balance += deposit()
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insuffecient funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0") 
            continue
    
        balance -= bet
        row = spin_row()
        print("Spinning...")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost")

        balance += payout

        play_again = input("Do you want to play again? (Y/N): ").upper()

        if play_again != 'Y':
            break
    
    print(f"Game over! Yoru final balance is ${balance}")

if __name__ == '__main__':
    main()