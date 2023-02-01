# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
'''
a = '1234abcd'
print(a[:-1])

'''

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
'''
def func():
    str1 = input("Enter a string with Uppercase & lowercase letters: ")
    upper = 0
    lower = 0
    for i in str1:
        if(i.islower()):
            lower+=1
        else:
            upper+=1
    print("No. of Uppercase characters :", upper, "No. of Lower case Characters :", lower)

func()

'''

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
'''
def distinct(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    print("Unique list: ",list2)

list1 = [10, 20, 20, 30, 30, 30, 40, 50, 50]
distinct(list1)

'''

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

'''
list=[n for n in input("Enter words separated by hyphens:").split('-')]
list.sort()
print('-'.join(list))

'''

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
'''
string = input("Enter a sequence of words:")
print(string.upper())

'''

# 6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.

'''
def add(a, b):
    sum = int(a) + int(b)
    print("Sum is: ",sum)

a, b = input("Enter 2 integers: ").split(' ')
add(a,b)

'''

# 7. Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function 
#     should print both the strings line by line.
'''
def comp_string(str1, str2):
    if(len(str1)==len(str2)):
        print("First Sring: ",str1,"\nSecond String: ",str2)
        print("Both are equal in length")
    elif(len(str1)>len(str2)):
        print(str1)
    else:
        print(str2)

str1 = input("Enter 1st string:")
str2 = input("Enter 2nd string:")

comp_string(str1, str2)

'''

# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).

'''
def sq():
    a = []
    for i in range(1,21):
        a.append(i**2)
    b = tuple(a)
    print(b)
sq()

'''

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3)(where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
'''
def showNumbers(limit):
    for i in range(0, limit+1):
        if (i%2 == 0):
            print(i, " EVEN")
        else:
            print(i, " ODD")

limit = int(input("Enter the limit:"))
showNumbers(limit)

'''

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
'''
def even(a):
    if a % 2 == 0:
          return True  
    else:
        return False

a =[]
for n in range(1,21):
    a.append(n)

x = filter(even, a)

even_no_list = list(x)

print(even_no_list)

'''

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the numbers in the filtered list. Use lambda() to define anonymous functions.

'''
def even(numbers):
    if numbers % 2 == 0:
          return True  
    else:
        return False

numbers = [1,2,3,4,5,6,7,8,9,10]
x = filter(even, numbers)
even_no_list = list(x)
# print(even_no_list)

def square(even_no_list):
    return even_no_list**2

y = map(square, even_no_list)
sq_list = list(y)

print(sq_list)

'''

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
'''
def func():
    try:
        a =5/0
        print(a)
    except ZeroDivisionError:
        print("Division by zero not possible")

func()

'''

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
'''
# import operator
import functools
a = [1,2,3,4,5,6,7]


def rem_commas(a):
    result =''
    for x in a:
        result = result + str(x)
    print(result)
        
# print(functools.reduce(rem_commas, a))
rem_commas(a)


'''
        

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7. Make sure to use only higher order functions.

'''
def check_num(num):
    if(num % 3 != 0 and num % 7 == 0):
        print("Yes ", num, "is not divisible by 3 but is a multiple of 7")
    else:
        print("Wrong!!")

num = 28
check_num(num)

'''

# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.

'''
def multiply(list1):
    return list1*list1

list1 = [1, 2, 3, 4]
y = map(multiply, list1)
mul_list = list(y)

print(mul_list)

'''

# 16. What is the output of the following codes:
# (i) def foo():
#         try:
#             return 1
#         finally:
#             return 2
#         k = foo()
#         print(k)

#### Output:
# 2

# (ii) def a():
# try:
# f(x, 4)
# finally:
# print('after f')
# print('after f?')
# a()

# Output:
# f is not defined


