# Two eggs dropped from building find the breaking floor O(sqrt(n))
import math

floors = list(range(10))
breaks = 3
jump = int(math.sqrt(len(floors)))


for i in range(1, len(floors)):
    if len(floors) < breaks:
        print('Nope')
        break
    i = i * jump
    if i < breaks:
        continue
    else:
        for x in range(i - jump, i + 1):
            if x == breaks:
                print(x)
                break
        break



