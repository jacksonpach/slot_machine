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


