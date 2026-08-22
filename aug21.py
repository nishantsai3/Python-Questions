
#Create a list of 5 numbers and add a new number at the end.
list = [1,2,3,4,5]
list.append(6)
print(list)

#Create a list of names and insert "Rahul" at index 2.
list = ["Ram","Hari","Maddy"]
list[2] = "Rahul"
print(list)

#Given [10, 20, 30, 20, 40, 20], remove the first occurrence of 20.
list = [10, 20, 30, 20, 40, 20]
for i  in list:
    if i==20:
        list.remove(i)
        break 
print(list)

#Given [5, 2, 8, 1, 9], sort the list in ascending and descending order.
list_l = [5, 2, 8, 1, 9]
asc = list_l.sort()
desc = list_l.sort(reverse=True)
print(asc)
print(desc)

#Given [10, 20, 30, 40, 50], remove the last element and print the removed element.
l = [10, 20, 30, 40, 50]
ans = l.pop()
print(ans)

#Given [1, 2, 2, 3, 2, 4], find how many times 2 occurs.
lst = [1, 2, 2, 3, 2, 4]
print(lst.count(2))

#Given ["apple", "banana", "mango", "orange"], find the index of "mango".
lst = ["apple", "banana", "mango", "orange"]
print(lst.index("mango"))

#Create two lists and combine the second list into the first using extend().
l = [10, 20, 30, 40, 50]
lst = [1, 2, 2, 3, 2, 4]
l.extend(lst)
print(l)

#Create a tuple (10, 20, 10, 30, 10, 40) and find how many times 10 occurs.
tup = (10, 20, 10, 30, 10, 40)
print(tup.count(10))

#Given the tuple ("Python", "Java", "C++", "JavaScript"), find the index of "C++".
tup = ("Python", "Java", "C++", "JavaScript")
print(tup.index("C++"))





#Set — 10 Questions
#Create a set of 5 numbers and add a new number using add().
myset = {1,2,3,4,5}
myset.add(6)
print(myset)

#Given {10, 20, 30, 40}, remove 30 from the set.
myset = {10, 20, 30, 40}
myset.remove(30)
print(myset)

#Given {1, 2, 3} and {3, 4, 5}, find their union.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
ans = set1.union(set2)
print(ans)

#Given {1, 2, 3, 4} and {3, 4, 5, 6}, find their intersection.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
ans = set1.intersection(set2)
print(ans)

#Given {1, 2, 3, 4} and {3, 4, 5}, find the elements present only in the first set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
ans = set1 - (set2)
print(ans)

#Given {1, 2, 3} and {2, 3, 4}, find the symmetric difference.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
ans = set1.symmetric_difference(set2)
print(ans)

#Create a set containing duplicate values and remove all duplicates.
myset = {1, 2, 2, 3, 3, 4, 4, 5}
print(myset)


#Given two sets, check whether they have any common elements.
set1 = {0, 5, 3, 4}
set2 = {3, 9, 0, 2}
ans = set1.intersection(set2)
print(ans)

#Create a set and remove all its elements using clear().
myset = {10, 20, 30, 40}
myset.clear()
print(myset)

#Given {10, 20, 30, 40}, check whether 20 exists in the set.
myset = {10, 20, 30, 40}
print( 20 in myset)



#Dictionary — 10 Questions
#Create a dictionary containing a student's name, age, and marks and print each value.
mydict = {
    "name" : "Nishant",
    "age" : 21,
    "marks" : 100
}
print(mydict)

#Given {"name": "Rahul", "age": 20}, add a new key city.
mydict = {"name": "Rahul", "age": 20}
mydict["city"] = "Hyderabad"
print(mydict)

#Given {"name": "Rahul", "age": 20}, update the age to 21.
mydict = {"name": "Rahul", "age": 20}
mydict["age"] = 21
print(mydict)

#Given {"name": "Rahul", "age": 20, "city": "Hyderabad"}, remove the city key.
mydict = {"name": "Rahul", "age": 20, "city": "Hyderabad"}
mydict.pop("city")
print(mydict)

#Given a dictionary, check whether a particular key exists.
mydict = {"name": "Rahul", "age": 20, "city": "Hyderabad"}
print("city" in mydict)

#Given {"apple": 50, "banana": 30, "mango": 40}, print all the keys.
mydict = {"apple": 50, "banana": 30, "mango": 40}
print(mydict.keys())

#Given {"apple": 50, "banana": 30, "mango": 40}, print all the values.
mydict = {"apple": 50, "banana": 30, "mango": 40}
print(mydict.values())

#Given a dictionary, use items() to print every key and value.
mydict = {"apple": 50, "banana": 30, "mango": 40}
print(mydict.items())

#Given {"a": 10, "b": 20, "c": 30}, find the sum of all values.
mydict = {"a": 10, "b": 20, "c": 30}
ans = 0 
for num in mydict.values():
    ans+=num 
print(ans)

#Given a dictionary containing student names and marks, find the student who has the highest marks.
mydict = {"a": 10, "b": 20, "c": 30, "d": 40}
ans = 0 
for num in mydict.values():
    if num>ans:
        ans=num
print(ans)












"""Python Practice Questions — 30 Questions"""

#1. Basics & Input/Output
#Take two integers as input and print their sum, difference, product, and division.
num1 = int(input())
num2 = int(input())
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

#Take a user's name and age as input and print: Hello Rahul, you are 21 years old.
name = input()
age = int(input())
print("Hello "+name+", you are "+str(age)+"  years old.")

