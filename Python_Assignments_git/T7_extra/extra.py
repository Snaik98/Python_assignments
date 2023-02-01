

# 1. Create a list of given structure and get the Access list as provided below:
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list: [1, 2, 3, 4]Access list: [600, 700]
# Access list: [100, 300, 500, 600, 800]
# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list: [10]
# Access list: [ ]

'''
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

a = x[5]
print(a[0:4]) # Access list: [1, 2, 3, 4]
print(x[6:8]) # Access list: [600, 700]
print(x[0::2]) #Access list: [100, 300, 500, 600, 800]
print(x[::-1]) #Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
b = a[5]
print("[",b[0],"]") #Access list: [10]
print(x.clear()) # Access list: [ ] / None


'''


# 2. Create a list of thousand numbers using range and xrange and see the difference between each other.
# (For reference:https://www.techbeamers.com/python-xrange-range/)

##xrange is similar to range we use in python3.x while in python 2.x xrange worked as we use range in python3.x and range used to return a direct list of the whole range.
## in xrange we use for loops to iterate over objects.

'''
list = range(1,100) # python 2.x

list1 = [] #python 2.x
for x in xrange():
    list1.append(x)

'''

# 3. How Tuple is beneficial as compared to the list?

###Answer
# Tuples are immutable and these are beneficial in some scenarios when some data needs to be same wihout any modification to it. Lists take more memmory than lists.

# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and is a multiple of 2.
'''
a = []
for i in range(1,100):
    if(i % 3 == 0 and i % 2 == 0):
        a.append(i)

print(a)

'''

# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.

'''
string = input("Enter a string :")

rev_string = string[::-1]
count = 0
for i in rev_string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        print(i, count)
        count+=1
    else:
        count+=1
        continue

'''


# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an even length.

'''
string = 'hello my name is abcde'

words = string.split(' ')

for i in words:
    if(len(i) % 2 == 0):
        print(i)

'''

# 7. Write a program in python to print the pair of numbers whose result is equal to the result number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]
'''
def pair(x, n, result_no):
    mydict = dict()
    for i in range(n):
        temp = result_no - x[i]
 
        if temp in mydict:
            count = mydict[temp]
            for j in range(count):
                print("(", temp, ", ", x[i],")", sep="", end='\n')
 
        if x[i] in mydict:
            mydict[x[i]] += 1
        else:
            mydict[x[i]] = 1
 
if __name__ == '__main__':
 
    x = [1,2,3,4,5,6,7,8,9,-1]
    n = len(x)
    result_no = 8
 
    pair(x, n, result_no)

'''

# 8. Write a program in Python to complete the following task:
    # Create two lists such as even_list and odd_list
    # Ask user to enter a number in the range of 1,50 and make sure if the entered number is even, append it to the even_list and if the entered number is odd append it to the odd_list.
    # Keep that in mind you can only add 5 items in each list
    # Make sure once you enter all the 5 elements, calculate the sum of the list and return the maximum of the list.
'''
even_list = []
odd_list = []
even_list_count = 0
odd_list_count = 0

while True:
    n = int(input("Enter a number in the range of 1-50 :"))
    # print(n%2)
    if(even_list_count <5):
        if(n % 2 == 0):
            even_list.append(n)
            even_list_count += 1
    if(even_list_count ==5):
        print("Even List is full", even_list)
    if(odd_list_count <5):
        if(n % 2 != 0):
            odd_list.append(n)
            odd_list_count += 1
    if(odd_list_count ==5):
        print("Odd List is full",odd_list)
    if(odd_list_count and even_list_count == 5):
        break

    # print(even_list_count, odd_list_count)

print("Even List = ", even_list, "\nMax = ",max(even_list))
print("Odd List = ", odd_list, "\nMax = ",max(odd_list))

'''

# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.
'''
input_string = "12abcbacbaba344ab"

occ = {}

for i in input_string:
    if(i.isnumeric()):
        continue
    else:
        if i in occ:
            occ[i]+= 1
        else:
            occ[i]= 1

print("Occurence of characters in the given string = ", str(occ))

'''

# 10. Generate and print another tuple whose values are even numbers in the given tuple
# (1,2,3,4,5,6,7,8,9,10).
'''
tuple1 = (1,2,3,4,5,6,7,8,9,10)
list = []
for i in tuple1:
    if( i % 2 ==0):
        list.append(i)

tuple2 = tuple(list)

print(tuple2)

'''

