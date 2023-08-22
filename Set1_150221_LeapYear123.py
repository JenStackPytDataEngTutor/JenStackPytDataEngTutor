# Question 3

# The seed of the function is already sown in the skeleton code (below).

# Note: we’ve also prepared a short testing code, which you can use to test your function.
# The code uses two lists – one with the test data, and the other containing the expected results.
# The code will tell you if any of your results are invalid.
#
# Solution:


def IsYearLeap(year):
    """Function to check if a given year is a leap year
    -  takes one argument (a year)
    - returns True if the year is a leap year, or False otherwise.
    """
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False
#end of function


def DaysInMonth(year, month):
    """ Function to determine the number of days in a given month
    of a given year"""

    this_month = 0
    if type(year) == str or type(month) == str:
        print("Bad data found")
        return          # returns None

    if month == 2:
        if IsYearLeap(year):
            this_month = 29
        else:
            this_month = 28
    else:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        this_month = days_per_month[month-1]
    return this_month


def DayOfYear(year, month, day):
    total_days = day                    # Add day of current month to total_days
    if month != 1:                      # if it's not January then add the days
        for mo in range(1, month):      # of each preceeding month to the total_days
            total_days += DaysInMonth(year, mo)
    return total_days                   # return teh calculated total number of days

# The following lists specifies input test data and the corresponding expected results
# Input Dataset for Test of function
testyears = [2000, 2000, 2001, 2001, 2016, 2000, 2001]
testmonths = [3, 3, 3, 2, 8, 12, 12]
testdays = [31, 4, 4, 5, 5, 31, 31]
# Expected Results
testresults = [91, 64, 63, 36, 218, 366, 365]

#    The following for loop invokes the IsYearLeap() function on each YEAR provided in testdata[] list
#    the result returned from IsYearLeap() is then compared with the corresponding entry in testresults[]
#    If the value returned from the function matches the corresponding result then the 'OK' message is displayed
#    beside the YEAR tested to indicate this test case has PASSED - (ie our code appears to be correct)
#    otherwise 'Failed' message is displayed beside the YEAR tested to indicate teh test case has FAILED


for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    da = testdays[i]
    print("The year, month and day being tested is: ", yr, mo, da, "->", end="")
    result = DayOfYear(yr, mo, da)

    if result == testresults[i]:
        print("Test OK - Actual Results = Expected Results")
    else:
        print("Test Failed - Actual Results Do NOT = Expected Results")

