from functools import reduce


def fizzbuzz(n):
    r = ""
    
    if n % 3 == 0: 
        r += "fizz"
    if n % 5 == 0: 
        r += "buzz"
    
    return r or str(n)

def loop_fizzbuzz(t: int):
    results = []
    for i in range(1, t + 1):
        results.append(fizzbuzz(i))
    return results

if __name__ == '__main__':
    fizzbuzz()
