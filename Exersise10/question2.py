import getpass
# this module prompts user for a password without echoing

# created two variables - one representing the maximum attempts allowed and one the counts up by 1 as the loop continues
max_attempts = 3
attempts = 0

# while the condition - the attempts made by the user has not met the maximum attempts set (3) - the loop continues and the attempts made by the user goes up by one
while attempts < max_attempts:
# getpass.getpass() returns a hidden value to the variable supplied_pin
    supplied_pin = getpass.getpass("Enter your PIN: ")
    attempts = attempts + 1
# assigning a new value to the variable 'attempts' - adding integer (1) to the attempts variable as the loop continues

# == (double equals)
    if supplied_pin == "123":
            print('PIN correct.')
            break
# break line stops the loop early when the condition is met (supplied pin equals 123)

# Concatenation of variables
    else:
        attempts_left=max_attempts - attempts
        if attempts_left > 0:
            # f-string (formatted string literal) - embeds variables in a string - more readable that using .format()
            print(f'incorrect PIN, please try again.You have {attempts_left} left.')

else:
    print("Failure to access. You have used all three attempts")
# Final message after three incorrect attempts
