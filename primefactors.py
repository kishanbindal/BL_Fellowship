from com.bridgelabz.utility import utility


def primeFactors(n):
    factors_list = []
    divisor = 2
    while n>1:
        while n%divisor == 0:
            factors_list.append(divisor)
            n = n/divisor
        divisor += 1,
    return factors_list
