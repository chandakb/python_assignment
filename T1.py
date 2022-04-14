"""1. Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type."""

x,y,z=1,2.1,"abc"
print(x)
print(y)
print(z)

"""2. Create a variable of type complex and swap it with another variable of type integer."""

a=2+3j
print(int(abs(a)))


"""3. Swap two numbers using a third variable and do the same task without using any third variable."""

a=5
b=4

a,b=b,a
print(a)
print(b)

a=5
b=4
c=a
a=b
b=c
print(a)
print(b)




"""4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version."""
a=input("enter a number:")
#python 3  
print(a)
#python 2
print a


"""5.
Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output."""

x=int(input("enter a number between 1 to 10:"))
y=int(input("enter a number between 1 to 10:"))
if x<11 and y<11:
    z=x+y
    a=z+30
    print(a)
else:
    print("please enter a number between 1 and 10")   



"""6.
Write a program to check the data type of the entered values.
x=eval(input("enter a value:")) """

print(x)
print(type(x))


"""7.
Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE."""

MyVar=10
myVar=20
my_var=30
MYVAR=40

"""8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?

answer-yes it will change the value because python is dynamically typed programming language"