from functools import reduce

def sum(numbers):
    return reduce(lambda a, b: a+b, numbers)


def calc(numbers):
    result = sum(numbers)
    print(f"{numbers} => {result}")

if __name__ == '__main__':
    calc([0])
