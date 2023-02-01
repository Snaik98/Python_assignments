# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
'''
a = [1 , 2.0 , (1+3j), 'hello', 5 , 7.5, 'world', 55, (5+55j)]

'''
# 2. Create a list of size 5 and execute the slicing structure
'''
a = [1, 2, 3, 4, 5]

print(a[0:])
print(a[1:3])

'''

# 3. Write a program to get the sum and multiply of all the items in a given list.
'''
a = [1, 2, 3, 4, 5]
print("Sum of elements in list is : ", sum(a))

result_mul = 1
for x in a:
    result_mul = result_mul * x
print("Multiplication of all the elements in the list is :", result_mul )

'''

# 4. Find the largest and smallest number from a given list.
'''
a = [1, 2, 3, 4, 5]
print("Largest number:", max(a))
print("Smallest number:", min(a))

'''
# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
'''
a = [1, 2, 3, 4, 5]
b = []
for x in a:
    if(x%2 != 0):
        b.append(x)

print("New list without even numbers is :", b)
    
'''

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
'''
a = []
b =[]
for i in range(1, 31):
    a.append(i**2)
for i in a[:5]:
    b.append(i)
for i in a[-5:]:
    b.append(i)
print("List of squared number between 1 and 30 is: ", b)

'''

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]
'''
x, y= [1,3,5,7,9,10], [2,4,6,8]

x[-1:] = y

print(x)

'''

# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}
'''
a={1:10,2:20} 
b={3:30,4:40}

result = a | b
print(result)
a.update(b)
print(a)

'''

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
'''
n = int(input("Enter value:"))
dict ={}

for x in range(1,n+1):
    dict[x] = x*x

print(dict)

'''

# 10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
''''
numbers = [str(x) for x in input("Enter numbers separated by commas:\n").split(', ')]

print(numbers, tuple(numbers))

'''
