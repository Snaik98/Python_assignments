'''
# 1. Write a program in Python to perform the following operation:
#     If a number is divisible by 3 it should print “Consultadd” as a string
#     If a number is divisible by 5 it should print “Python Training” as a string
#     If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.


a = int(input("Enter any int number:"))

if(a % 3 == 0 and a % 5 == 0):
    print("Consultadd - Python Training")
elif(a % 3 == 0 ):
    print("Consultadd")
elif(a % 5 == 0):
    print("Python Training")

'''
'''
# 2. Write a program in Python to perform the following operator based task:
    # Ask user to choose the following option first:
    #     If User Enter 1 - Addition
    #     If User Enter 2 - Subtraction
    #     If User Enter 3 - Division
    #     If User Enter 4 - Multiplication
    #     If User Enter 5 - Average
    # Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
    # Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
    # At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
    # NOTE: At a time a user can only perform one action.

x = int(input("Enter Your choice: \n Enter 1 - Addition \n Enter 2 - Subtraction \n Enter 3 - Division \n Enter 4 - Multiplication \n Enter 5 - Average \n -->" ))

result = 0

if(x < 5):
    num1, num2 =  [int(y) for y in input("Enter any 2 numbers :").split()]
    if(x == 1):
        result = num1 + num2
    elif(x == 2):
        result = num1 - num2
    elif(x == 3):
        result = num1 / num2
    elif(x ==4):
        result = num1 * num2
      
elif(x == 5):
    nums = [int(x) for x in input("Enter 2 or more numbers : ").split()]
    result = sum(nums)/ len(nums)

print("Result is =",result)
if(result < 0):
    print("NEGATIVE")

'''
'''
# 3. Write a program in Python to implement the given flowchart:

a, b, c = 10, 20, 30
avg = (a + b + c)/3
print("avg =", avg)

if(avg > a and avg > b and avg > c):
    print("Average is higher than a, b, c")
else:
    if(avg > a and avg > b):
        print("AVergae is higher than a, b")
    else:
        if(avg > a and avg > c):
            print("Average is higher than a, c")
        else:
            if(avg > b and avg >c):
                print("Average is higher than b, c")
            else:
                if(avg > a):
                    print("Average is just higher than a")
                else:
                    if(avg > b):
                        print("Average is just higher than b")
                    else:
                        if(avg > c):
                            print("Average is just higher than c")

'''
'''
# 4. Write a program in Python to break and continue if the following cases occurs:
#     If user enters a negative number just break the loop and print “It’s Over”
#     If user enters a positive number just continue in the loop and print “Good Going”

while True:
    x = int(input("Enter any number:"))

    if( x < 0):
        print("It's Over")
        break
    elif( x > 0):
        print("Good Going")
        continue

'''
'''
# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

a = []
for x in range(2000, 3201):
    if(x%7 == 0 and x%5 != 0):
        a.append(x)
print("The numbers are : ", a) 

'''

# 6. What is the output of the following code examples?

#6.1
# x = 123
# for i in x:
#     print(i)

###Output: TypeError, Int is not iterable

#6.2
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print(“error”)

#6.3
##Output:
# 0
# error
# 1
# error
# 2

#6.4
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break

### Output:
# 0
# 1
# 2
# 3
# 4

'''
# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

for x in range(0, 7):
    if( x == 3 or x ==6):
        continue
    else:
        print(x)

'''
'''
# 8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2

s = input("Enter a alphanumeric string:")
digits = 0
letters = 0

for x in s:
    if  x.isnumeric():
        digits += 1
    else:
        letters += 1

print("Letters", letters,"Digits", digits)

'''

# 9. Read the two parts of the question below:
    # Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
'''
x = 5
while True:
    number = int(input("Guess the lucky number:"))
    if(x == number):
        print("Good Guess")
        break
    else:
        print("Try Again")
        continue

'''

    # Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number 
    #   and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number 
    #       or answers “no”. (The program continues as long as a user has not answered “no” and has not guessed the correct number)

'''
x = 5
while True:
    number = int(input("Guess the lucky number:"))
    if(x == number):
        print("Good Guess")
        break
    else:
        answer = input("Do you want to try again (yes/no):").lower()
        if(answer == 'no'):
            break
        elif(answer == 'yes'):
            continue

'''
# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as

#     counter = 1
#     While counter <= 5:
#         print(“Type in the”, counter, “number”
#         counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, 
# otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
'''
counter = 1
a = 2
while counter <=5:
    number = int(input("Type in your guess : "))
    if(number == a):
        print("Good Guess!!")
        counter+=1
    else:
        print("Try Again! ")
        counter+=1
print("Game Over!!")

'''

# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue 
#     guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.
'''
counter = 1
a = 2
while counter <=5:
    number = int(input("Type in your guess : "))
    if(number == a):
        print("Good Guess!!")
        break
    else:
        print("Try Again! ")
        counter+=1

if(counter >= 5):
    print("Sorry but that was not very successful")

'''