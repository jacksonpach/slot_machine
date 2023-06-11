MAX_LINES = 3

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

    return amount


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

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print("Balance: " + str(balance))
    print("Lines: " + str(lines))

main()