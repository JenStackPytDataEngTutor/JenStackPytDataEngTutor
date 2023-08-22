import math

def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for remainder
    sr for square root
    ! for factorial
    ''')

    number_1 = int(input('Enter your first number: '))
    #some operators only require 1 operand
    if operation not in ['sr', '!']:
        number_2 = int(input('Enter your second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '**':
        print('{} to the power of {} = '.format(number_1, number_2))
        print(math.pow(number_1, number_2))

    elif operation == '%':
        print('{} Modulo {} = '.format(number_1, number_2))
        print(number_1 % number_2)

    elif operation == 'sr':
        print('Square Root of {} = '.format(number_1))
        print(math.sqrt(number_1))

    elif operation == '!':
        print('Factorial {} = '.format(number_1))
        print(math.factorial(number_1))

    else:
        print('You have not typed a valid operator, please run the program again.')
    again()

# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
        calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

# Call calculate() outside of the function

calculate()
