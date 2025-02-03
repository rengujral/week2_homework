# this module prompts user for a password without echoing
import getpass

# terminal - python (win)/python3 (MAC) & file name

# created two variables - one representing the maximum attempts allowed and one that counts up by 1 from 0 as the loop continues
max_attempts = 3
attempts = 0

# while the condition - the attempts made by the user has not met the maximum attempts set (3) - the loop continues and the attempts made by the user goes up by one
while attempts < max_attempts:
# getpass.getpass() returns a hidden value to the variable supplied_pin
    supplied_pin = getpass.getpass("Enter your PIN: ")
    attempts = attempts + 1
# assigning a new value to the variable 'attempts' - adding integer (1) to the 'attempts' variable as the loop continues

# == (double equals) - equality operator; 123 is assigned to variable supplied_pin)
    if supplied_pin == "123":
            print('PIN correct.')
            break
# break line stops the loop early when the condition is met (supplied pin equals 123)

# new variable (attempts_left) and creates new condition - if the attempts_left is greater than zero - the loop continues with new print statement (incorrect PIN)
# if statement is used for conditional execution - if initial condition is not true, the program will check the other conditions ( elif, else )
    else:
        attempts_left=max_attempts - attempts
        if attempts_left > 0:
            # f-string (formatted string literal) - embeds variables and expressions in curly braces within a string - makes output more readable (that using .format() for example)
            # can automatically convert non-string types to strings
            print(f'incorrect PIN, please try again.You have {attempts_left} left.')

else:
    print("Failure to access. You have used all three attempts")
# print is a function
# Final message after three incorrect attempts

# another version of the exercise - unable to incorporate the display of 'attempts left' as the block of code loops - prefer the first version

# getpass is a module that allows you get username and passwords
import getpass

# the pin function is used to add the credit card's pin
# one variable - in this case pin is associated with string '1234'
pin = '1234'

# using 'for' conditional statement - repeats block of code a certain number of times
# range outlines the number of times the code loops for - range creates an iterable sequence (1,2,3) - in this case, the number of attempts allowed
for attempts in range(3):
    # getpass.getpass allows us to mask the password input
    supplied_pin = getpass.getpass('Enter your pin: ')
# equality operator - between both variables
    if supplied_pin == pin:
        print("PIN accepted!")
        break
    else:
        print('Incorrect PIN, please try again')
else:
    print("End of attempts, Goodbye.")