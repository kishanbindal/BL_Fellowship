import calendar


def cal():
    mm = int(input("Please enter month 1-12 : \n"))
    yy = int(input("Please enter year : \n"))
    if mm > 12 or mm < 1:
        raise ValueError("Please enter value of month between 1-12 only.")
    c = calendar.TextCalendar(calendar.SUNDAY)  # Creating a text calendar and setting the first day to print Sunday
    st = c.formatmonth(2020, 1)  # inputting the year,month in order to create the calendar
    print(st)  # printing the calendat
    return calendar.monthcalendar(yy, mm)  # Returning the 2-D array [week[Dates]]
