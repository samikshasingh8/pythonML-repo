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

#15 program that reads data from a CSV file and prints it to the console
import csv
file_path = input("Enter the CSV file path: ")
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

#16 program in Python that counts the frequency of each character in a string
user_input = input("Enter a string: ")
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

#17 program in Python that converts a given string to title case
user_input = input("Enter a string: ")
print(string.title())

#18 program that checks if two strings are anagrams of each other
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#19 program that removes all punctuation from a given string
import string
user_input = input("Enter a string: ")
for punctuation in string.punctuation:
    user_input = user_input.replace(punctuation, "")
print("String without punctuation:", user_input)

#20 program that takes a list of numbers and returns their sum
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Sum of the list is:", sum(numbers))

#21 program that counts the occurrences of a specific element in a list
lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
print(f"{element} occurs {lst.count(element)} times.")

#22 program that returns the minimum and maximum values in a list of numbers
lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
minimum, maximum = min(lst), max(lst)
print(f"Minimum value is {minimum}, Maximum value is {maximum}.")

#23 program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
f_to_c=1
c_to_f=2
choice=int(input("enter 1 for ^f to ^c conversion or enter 2 for ^c to ^f conversion:"))
if choice==1:
  f=float(input('Enter temperature in Fahrenheit:'))
  con1=(f-32)/1.8
  print("The temperature is",con1,"degree Celsius")
elif choice==2:
  c=float(input('Enter temperature in Celsius:'))
  con2=(c*1.8)+32
  print("The temperature is",con2,"degree Fahrenheit")

#24 program that acts as a simple calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = "Invalid operator"
print("The result is: ", result)

#25 program that copies the contents of one text file to another
src = input("Enter the source file path: ")
dest = input("Enter the destination file path: ")
with open(src, "r") as source_file:
    content = source_file.read()
with open(dest, "w") as destination_file:
    destination_file.write(content)

#26 program that checks if a string starts with a given prefix or ends with a given suffix
string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
starts_with = string.startswith(prefix)
ends_with = string.endswith(suffix)
print(f"String starts with {prefix}: {starts_with}")
print(f"String ends with {suffix}: {ends_with}")

#27 program that converts a string into a list of its characters
user_input = input("Enter a string: ")
print(list(string))
'''
