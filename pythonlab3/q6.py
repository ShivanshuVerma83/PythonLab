# import math
#
# x, y = 0, 0
#
# while True:
#     step = input("enter movements up,down,left,right and step number: ")
#     if step == "":
#         break
#     else:
#         step = step.split(" ")
#         if step[0] == "up":
#             y = y + int(step[1])
#         elif step[0] == "down":
#             y = y - int(step[1])
#         elif step[0] == "left":
#             x = x - int(step[1])
#         elif step[0] == "right":
#             x = x + int(step[1])
#
# distance = int(math.sqrt(x**2+y**2))
#
# print("ans:", distance)
import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)
