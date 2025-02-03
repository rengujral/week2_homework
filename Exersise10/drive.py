# input function returns output value entered by user in accordance with traffic_light variable
traffic_light = input("Enter the traffic light color (red, yellow, green): ")

# == double equals associates the colour with the designated print statement (red = stop and wait...)
# if statement is used for conditional execution - if initial condition is not true, the program will check the other conditions (elif, else)
if traffic_light == 'red':
        print('stop and wait for lights to change')
elif traffic_light == 'yellow':
        print('slow down and wait')
else:
        print('light is green, you can go!')

# Dictionaries - key:object pairs
# keys are IMMUTABLE and have to be text strings
# light = ['red', 'yellow', 'green']
# instruct = ['stop and wait for lights to change', 'slow down and wait', 'light is green, you can go!']
# zip () - combining two iterables (both lists in this case)
# driver_manual = dict(zip(light, instruct))
# print(driver_manual)
