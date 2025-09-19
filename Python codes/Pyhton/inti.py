from traceback import print_tb

# Python Questions from Shreyansh AI school
#
# name = "Honey Verma"
# age = 20
#
# print(f"My name is {name} and i am {age} years old")

 

# name = input("Enter your name ")
# age = int(input("Enter Your age Here : "))
#
# ageForVote = 18 - age
#
# if age >= 18:
#     print(f"Hello {name} you are a valid voter.")
# else:
#     print(f"Hello {name} you are not a valid voter , you can vote after {ageForVote} year.")
#
# n = int(input("Enter the Number : "))
#
# for i in range(n):
#     print("Hello Honey How you doing")
# n = int(input("Enter the Number : "))
# for i in range(1,n+1):
#     print(i)
# n = int(input("Enter the Number : "))
# # for i in range(n,0, -1):
# #     print(i)
# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")
# n = int(input("Enter the Number : "))
# Sum = 0
# for i in range(1,n+1):
#     Sum = Sum +  i
# print(f"Your Sum is {Sum}")
# n = int(input("Enter the Number : "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)
#
# n = int(input("Enter the Number : "))
# Even_Sum = 0
# Odd_Sum = 0
#
# for i in range(1 , n+1):
#     if (i%2 == 0):
#         Even_Sum += i
#
#     else:
#         Odd_Sum += i
# print(f"Here is the Even Sum {Even_Sum}")
# print(f"Here is the Odd Sum {Odd_Sum}")
# n = int(input("Enter the Number : "))

# for i in range(1 , n+1):
#     if n % i == 0:
#         print(i)
# Sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         Sum += i
# if Sum == n :
#     print(Sum,",It is the perfect Number")
# else:
#     print(Sum,",It is not the perfect Number")
# n = int(input("Enter the Number : "))
# Count = 0
# for i in range(1 , n+1):
#     if n % i == 0:
#         Count += 1
# if Count == 2:
#     print(n,"It is the Prime Number")
# else:
#     print(n,"It is not the prime Number")

#  Reversing a String without Using the In-Build function---->
# a = "Honey"
# # Here in the loop first we will reach till the length of the string using len(a)-1 because indexing is started with 0 so we have to go till len(a)-1
# # The the Stop index is 0 , and we know that the stop is Excluded so we need to go -1.
# # And For reversing the string we need to go to the reverse direction by just -1 steps.
# for i in range(len(a) - 1, -1, -1):
#     print(a[i])

a = "honey".lower()
b = ""
for i in range(len(a) - 1 , -1, -1):
    b += a[i]
if b == a:
    print(a,",This string is palindrome")
else:
    print(a,",This string is not palindrome")