#Take a number as input and check whether it is positive, negative, or zero.
n=int(input())
if(n>0):
    print("positive")
elif(n==0):
    print("zero")
else:
    print("negative")

#Take three numbers as input and print the largest number.
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)

#2. Strings
#Take a string as input and count the number of vowels in it.
str = input()
count = 0
for ch in str:
    if(ch in ['a','e','i','o','u']):
        count+=1 
print(count)

#Take a string and print it in reverse without using a built-in reverse function.
str = input()
ans = ""
for ch in str:
    ans = ch+ans 
print(ans)

#Take a string and check whether it is a palindrome.
str = input()
rev = ""
for ch in str:
    rev = ch+rev 
print(str==rev)

#Take a sentence and find the longest word in it.
words =  input().split(" ")
ans = ""
for word in words:
    if len(ans)<len(word):
        ans = word 
print(ans)

#3. Conditional Statements & Loops
#Print all numbers from 1 to 100 that are divisible by both 3 and 5.
for i in range(1,101):
    if(i%5==0 and i%3==0):
        print(i)

#Take a number n and print its multiplication table from 1 to 10.
n = int(input())
for i in range(1,11):
    print(str(n)+" * "+str(i)+" = "+str(n*i))

#Take a number and find the sum of its digits.
n = int(input())
ans = 0
while(n>0):
    ans += n%10
    n //= 10
print(ans)

#Take a number and check whether it is a prime number.
n = int(input())
if n<2:
    print(False)
elif n<4:
    print(True)
else:
    b = True
    for i in range(2,n//2+1):
        if(n%i==0):
            print(False)
            b = False
            break
    if(b):
        print(True)

#Print the following pattern for n = 5: *, **, ***, ****, ***** (one row per line).
n=int(input())
for i in range(1,n+1):
    print("*"*i)


#4. Lists
#Given a list of numbers, find the largest and smallest element without using max() or min().
lst = list(map(int,input().split(" ")))
min = lst[0]
max = lst[0]
for num in lst:
    if num<min:
        min = num 
    if num>max:
        max = num 
print(min)
print(max)

#Given a list, create a new list containing only the even numbers.
lst = list(map(int,input().split(" ")))
ans = []
for num in lst:
    if num%2==0:
        ans.append(num)
print(ans)

#Given [10, 20, 10, 30, 20, 40, 30], remove the duplicates and create a list containing only unique values.
lst = [10, 20, 10, 30, 20, 40, 30]
uni = []
dup = []
for i in lst:
    if i in uni:
        dup.append(i)
    else:
        uni.append(i)
for i in dup:
    uni.remove(i) 
print(uni)


#Given a list of numbers, find the second-largest element.
lst = list(map(int,input().split(" ")))
max = lst[0]
secmax = lst[0]
for num in lst:
    if num>max:
        secmax = max
        max = num
    elif num>secmax:
        secmax = num 
print(secmax)


#5. Tuples
#Given a tuple of numbers, find the sum, maximum, and minimum values.
tup = tuple(map(int,input().split(" ")))
sum = 0
min = tup[0]
max = tup[0]
for num in tup:
    sum+=num
    if num<min:
        min = num 
    if num>max:
        max=num
print(min)
print(max)
print(sum)

#Given the tuple (10, 20, 10, 30, 10, 40, 20), find how many times 10 and 20 occur.
tup = (10, 20, 10, 30, 10, 40, 20)
print(tup.count(10))
print(tup.count(20))


#6. Sets
#Given two sets, find their union, intersection, and difference.
set1 = set(map(int,input().split(" ")))
set2 = set(map(int,input().split(" ")))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1-set2)

#Given a list of numbers, use a set to find all the duplicate elements.
lst = list(map(int,input().split(" ")))
dup = set()
temp = set()
for num in lst:
    if num in temp:
        dup.add(num)
    else:
        temp.add(num)
print(dup)

#Given two sets of student names, find the students who are present in both sets.
set1 = set(input().split(" "))
set2 = set(input().split(" "))
print(set1.intersection(set2))



#7. Dictionaries
#Given students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}, find the student with the highest marks.


#Given a dictionary containing student names and marks, calculate the average marks.


#Take a sentence as input and create a dictionary containing the frequency of each word. Example: "apple banana apple mango banana apple" → {"apple": 3, "banana": 2, "mango": 1}.


#Given two dictionaries, combine them into a single dictionary.



#8. Functions
#Write a function is_prime(n) that returns True if a number is prime and False otherwise.
def is_prime(n):
    if n<2:
        return False
    elif n<4:
        return True
    else:
        for i in range(2,n//2+2):
            if(n%i==0):
                return False
        return True
        
print(is_prime(int(input())))

#Write a function find_largest(numbers) that takes a list of numbers and returns the largest number without using max().
def find_largest(numbers):
    if len(numbers)==0:
        return 0
    ans = 0
    for i in numbers:
        if i>ans:
            ans=i 
    return ans
        
print(find_largest(list(map(int,input().split(" ")))))


#9. Basic Recursion
#Write a recursive function to calculate the factorial of a number. Example: Input 5 → Output 120.
def fact(num):
    if num<=1:
        return 1 
    return num*fact(num-1)
        
print(fact(int(input())))

#Write a recursive function to find the sum of numbers from 1 to n. Example: Input 5 → Output 15.
def numsum(num):
    if num<=1:
        return 1 
    return num+numsum(num-1)
        
print(numsum(int(input())))