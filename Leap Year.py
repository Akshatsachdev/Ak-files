def is_leap(year):
    if year % 400 == 0:
        return "Leap year"
    if year % 100 == 0:
        return "Not a leap year"
    if year % 4 == 0:
        return "Not a leap Year"
    else:
        return False
year=int(input("Enter a year to check:"))
print(is_leap(year))        
