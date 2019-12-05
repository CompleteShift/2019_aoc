import sys


def func_choose(x):
    print "Opcode {}".format(data[x])
    if data[x] == 1: # addition
        func_add(x)
        return True
    elif data[x] == 2: # multiplication
        func_multiply(x)
        return True
    elif data[x] == 99: # done
        print data[0]
        print "I should stop"
        return False
    else:
        print "Something went wrong"
        return False


def func_add(x):
    print "Adding index {} ({}) and index {} ({}) and storing into index {} ({})".format(x+1, data[x+1], x+2, data[x+2], x+3, data[data[x+1]] + data[data[x+2]])
    data[data[x+3]] = data[data[x+1]] + data[data[x+2]]


def func_multiply(x):
    print "Multiplying {} ({}) and index {} ({}) and storing into {} ({})".format(x+1, data[x+1], x+2, data[x+2], x+3, data[data[x + 1]] * data[data[x + 2]])
    data[data[x + 3]] = data[data[x + 1]] * data[data[x + 2]]


data = open('input', 'r').read().split(',')
should_I_continue = True

index = 0
while index < len(data):
    data[index] = int(data[index])
    index += 1

data[1] = 22
data[2] = 54

index = 0
while should_I_continue:
    print "Index is {}".format(index)
    should_I_continue = func_choose(index)
    index += 4

print data[0]
