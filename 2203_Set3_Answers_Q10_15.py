"""Question 10:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,i-Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:
Note: In case of input data being supplied to the question,
it should be assumed to be a console input in a comma-separated form.

Solution:
input_str = input("Enter data:")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
#
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col

multilist = [[row*col for col in range(colNum)] for row in range(rowNum)]

print(multilist)
######################################
Question 11:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))
###############################
Question 12
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:"""
# number_of_lines = int(input("enter number of lines you want to capitalise:"))
# array_of_lines = [(input("Enter String :\n").upper()) for i in range(number_of_lines)]
#
# #
# print("these are the capital lines", array_of_lines)
# for sentence in array_of_lines:
#     print(sentence)

# lines = []
# while True:
#     sentence_entered = input("Please enter a sentence")
#     if sentence_entered:
#         lines.append(sentence_entered)
#     else:
#         break
#
# upper_list = [s.upper() for s in lines]         # list com
#
# for sentence in upper_list:
#     print(sentence)

#print(','.join(input('Enter a sequence of words').upper().split(',')))

#######################################
# """Question 13
# Write a program that accepts a sequence of whitespace separated words as input and prints the words
# after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.
#Solly
# slist = []
# print(' '.join([slist.append(word) or word for word in sorted(input('Enter whitespace separated words: ').split(' ')) if word not in slist]))
#
# # Provided Solution:
# s = input("Enter a sentence")
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))
# # #----------------------------------------#
# ############################################
#
# Question 14
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Solution:
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
#         values.append(s)
# print(",".join(values))
#
# # sollys
# def even_num(number):
#     num = str(number)      # num looks like: "2000"
#     for digit in num:              # iterate over 'num' the string of digits
#         if int(digit) % 2 != 0:        # if digit is odd then
#             return False                      # exit from Function with False return value -> all digits are not even!!
#         else:                          # else digit is even
#             continue                          # get next digit
#     return True                   # exit from Function with True return value -> all digits are even!!
#
#
# for all_even in range(1000, 3001): # loop over defined range of numbers
#     output = even_num(all_even)       # test if all digits of current number are even
#     if output:                        # if even (i.e output == True )
#         print(all_even, end=',')             # print all the digits of the even number
#     else:                             # else - its odd,
#         continue                             # nothing to print so get next number to test
# print()
# #----------------------------------------#


# ###########################################
# Question 15:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# faisal
# sent = input('Type in ')
# sent = list(sent)
#
# lett = 0
# digi = 0
# for i in sent:
#     if i.isalpha():
#         lett += 1
#     if i.isdigit():
#         digi += 1
# print('letters in sentence: ', lett)
# print('Digits in sentence ', digi)
### linda
import string
string.whitespace

phrase = "The cat in the\t hat is happy in 2021\n"
#phrase = list(phrase)
#print(phrase)

l, d, sp, wsp = 0, 0, 0, 0
for i in phrase:
    if i.isalpha():
        l = l + 1
    if i.isdigit():
        d = d + 1
    if i.isspace() and i.isprintable():
        sp = sp + 1
    elif i in string.whitespace:
        wsp += 1

print("Letters:", l)
print("Digits:", d)
print("Spaces:", sp)
print("WSpaces:", wsp)



###
# import string
# sentence = input('Enter a sentence:')
# letter_count = 0
# num_count = 0
# for each_letter in sentence:
#     if each_letter in string.ascii_letters:
#         letter_count += 1
#         continue
#     elif each_letter in string.digits:
#         num_count += 1
#         continue
#     else:
#         continue
# print('LETTERS', letter_count)
# print('DIGITS', num_count)
# # Solution:
input_string = input("Please enter a sentence with letters and numbers")
dict_count = {"DIGITS": 0, "LETTERS": 0, "SPACES": 0}

for char in input_string:
    if char.isdigit():
        dict_count["DIGITS"] += 1
    elif char.isalpha():
        dict_count["LETTERS"] += 1
    elif char.isspace() and char.isprintable():
        dict_count["SPACES"] += 1
    else:
        pass

print("LETTERS", dict_count["LETTERS"])
print("DIGITS", dict_count["DIGITS"])
print("SPACES", dict_count["SPACES"])
#----------------------------------------#
# #
# # """
