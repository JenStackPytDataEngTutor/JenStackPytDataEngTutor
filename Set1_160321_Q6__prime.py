"""Exercise 6 Set 1
 Write a function checking whether a number is prime or not.
"""


def IsPrime(number):
    if number > 1:
        for a in range(2, number):
            #print("\n divisor tried:", a, "number:", number)

            if (number % a) == 0 and number != a:
                #print(f"\n{number} is not a prime number")
                return False
        else:
            #print("\nPrime Identified :", number)
            return True
    else:
        # only executes when number is <=1 ... 1
        return False


for i in range(20):
    if IsPrime(i + 1):
        print("Final Print", i + 1, end=" ")
