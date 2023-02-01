#TASK 1

'''
# 1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.

a, b, c = 1, 2.5, True

print(type(a))
print(type(b))
print(type(c))

'''

'''
# 2. Create a variable of type complex and swap it with another variable of type integer.

a, b = 4, 5
c = complex(a,b)
d = 2

print("Before Swap, complex =",c,", integer=", d)
tmp = c
c = d
d = tmp

print("after swap, integer=",c,", complex=", d)
'''

'''
# 3. Swap two numbers using a third variable and do the same task without using any third variable.

#using 3rd variable
# a = 10
# b = 20

# print("Before swapping =",a,b)
# tmp = a
# a = b
# b = tmp

# print("After swapping =",a,b)

#without using 3rd variable
a = 10
b = 20

print("Before swapping =", a,b)
a = a + b
b = a - b
a = a - b

print("After swapping =", a,b)

'''

'''
# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

a = input()

print(a)

# for python 2.x
# print a

'''

'''
# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and 
# print result as the final output.

a, b = [int(x) for x in input("Enter any 2 numbers from 1-10:").split()]

z = a + b
result = z + 30

print("Result= ", result)

'''

'''
# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc

a = input("enter a value to check data-type:")

def check_type(a):
    try:
        print("Data type of the entered value is : Int ", int(a))
    except ValueError:
        try:
            print("Data type of the entered value is : Float ", float(a))  
        except ValueError:
            a = a.lower()
            if(a == 'true' or a == 'false'):
                print("Data type of the entered value is : bool ", (a))
            else:
                print("Data type of the entered value is : String ", str(a))
          
check_type(a)
'''

'''

# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

MyVar = 25 #UpperCamelCase
myVar = 25 #LowerCamelCase
my_var = 25 #SnakeCase
MYVAR = 25 #UPPERCASE
'''

# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?

# Answer:
# Yes, if a different datatype is assigned to a, it will change the value of a. This is because Python is dynamic programmic language


