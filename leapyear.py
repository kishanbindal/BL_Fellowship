def isLeapYear(year):
    if year < 1582:
        raise ValueError("Input Value cannot be less than 1582")
    else:
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            return True
    return False

year = int(input("Enter a year"))
print(isLeapYear(year))