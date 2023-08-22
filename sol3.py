def IsYearLeap(year):
    #
# put your code here
#
testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]
for i in range(len(testdata)):
    yr = testdata[i]
print(yr,"->",end="")
result = IsYearLeap(yr)
if result == testresults[i]:
    print("OK")
else:
    print("Failed") 