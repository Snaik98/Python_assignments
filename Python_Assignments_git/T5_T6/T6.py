 

# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
'''
string = "Hello World"
result = [char for char in string if char.isupper()]

print("Uppercase letters in the given string are: ",result)

'''

# 2. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students 
#     with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
#     HINT - Use Zip function also
#     Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
#     Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}
'''

students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']

result_dict = dict(zip(students, subjects))
print(result_dict)

'''

# 3. Learn More about Yield, next and Generators
### Done

# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
'''

string = 'Consultadd Training'

length = len(string)
rev_string =[]
for i in range(length-1, -1, -1):
    rev_string.append(string[i])

result=''.join(rev_string)
print(result)

'''

# 5. Write an example on decorators.
# Using function as an argument to another function
'''

def upper(string):
    return string.upper()

def lower(string):
    return string.lower()

def line(funct):
    line1 = funct("Hello, How are You?")
    print(line1)

line(upper)
line(lower)

'''
