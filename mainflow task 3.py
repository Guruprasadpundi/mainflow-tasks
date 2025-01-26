# table of a number

n=int(input("Enter a number:"))

for i in range (1,11):
    print (f"{n} x {i} = {n * i} ")

# swap Two Number

a = int(input("Enter fast number:"))
b = int(input("Enter second number:"))

a = a + b
b = a - b
a = a - b 

print(f"swapped value: a = {a}, b = {b} ")

# check substring

a = input("Enter string:")
b = input("Enter substring:")

if b in a:
    print("True")
else:
    print("False")
    

# Decimal to Binary

n = int(input("Enter decimal number: "))

binary_conversion = bin(n)[2:]

print(f"The binary conversion of {n} is {binary_conversion}")


#matrix addition

matrix1 = [[int(input("Enter value for matrix1: ")) for j in range(3)] for i in range(3)]

matrix2 = [[int(input("Enter value for matrix2: ")) for j in range(3)] for i in range(3)]

def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[i]))] for i in range(len(matrix1))]
result = matrix_addition(matrix1, matrix2)

print("Resultant Matrix:")
for row in result:
    print(row)


#matrix multiplication

matrix1 = [[int(input("Enter value for matrix1: ")) for j in range(3)] for i in range(3)]
matrix2 = [[int(input("Enter value for matrix2: ")) for j in range(3)] for i in range(3)]

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Number of columns in A must equal the number of rows in B")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


result = matrix_multiply(matrix1, matrix2)

for row in result:
    print(row)


#second largest

list1 = []

user_input = input("Enter a list of integers separated by commas: ")

list1 = [int(x) for x in user_input.split(',')]


if len(set(list1)) < 2:
    raise ValueError("List must contain at least two distinct elements")


fmax = max(list1)


f = [x for x in list1 if x != fmax]


smax = max(f)
print(f'Second maximum value is {smax}')

#check Anagram

s1 = input("Enter a string:")
s2 = input("Enter a string:")

if(sorted(s1)== sorted(s2)):
    print(True)
else:
    print(False)