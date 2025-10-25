import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol occurrences define rarity and payout
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
}

def deposit():
    while True:
        amount = input("What amount would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Enter a valid number.")

def get_bet():
    while True:
        amount = input(f"What amount would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Enter a valid number.")

def get_slot_machine_spin(rows, cols, symbols_count):
    all_symbols = []
    for symbol, count in symbols_count.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]  
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=" | " if i != len(columns)-1 else "")
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Not enough balance. Your current balance: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print("\n🎰 Spinning...\n")
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"\nYou won ${winnings}!")

    if winning_lines:
        print("Winning lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    
    while True:
        print(f"\nCurrent balance: ${balance}")
        action = input("Press Enter to play (or 'q' to quit): ")
        if action.lower() == 'q':
            break

        balance += spin(balance)
        if balance <= 0:
            print("You ran out of money! Game Over 💸")
            break

    print(f"\nYou left with: ${balance}")
    print("Thanks for playing! 🎉")


if __name__ == "__main__":
    main()
