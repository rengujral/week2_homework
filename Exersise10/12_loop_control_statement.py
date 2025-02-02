# run as is then change j to 12
# use the debugger to show the i counter increasing
i = 45
j = 12
# i and j are two separate variables
# while i is less than 42, multiply the value by 2/if it becomes more than the value of j break (end)
while i < 42:
    i = i * 2
    if i > j:
        break
# make comments about break - who is the friend - break and while are friends - exits loop early if the conditions listed are met
# if i is more than 42 - the loop expires
else:
    print("Loop expired: ", i)
# separate message not depending on a variable - gives the final value
print("Final value: ", i)
