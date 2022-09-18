import math


def add2(input1, input2):
    return input1 + input2


def sub(input1, input2):
    return input1 - input2


def div(input1, input2):
    if (input2 == 0):
        return "error"
    return ("{0:.4f}".format(input1 / input2))



def mult(input1, input2):
    return input1 * input2


def power(input1, input2):
    return math.pow(input1, input2)


def sqrt(input1, input2):
    return math.sqrt(input1)