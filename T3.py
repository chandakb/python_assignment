"""1. Create a list of 10 elements of four different data types like int, string, complex and float."""

l=[1,2,3,10.5,20.5,"abc","ghi",4+5j,3+2j,10]
print(l)


"""2. Create a list of size 5 and execute the slicing structure"""

l2=[1,2,3,4,5]
print(l2[0:3])

"""3. Write a program to get the sum and multiply of all the items in a given list."""

l=[1,2,3,4,5]
sum=0
for i in l:
    sum=sum+i
print(sum)


l=[1,2,3,4,5]
multi=1
for i in l:
    multi=multi*i
print(multi)


"""4. Find the largest and smallest number from a given list."""

l1=[1,2,3,4,5]
print(min(l1))
print(max(l1))

"""5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list."""

l1=[1,2,3,4,5,6]
l2=[]
for i in l1:
    if i%2 != 0:
        l2.append(i)
print(l2)


"""6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included)."""

l1=[]
for i in range(1,31):
    if i <= 5 or i >= 25:
        l1.append(i*i)
print(l1)


"""7. Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]"""

l1=[1,3,5,7,9,10]
l2=[2,4,6,8]
l1.pop()
l1.extend(l2)
print(l1)


"""8. Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}"""

a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)


"""9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}"""

n=int(input("enter a number of dictionary elements in dictionary: "))
d1={}
for i in range(1,n+1):
    d1.update({i:i*i})
print(d1)


"""10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: ['34','67','55','33','12','98'] ('34','67','55','33','12','98')"""



x=input("enter a comma separated values: ")
l1=x.split(',')
t1=tuple(l1)
print("list: ",l1)
print("tuple: ",t1)