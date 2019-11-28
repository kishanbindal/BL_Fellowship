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
    def dayOfWeek(date,month,year):
        pass



