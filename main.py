
def dateIsBefore (year1, month1, day1, year2, month2, day2):
    '''This function dateIsBefore checks if year1-month1-day1
       is before year2-month2-day2 and returns True if date1 is
       before date2. Otherwise returns False'''
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False
print dateIsBefore(1995,4,3,1999,4,1) #test for dateIsBefore() function