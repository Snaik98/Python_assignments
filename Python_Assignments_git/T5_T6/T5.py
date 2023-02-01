

# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
'''
try:
    eval('a === a')
except SyntaxError:
    print("Syntax Error!!")

'''

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. 
#     Make sure to use read only mode.
##  used the same file_name from question 6 to check the name
### python T5.py doc.txt

'''
import sys
# i =0
while True:
    if sys.argv[1] == "doc.txt":
        with open("E:\Python\Consultadd Assignments\Python_Assignments\Python_Assignments_git\T5_T6\doc.txt", "r" ) as f:
            print(f.read())
        break
    else:
        print("try again")
        break


'''

# 3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”

'''
import sys
x = int(input("Enter a 4 digit number: "))
if (len(str(x))== 4):
        print("input accepted!")
else:
    print("The length is too short/long !!! Please provide only four digits")

'''

# 4. Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to 
#     enter it again but it should not be more than 3 times.
'''
i = 0
username = input("Enter Username :")
password = input("Enter your password :")

while i <=3:
    re_password = input("Enter your password :")
    if(password == re_password):
        print("Passwords Match!! User created successfully!!")
    else:
        print("Try Again, You got",3-i, "tries left")
        i+=1
print("Try again after sometime!!")

'''

# 5. Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling

### Done

# 6. Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

'''
with open("E:\Python\Consultadd Assignments\Python_Assignments\Python_Assignments_git\T5_T6\doc.txt", "r") as f:
    for line in f:
        if(len(line) % 2 == 0):
            print(line,"(Lenth of this line is", len(line), ")")

'''