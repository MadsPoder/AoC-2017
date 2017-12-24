import math

pInput = 361527

#Part 1
#Get amount of "spirals"
step = 0
counter = 0
val = 1
while val < pInput:
    if counter%2 == 0:
        step += 1
    val += step
    counter += 1

#values in "spiral"
data = range(val-step, val)

#offset from origin
offset = math.floor(len(data)/2.)

#find index and calculate manhattan distance
for k in range(len(data)):
    if data[k] == pInput:
        print("distance {}".format(math.fabs(k-offset+(math.ceil(step/2.)))))

#Part 2
#...