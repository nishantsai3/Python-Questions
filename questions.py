"""
1. Sequence of Instructions
Write a program that takes a number N and:
Adds 10
Multiplies the result by 2
Subtracts 5
Divides the result by 3
Print the final result.

"""

n = int(input())
print((((n+10)*2)-5)/3)

"""
2.. Type Conversions
Given:
x = "25"
y = 4.5
z = 10
Convert and calculate:
x + z
x * 2
y + z
Print the results along with their data types.
"""
x = int("25")
y = 4.5 
z = 10 

print(x+z)
print(type(x+z))
print(x*2)
print(type(x*2))
print(y+z)
print(type(y+z))

"""
3. Logical Operators
Given three integers a , b , and c , print True if:
a is greater than b AND b is greater than c
OR a is equal to c
Otherwise, print False .

"""
a = int(input())
b = int(input())
c = int(input())

if((a>b and b>c)or a==c):
    print(True)
else:
    print(False)


"""
4. Logical Operators + Conditions
Given a person's age and has_id , a person can enter a club if:
Age is at least 18 AND they have an ID.
Print "Allowed" or "Not Allowed" .
"""
age = int(input())
has_id = bool(input())
if(age>=18 and has_id==True):
    print("Allowed")
else:
    print("Not Allowed")


"""
5. Given an integer N , print all numbers from 1 to N that are divisible by both 3 and 5 .
Example:
Input: 30
Output: 15 30
"""
n = int(input())
for i in range(1,n+1):
    if(i%5==0 and i%3==0):
        print(i,end=" ")


"""
6. Loops + Arithmetic
Given N , calculate the sum of all even numbers from 1 to N .
Example:
Input: 10
Output: 30

"""
n = int(input())
sum =0
for i in range(1,n+1):
    if(i%2==0 ):
        sum += i
print(sum)

"""
7. Loops + Conditions
Given a number N , count how many digits in the number are even.
Example:
Input: 583246
Output: 4

"""
n = int(input())
count =0
while(n>0):
    if((n%10)%2==0):
        count +=1
    n = n/10
print(count)


"""
8. String Methods
Given the sentence:
Python is very easy to learn
Write a program to: 1. Count the number of words. 2. Convert the sentence to uppercase. 3. Replace 
"easy" with "powerful" .
"""
string = "Python is very easy to learn".upper()
string = string.split(" ")
ans=""
for word in string:
    if word=="EASY":
        ans+="POWERFUL"+" "
    else:
        ans+=word+" "
print(len(string))
print(ans)


"""
9. String Comparison
Given a sentence containing space-separated words, print the lexicographically smallest word.
Example:
Input:
banana apple mango cherry
Output:
apple
Do not use min() .
"""
string = input().split(" ")
answer = string[0]
for word in string:
    if(word<answer):
        answer = word
print(answer)


"""
10. String Methods + Loops
Given a string, count how many characters are:
Vowels
Consonants
Digits
Example:
Input:
hello123
Output:
Vowels: 2
Consonants: 3
Digits: 3
"""
string = input()
vowel = 0
consonant = 0
digit = 0
for word in string:
    if word.isdigit():
        digit += 1 
    if word.isalpha():
        if(word in ['a','e','i','o','u']):
            vowel += 1 
        else:
            consonant += 1 

print("vowel : "+ str(vowel) )
print("consonant : "+str(consonant))
print("digit : " + str(digit))

"""
11. Loop Control – break
Keep taking numbers from the user until the user enters 0 .
Print the sum of all numbers entered before 0 .
Example:
Input:
10
20
5
0
Output:
35
"""
sum = 0
while True :
    num = int(input())
    if(num==0):
        break
    sum+=num
print(sum)


"""
12. Loop Control – continue
Given a number N , print numbers from 1 to N , but skip numbers divisible by 3 .
Example:
Input: 10
Output:
1 2 4 5 7 8 10
"""
num = int(input())
for n in range(1,num+1):
    if(n%3==0):
        continue 
    print(str(n),end=" ")


"""
13. Lists
Given:
numbers = [12, 5, 8, 21, 4, 15, 10]
Find:
Largest number
Smallest number
Sum of all numbers
Do not use max() , min() , or sum() .
"""
numbers = [12,5,8,21,4,15,10]
lar = numbers[0]
small = numbers[0]
numsum = 0 
for i in numbers:
    if i>lar:
        lar = i 
    if(i<small):
        small = i 
    numsum += i 
print(lar)
print(small)
print(numsum)


"""
14. Lists + Loops
Given a list of integers, create a new list containing only numbers greater than 10 .
Example:
Input:
[4, 15, 8, 21, 3, 17]
Output:
[15, 21, 17]
"""
numbers = [4,15,8,21,3,17]
answer = []
for num in numbers:
    if num>10:
        answer.append(num)
print(answer)


"""
15. Lists + Conditions
Given a list of numbers, count how many numbers occur more than once.
Example:
Input:
[1, 2, 3, 2, 4, 1, 5]
Output:
2
Here, 1 and 2 are repeated.
"""
nums = [1, 2, 3, 2, 4, 1, 5]
uni = []
ans = []
for i in nums:
    if i in uni:
        ans.append(i)
    else:
        uni.append(i)
print(ans)

"""
16. List Methods
Given:
students = ["Rahul", "Aman", "Priya", "Neha"]
Perform the following operations:
Add "Karan" at the end.
Add "Sneha" at index 2 .
Remove "Aman" .
Sort the list.
Reverse the list.
Print the final list.
"""
students = ["Rahul", "Aman", "Priya", "Neha"]
students.append("Karan")
students[2] = "Sneha"
students.remove("Aman")
students.sort()
students.reverse()
print(students)

"""
17. Nested Lists
Given:
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Calculate the sum of all elements.
Expected output:
45
"""
numbers = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
nsum=0
for i in range(len(numbers)):
    for j in numbers[i]:
        nsum += j
print(nsum)


"""
18. Lists + Strings
Given:
words = ["apple", "banana", "kiwi", "orange", "grape"]
Create a new list containing only words whose length is greater than 5 .
Expected output:
["banana", "orange"]
""" 
words = ["apple", "banana", "kiwi", "orange", "grape"]
ans = []
for word in words:
    if len(word)>5:
        ans.append(word)
print(ans)


"""
19. Combined Question
Given the sentence:
Python is easy and Python is powerful
Convert it into a list of words and find how many times "Python" occurs.
Expected output:
2
Do not use count() .
"""
string = "Python is easy and Python is powerful"
string = string.split(" ")
count = 0;
for word in string:
    if(word == "Python"):
        count += 1 
print(count)

"""
20. Combined Challenge
Given:
numbers = [10, 25, 30, 45, 50, 75, 90, 100]
Create a new list containing numbers that:
Are greater than 30
Are divisible by 5
Do not include 75
Expected output:
[45, 50, 90, 100]
"""
numbers = [10, 25, 30, 45, 50, 75, 90, 100]
answer = []

for num in numbers:
    if num>30 and num%5==0 and num!=75:
        answer.append(num)
print(answer)

