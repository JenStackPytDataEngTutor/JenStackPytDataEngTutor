"""
take input from user ( integer)
generate list of numbers from 0 to (i)input number
- these will be the dictionary keys
- corresponding dictionary value is i*i
put into dictionary

"""
#
# Dictionary content should be
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
num_dict = {}
input_i = input("Please enter an integer")
int_i = int(input_i)

# int_i is the key, val is the calculated value
for key in range(1, int_i + 1):
    val = key * key
    num_dict[key] = val

print(num_dict)

#########################
number = int(input('Enter a number:'))
squares_dict = {}
for i in range(1, number + 1):
    squares_dict[i] = i*i
print(squares_dict)
############################################

num = int(input("please enter a number:\n"))

number_dict_comp = {num: num*num for num in range(1, num + 1)}

print(number_dict_comp)
