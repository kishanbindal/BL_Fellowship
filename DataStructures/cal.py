import calendar


def cal():
    mm = int(input("Please enter month 1-12 : \n"))
    yy = int(input("Please enter year : \n"))
    if mm > 12 or mm < 1:
        raise ValueError("Please enter value of month between 1-12 only.")
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2020, 1)
    print(st)
    print(calendar.monthcalendar(yy, mm))
