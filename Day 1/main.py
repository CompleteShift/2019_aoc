import math

data = open('input', 'r').readlines()


def fuel(x):
    if x <= 0:
        return 0
    iFuel = int(math.floor(x / 3.0) - 2)
    return max(iFuel + fuel(iFuel), 0)

total = 0

for line in data:
    total += fuel(int(line))
    print fuel(int(line))

print "Total: {}".format(total)
