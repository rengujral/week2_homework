# run as is then change j to 12
# use the debugger to show the i counter increasing
from typing import final

i = 2
j = 12
# i and j are two separate variables
# while i is less than 42, multiply the value by 2/if it becomes more than the value of j break (end)

# To debug, start at the beginning of the loop (while) and step into code, can see the changing values as the loop continues
while i < 42:
    i = i * 2
    if i > j:
        break
# break statement (instruction) and while are friends - exits loop early if the conditions listed are met
# continue also works closely with break - skips iteration but keeps looping
# break is the exit out of the loop (can only be used within loop) and stops loop when a certain condition is met
# if i is more than 42 - the loop expires

else:
    print("Loop expired: ", i)
# separate message not depending on a variable - gives the final value
print("Final value: ", i)

# continue
# skips the next iteration (only affects current iteration of the loop) whereas break terminates the ENTIRE loop
# can only be used inside a loop - any code after will be ignored


