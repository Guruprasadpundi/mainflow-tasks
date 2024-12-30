# Write a program to calculate the sum of two numbers.

num1 = int(input("Enter fast number:"))
num2 = int(input("Enter second number:"))

r = num1 + num2

print(f'sum of two number: {r}')


# Determine whether a number is odd or even

num1 = int(input("Enter a number:"))

if num1 %2 == 0 :
    print(f'{num1} is an even number.')
else:
    print(f'{num1} is an  odd number.')

# Factorial Calculation

n = int(input("Enter a number: "))

result = 1

for i in range (1, n+1):
    result *= i

print(f' The factorial of {n} is {result}')

# Fibonacci Sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))

if n <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    fib_sequence = []
    a, b = 0, 1

    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

print(f'The first {n} Fibonacci numbers are: {fib_sequence}')

#Reverse a String

s = input("Enter a string: ")
reversed_str = ""
for i in s :
 reversed_str = i + reversed_str

print(f'The reversed string is: {reversed_str}')

#Palindrome Check

# Palindrome Check

def is_palindrome(s):

    s = s.replace(" ", "").lower()

    return s == s[::-1]

input_string = input("Enter a string: ")

result = is_palindrome(input_string)

print(f'Is the string a palindrome? {result}')


#Leap year check

year=int(input("Enter any year:"))
if year%4==0:
    print(f'{year} is leap year')
else:
    print(f'{year} is leap not a year')

#Armstrong Number

num=int(input("Enter a number:"))
org=num
s=0
while num>0:
    d=num%10
    s=s+(d**3)
    num=num//10

if org==s:
    print(f'{org} is amstrong number')
else:
    print(f'{org} is amstrong not number')