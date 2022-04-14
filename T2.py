
"""
1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string.
"""


x=int(input("enter a number: "))
if x%3==0 and x%5==0:
    print("Consultadd-Python Training")
elif x%3==0:
    print("Consultadd")
elif x%5==0:
    print("Python Training")


"""2. Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
"""
x=int(input("enter a value to perform action: "))
num1=int(input("enter a value for num1: "))
num2=int(input("enter a value for num2: "))
if x==1:
    z=num1+num2
    if z < 0:
        print("NEGATIVE")
    print(z)
elif x==2:
    z=num1-num2
    if z < 0:
        print("NEGATIVE")
    print(z)
elif x==3:
    z=num1/num2
    if z < 0:
        print("NEGATIVE")
    print(z)
elif x==4:
    z=num1*num2
    if z < 0:
        print("NEGATIVE")
    print(z)
elif x==5:
    first=int(input("enter a first number: "))
    second=int(input("enter a second number: "))
    z=(num1+num2+first+second)/4
    if z < 0:
        print("NEGATIVE")
    print(z)
else:
    print("please enter a value less than 6")



"""3. Write a program in Python to implement the given flowchart:"""

a=10
b=20
c=30
avg=(a+b+c)/3
print("avg=",avg)
if avg>a and avg>b and avg>c:
    print("avg is higher than a,b,c")
elif avg>a and avg>b:
    print("avg is higher than a,b")
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is just higher than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print("avg is just higher than c")



"""4. Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”"""

x=range(int(input("enter a number: ")),int(input("enter a number")))
for i in x:
    if i<0:
        print("it's Over")
        break
    print("good going")


"""5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200."""

x=range(2000,3201)
for i in x:
    if i%7==0 and i%5!=0:
        print(i)  



"""6. What is the output of the following code examples?
x=123
for i in x:
print(i)
"""
"""answer1-- int object is not iterable
   answer2-- 0
             error
             1 
             error
             2
    answer3--Break is not defined
    if i put break
    output is 0
              1
              2
              3
              4
             """


"""7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use 'continue' statement"""

x=[0,1,2,3,4,5,6]
for i in x:
    if i==3 or i==6:
        continue
    else:
        print(i)


"""8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2"""

x="abc1234"
letters=0
digits=0

for i in x:
    if i.isnumeric():
        digits += 1
    else:
        letters += 1  
print("letters: ",letters)
print("digits: ",digits) 

"""9. Read the two parts of the question below:
Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)
"""

import random 
guess_num=int(input("guess the lucky number: "))
while True:
    lucky_num=random.randint(1,5)
    print(lucky_num)
    if guess_num==lucky_num:
        break
    else:
        continue

while True:
    guess_num=int(input("guess the lucky number: "))
    lucky_num=random.randint(1,50)
    print(lucky_num)
    if guess_num==lucky_num:
        break
    else:
        answer=(input("do you want to guess again? y/n: "))
        if answer=='y':
            continue
        else:
            break



"""
10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as

While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.
"""

import random


counter=1
while counter <= 5:
    print("type in the" ,counter," number")
    guess_num=int(input("guess a lucky number: "))
    lucky_number=random.randint(1,50)
    if guess_num==lucky_number:
        print("good guess!")
    else:
        print("try again!")
    counter=counter+1
print("game over!")


"""11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”."""


import random


    
try:
    counter=1
    while counter <= 5:
        print("type in the" ,counter," number")
        guess_num=int(input("guess a lucky number: "))
        lucky_number=random.randint(1,50)
        if guess_num==lucky_number:
            print("good guess")
            break
        else:
            print("try again")
        counter=counter+1
    print("game over")
except ValueError:
         print("sorry but that was not very sucessful")









