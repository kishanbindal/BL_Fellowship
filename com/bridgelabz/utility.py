import math

class utility():

    @staticmethod
    def checkanagram(word1,word2):
        if sorted(word1) == sorted(word2):
            return True
        return False

    @staticmethod
    def isPrime(number):
        if number>1:
            for i in range(2,math.floor(number**0.5)+1):
                if number % i == 0 :
                    return False
            return True

    @staticmethod
    def temperaturConversion(temp,unit):
        '''Enter Temperature and unit.
        Unit Must be either F or C'''
        if unit[0].upper() == 'F':
            c = (temp -32)*(5/9)
            print(f"Temperature in Fahrenheit : {temp}\nTemperature in Celcius {c}")
            return round(c,4)
        elif unit[0].upper() == 'C':
            f = (temp*(9/5))+32
            print(f"Temperature in Celcius : {temp}\nTemperature in Fahrenheit {f}")
            return round(f,4)
        else:
            print("Invalid Input, Please specify Units(Second Attribute) in 'f' or 'c'\n")


    @staticmethod
    def monthlyPayment(P,Y,R):
        '''
        monthlyPayment(principle,duration in years,InterestRate)
        Enter P = Principle,Y = Year, R = interest Percentage'''
        n = 12*Y
        r = R/(12*100)
        payment = (P*r)/(1-(1+r)**(-n))
        print(f"Monthly Payment : {payment}")
        return round(payment,2)

    @staticmethod
    def dayOfWeek(d,m,y):
        '''Input Format (dd/mm/yyyy'''
        y0 = y - ((14-m)/12)
        x = y0 + (y0/4) - (y0/100) + (y0/400)
        m0 = m  + 12*((14-m)/12) - 2
        d0 = (d+x+(31*m0)/12) % 7
        return math.floor(d0)

    @staticmethod
    def toBinary(n):
        s = ''
        while n>1:
            remainder = str(n%2)
            s = s+ remainder
            n = n//2
        if n == 1:
            s = s + str(1)
        if len(s)%2 == 1:
            s = s + str(0)
        return s[::-1]

    @staticmethod
    def swapNibble(num):
        binary = utility.toBinary(num)
        swap_nibble = binary[4:] + binary[:4]
        swap_nibble = list(swap_nibble)
        formula = [2**7,2**6,2**5,2**4,2**3,2**2,2**1,1]
        decimal = 0
        for i in range(0,len(swap_nibble)):
            if swap_nibble[i] == '1':
                decimal = decimal + formula[i]
        return decimal

