import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "♣": 2,
    "♦": 4,
    "♥": 6,
    "♠": 8,
}

symbol_value = {
    "♣": 5,
    "♦": 4,
    "♥": 3,
    "♠": 2,
}


def check_win(columns, lines, bet, values):
    win = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
            else:
                win += values[symbol] * bet
                win_lines.append(line + 1)
    return win, win_lines


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


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="\n")


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


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough money to make that bet, your current balance is ${balance}")
        else:
            break

    print(f" You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    win, win_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${win}")
    print(f"Winning lines: ", *win_lines)
    return win_lines - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your balance is ${balance}")
        answer = input("Would you like to spin? (y/n) ")
        if answer == "n":
            print(f"Your final balance is ${balance}")
            break

        balance += spin(balance)

    print(f"You left with ${balance}")


main()
