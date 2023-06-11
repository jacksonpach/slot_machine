MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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
    bet = get_bet()
    total_bet = lines * bet
    print(f" You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")


main()
