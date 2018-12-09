import math

def time(n):
    """ Return the number of steps
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    steps = 2 * math.ceil(float(n)/5) + 2
    return steps

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y

x = 5
countdown(x)
print "time = " + str(time(x))
