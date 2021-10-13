from functools import reduce

def sum(numbers):
    return reduce(lambda a, b: a+b, numbers)
