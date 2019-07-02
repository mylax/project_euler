def thirtyone(year):
    return 31

def thirty(year):
    return 30

def feb(year):
    if year % 400:
        return 29
    if year % 100:
        return 28
    if year % 4:
        return 29
    return 28


get_days_month = {
    1:thirtyone,
    2:feb,
    3:thirtyone,
    4:thirty,
    5:thirtyone,
    6:thirty,
    7:thirtyone,
    8:thirtyone,
    9:thirty,
    10:thirtyone,
    11:thirty,
    12:thirtyone
}


LIMIT = 36964

RESULT = [[1, 1, 1900, 1]]
i = 0
while(i < LIMIT):
    day = RESULT[-1][0]
    month = RESULT[-1][1]
    year = RESULT[-1][2]
    weekday = RESULT[-1][3]
    max_days_month = get_days_month[month](year)
    if day == max_days_month:
        if month == 12:
            year += 1
            day = 1
            month = 1
        else:
            month += 1
            day = 1
    else:
        day += 1
    if weekday == 7:
        weekday = 1
    else:
        weekday += 1
    RESULT.append([day, month, year, weekday])
    i += 1

len([x for x in RESULT if (x[3] == 7 and x[0] == 1 and x[2] > 1900)])