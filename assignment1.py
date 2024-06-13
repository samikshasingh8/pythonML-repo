'''
#1 program that takes two numbers as input and prints their sum
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The sum of the numbers is =", num1+num2)

#2 program that checks whether a given number is even or odd
num=int(input("enter a number:"))
if num%2==0:
  print(num, "is an even number.")
else:
  print(num, "is an odd number.")

#3 program that calculates the factorial of a given number
n=int(input("enter a number:"))
f=1
for i in range(1,n+1):
  f*=i
print(f, 'is the factorial of', n)

#4 program that asks the user for their name and then prints a greeting message
name=str(input("Enter your name: "))
print("Hello,", name, "! Hope you're having a good day")

#5> program that takes a string input from the user and writes it to a text file
user_input = input("Enter a string: ")
with open("output.txt", "w") as file:
    file.write(user_input)

#6 program that reads the content of a text file and prints it to the console
with open("output.txt", "r") as file:
     content = file.read()
     print(content)

#7 program that takes a string as input and returns its length
str1=input("Enter a string: ")
print("The length of the string is:", len(str1))

#8 program that concatenates two strings and returns the result
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Concatenated string is", str1 + str2)

#9 program that checks if a substring is present in a given string
mstring = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in mstring:
    print("Substring found!")
else:
    print("Substring not found.")

#10 program that converts a given string to uppercase
lowstring = input("Enter a string: ")
print("Uppercased string:", lowstring.upper())

#11 program that generates the first n numbers in the Fibonacci sequence
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = [0, 1]
while len(fib_sequence) < n:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
print(fib_sequence[:n])

#12 program that calculates the sum of the digits of a given number
number = int(input("Enter a number: "))
print("Sum of the digits is:", sum(int(digit) for digit in str(number)))

#13 program that asks the user for their birth year and calculates their age
birth_year = int(input("Enter your birth year: "))
current_year = 2024
age = current_year - birth_year
print(f"You are {age} years old.")

#14 program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines
lines = []
while True:
    line = input("Enter a line (leave empty to finish): ")
    if line == "":
        break
    lines.append(line)
for line in lines:
    print(line)
'''
#15 program that reads data from a CSV file and prints it to the console
import csv
with open("data.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(", ".join(row))
