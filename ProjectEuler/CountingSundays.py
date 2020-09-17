year = 1900
weekday = 0
month = 1
dayCount = 0

sundays = 0

while year != 2001:
    weekday += 1
    dayCount += 1
    if month == 4 or month == 6 or month == 9 or month == 11:
        if dayCount == 31:
            month += 1
            dayCount = 1
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if dayCount == 30:
                month += 1
                dayCount = 1
        else:
            if dayCount == 29:
                month += 1
                dayCount = 1
    else:
        if dayCount == 32:
            month += 1
            dayCount = 1
    if month == 13:
        year += 1
        month = 1
        dayCount = 1
    weekday %= 7
    if weekday == 0 and dayCount == 1:
        if year >= 1901:
            sundays += 1

    #print("{}, {}, {} | {}".format(month, dayCount, year, weekday))

print(sundays)
