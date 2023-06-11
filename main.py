import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0")
        else:
            print("Amount must be a number")


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Amount must be a number")

    return lines


def get_bet():
    while True:
        bet = input("Enter the amount to bet: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a valid bet between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Bet must be a number")

    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough money to make that bet, your current balance is ${balance}")
        else:
            break

    print(f" You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")


main()
