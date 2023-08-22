#----------------------------------------#
# Question 1:
# Write a program which will find all such numbers which are divisible 
# by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a 
# comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method
#


#range(begin, end)
#if
#method join
#list
#for def
#if
#3201
#print()










# Solution:
l = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))

print(','.join(l))
#----------------------------------------#
# Question 2:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Solution:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input())
print(fact(x))
#----------------------------------------#
# Question 3
# Write and test a function which takes one argument (a year)
# and returns True if the year is a leap year, or False otherwise.
# The seed of the function is already sown in the skeleton code (below).

# Note: we’ve also prepared a short testing code, which you can use to test your function.
# The code uses two lists – one with the test data, and the other containing the expected results.
# The code will tell you if any of your results are invalid.
#
# Solution:


def IsYearLeap(year):
    """Function to check if a given year is a leap year"""
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False
#end of function


# The following lists specifies input test data and the corresponding expected results

testdata = [1900, 2000, 2016, 1987, 2020, 2023]
testresults = [False, True, True, False, True, False]

#    The following for loop invokes the IsYearLeap() function on each YEAR provided in testdata[] list
#    the result returned from IsYearLeap() is then compared with the corresponding entry in testresults[]
#    If the value returned from the function matches the corresponding result then the 'OK' message is displayed
#    beside the YEAR tested to indicate this test case has PASSED - (ie our code appears to be correct)
#    otherwise 'Failed' message is displayed beside the YEAR tested to indicate teh test case has FAILED


for i in range(len(testdata)):
    yr = testdata[i]
    print(yr, "->", end="")
    result = IsYearLeap(yr)
    if result == testresults[i]:
        print("Test OK - Actual Results = Expected Results")
    else:
        print("Test Failed - Actual Results Do NOT = Expected Results")

