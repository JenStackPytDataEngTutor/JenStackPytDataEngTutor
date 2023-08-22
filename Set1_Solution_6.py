# Question 6
# A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.
# Complicated? Not at all. Look: 8 isn’t a prime number, as you can divide it by 2 and 4
# (we can’t use divisors equal to 1 and 8 as the definition prohibits this).
# On the other hand, 7 is a prime number, as we can’t find any legal divisors for it.
# Write a function checking whether a number is prime or not.
# The function:
# •is called IsPrime;
# •takes one argument (the value to check)
# •returns True if the argument is a prime number, and False otherwise.
# Hint: try to divide the argument by all subsequent values (starting from 2) and check the remainder
# – if it’s zero, your number cannot be a prime; think carefully about when you should stop the process.
# If you need to know the square root of any value, you can utilize the ** operator.
# Remember: the square root of x is the same as x ** 0.5 ( x raised to the power of 1.5).
# Solution:


def IsPrime(num):
    """function to identify prime numbers"""
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0 and num != i:
                print(num, "is not a prime number") #debug
                return False
        else:
            print(num, "is a prime number") #debug
            return True


for i in range(1,20):
    if IsPrime(i + 1):
        print(i + 1, end="is prime,")
print()
