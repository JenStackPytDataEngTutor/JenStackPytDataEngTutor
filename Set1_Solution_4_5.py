# Question 4
# Write and test a function which takes two arguments (a year and a month)
# and returns the number of days for the given month/year pair
# (yes, we know that only February is sensitive to the year value, but we want our function to be universal).
# The initial part of the function is ready. Now, convince the function to return None if its arguments don’t make sense.
# Of course, you can (to be honest: you should!) use the previously written and tested function.
# It may be very helpful (we cannot say anything more, sorry).
# We encourage you to use a list filled with the months’ lengths.
# You can create it inside the function – this trick will significantly shorten the code.
# We’ve prepared a testing code. Expand it to include more test cases

# Question 5
# Write and test a function which takes three arguments (a year, a month, and a day of the month)
# and returns the corresponding day of the year, or returns None if any of the arguments is invalid.
# Use the previously written and tested functions. Add some test cases to the code. Our test is only a beginning.

# #Solution 4 and 5:


def IsYearLeap(year):
    """Function to check if a given year is a leap year"""
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print("I'm a leap year")
        return True
    else:
        return False

def DaysInMonth(year,month):
    """Function to check how many days are in a given month in a given year"""
    daysinallmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and IsYearLeap(year):
        return 29 # return 29 days for the month of feb in a leap year
    else:
        return daysinallmonths[month-1] # return days for the month from the list

def DayOfYear(year,month,day):
    """Function to count the number of days elapsed in the year to date"""
    totaldays = day
    if month != 1: # if not January, add the number of days in the preceding months to day to calculate DayOfYear
        for i in range(1, month): # loop to read the
            totaldays += DaysInMonth(year, i)
            print(year, i, totaldays)
        return totaldays

print("Number of days:",DayOfYear(2000,3,4))
print("Number of days:",DayOfYear(2001,3,4))
print("Number of days:",DayOfYear(2001,2,5))
print("Number of days:",DayOfYear(2016,8,5))
print("Number of days:",DayOfYear(2000,12,31))
print("Number of days:",DayOfYear(2001,12,31))




