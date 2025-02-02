traffic_light = input("Enter the traffic light color (red, yellow, green): ")

if traffic_light == 'red':
        print('stop and wait for lights to change')
elif traffic_light == 'yellow':
        print('slow down and wait')
else:
        print('light is green, you can go!')

# traffic_lights = ['red', 'yellow', 'green']
# for light in traffic_lights:
#     if light == 'red':
#         print('stop and wait for lights to change')
#     elif light == 'yellow':
#         print('slow down and wait')
#     else:
#         print('light is green, you can go!')
#
# light = ['red', 'yellow', 'green']
# instruct = ['stop and wait for lights to change', 'slow down and wait', 'light is green, you can go!']
# manual = dict(zip(light, instruct))
# print(manual)
