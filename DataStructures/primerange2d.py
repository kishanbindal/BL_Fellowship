import math


def isPrime(number):
    if number > 1:
        for i in range(2, math.floor(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


def check_prime_range():
    li1 = []
    lower = 0
    upper = 100
    while True:
        li = []
        for num in range(lower, upper + 1):
            x = isPrime(num)
            if x is True:
                li.append(num)
            if num >= upper - 1:
                break
        li1.append(li)
        lower, upper = upper, upper + 100
        if upper >= 1001:
            break
    return li1
