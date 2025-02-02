import getpass

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    supplied_pin = getpass.getpass("Enter your PIN: ")
    attempts += 1

    if supplied_pin == "123":
            print('PIN correct')
            break
    else:
        attempts_left=max_attempts - attempts
        if attempts_left > 0:
            print('incorrect PIN, please try again')
else:
    print("Failure to access. You have used all three attempts")

