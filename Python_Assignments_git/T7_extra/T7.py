
'''
# 1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

import math

C = 50
H = 30
numbers = [int(x) for x in input("Enter values for D:").split(",") ]
print(numbers)
answers = []

for D in numbers:
    temp = (2 * C * D) / H
    Q = math.sqrt(temp)
    answers.append(Q)

print(answers)

'''

'''
# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument. Both classes have an area function which can 
#     print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Area of shape is :", 0)

class Square(Shape):
    def __init__(self, length):
        self.length = length
        super(Square, self).__init__()

    def area(self):
        a = self.length * self.length
        print("Area of square is :", a)

s = Square(4)
s.area()

'''

# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]

'''
class sum_to_zero:
    def sum_of_three(self, digits):
        answer = []
        digits = sorted(digits)
        x = 0
        while x < len(digits) - 2:
            y, z = x + 1, len(digits) - 1
            while y < z:
                if digits[x] + digits[y] + digits[z] < 0:
                    y += 1
                elif digits[x] + digits[y] + digits[z] > 0:
                    z -= 1
                else:
                    answer.append([digits[x], digits[y], digits[z]])
                    y, z = y + 1, z - 1
                    while y < z and digits[y] == digits[y - 1]:
                        y += 1
                    while y < z and digits[z] == digits[z + 1]:
                        z -= 1
            x += 1
            while x < len(digits) - 2 and digits[x] == digits[x - 1]:
                x += 1
        return answer

print(sum_to_zero().sum_of_three([-25,-10,-7,-3,2,4,8,10]))

'''

# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

'''
import re

class Time:
    def __init__(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins

    def displayTime(self,final_hrs, final_mins):
        print(final_hrs,"hr and", final_mins, "min")

    def addTime(self, ele1, ele2):
        hr1 = re.findall(r'(\d+) hour', ele1)
        min1 = re.findall(r'(\d+) min', ele1)
        hr2 = re.findall(r'(\d+) hour', ele2)
        min2 = re.findall(r'(\d+) min', ele2)


        min1 = int(''.join(min1))
        min2 = int(''.join(min2))

        hr1 = int(''.join(hr1))
        hr2 = int(''.join(hr2))

        temp1 = min1 + min2
        # print (temp1)
        final_mins = 0
        final_hrs = 0
        if temp1 > 60:
            final_mins = temp1 - 60
            final_hrs += 1
        else:
            final_mins = temp1
        
        final_hrs = final_hrs + hr1 + hr2

        def displayTime(final_hrs, final_mins):
            print(final_hrs,"hr and", final_mins, "min")

        displayTime(final_hrs, final_mins)
        
        def displayMinute(final_hrs, final_mins):
            conv_minutes = final_hrs * 60
            final_mins = final_mins + conv_minutes
            print(final_mins, "mins")
        
        displayMinute(final_hrs, final_mins)
        
time = Time(hrs=0, mins=0)

ele1 = input("Enter hours and min in format (<int> hour and <int> min) :")
ele2 = input("Enter hours and min in format (<int> hour and <int> min) :")
time.addTime(ele1, ele2)



        
'''
        





# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# --yearPasses() should increase age by the integer value that you are passing inside the function.
# --amIOld() should perform the following conditional actions:If age is between 0 and <13, print “You are young”.
#   If age is >=13 and <=19 , print “You are a teenager”.
#   Otherwise, print “You are old”.
'''
class Person:
    def __init__(self, age):
        self.age= age
    def age_of_person(self):
        if self.age < 0 :
            self.age= 0
            print("Age is not valid, setting age to 0")
        else:
            print("Your age is", self.age)

    def yearPasses(self,inc):
        if int(self.age) > 0 :
            print(self.age + inc)

    def amIOld(self):
        if int(self.age) > 0 :
            if(0 < self.age <13):
                print("You are young")
            elif(13 <= self.age <=19):
                print("You are a teenager")
            else:
                print("You are Old")

x = int(input("Enter your age: "))
person = Person(x)

person.age_of_person()
person.yearPasses(20)
person.amIOld()
'''






