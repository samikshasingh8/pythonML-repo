'''
# 1> program that takes two numbers as input and prints their sum
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The sum of the numbers is =", num1+num2)

# 2>  program that checks whether a given number is even or odd
num=int(input("enter a number:"))
if num%2==0:
  print(num, "is an even number.")
else:
  print(num, "is an odd number.")
'''
# 3> program that calculates the factorial of a given number
n=int(input("enter a number:"))
f=1
for i in range(1,n+1):
  f*=i
print(f, 'is the factorial of', n)