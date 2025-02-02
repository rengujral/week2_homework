# getpass is a module that allows you get username and passwords
import getpass

# the pin function is used to add the credit card's pin
pin = '1234'

# the input function allows us to create a way for the pin to be entered
# supplied_pin = input("Enter your pin: ")

# the 'while' function is used to create the loop to allow the input of the credit card pin
# the second input statement displays an error message if the inputted pin is wrong
# while supplied_pin != pin:
#     supplied_pin = input("That is the incorrect pin, please try again: ")

for attempts in range(3):
    # getpass.getpass allows us to mask the password input
    supplied_pin = getpass.getpass('Enter your pin: ')
    if supplied_pin == pin:
        print("PIN accepted!")
        break
    else:
        print('Incorrect PIN, please try again')
else:
    print("End of attempts, Goodbye.")