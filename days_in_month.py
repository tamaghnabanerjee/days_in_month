days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]

year=int(input("Enter the year: "))
month=int(input("Enter the month: "))

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

def days_in_month(year,month):
    if leap_year(year) and month==2:
        return 29
    else:
        return days_in_months[month-1]

print(days_in_month(year,month))
