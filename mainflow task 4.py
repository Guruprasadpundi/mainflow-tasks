#Find Missing Number

def find_missing_number(arr):
    n = len(arr) + 1
    hash_set = set(arr)

    for i in range(1, n):
        if i not in hash_set:
            return i

    return n

arr = [1, 2, 4, 6, 3, 7, 8]
missing_number = find_missing_number(arr)
print("Missing number is:", missing_number)

#Check Balanced Parentheses

def isbalanced(s):
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        else:
            if st and ((st[-1] == '(' and s[i] == ')') or
                       (st[-1] == '{' and s[i] == '}') or
                       (st[-1] == '[' and s[i] == ']')):
                st.pop()
            else:
                return False
    return not st

if __name__ == "__main__":
    s = "{([])}"
    if isbalanced(s):
        print("true")
    else:
        print("false")


#Longest Word in a Sentence

s = input ("Enter a string:")
words = s.split()
res = ""

for word in words:
    if len(word) > len(res):
        res = word 

print("the longest word is:", res)

#Count Words in a Sentence

s = input("Enter string:")

word_count = len(s.split())
print(word_count)

#Check Pythagorean Triplet

def is_pythagorean_triplet(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    return False

a = int(input("Enter first integer:"))
b = int(input("Enter second integer:"))
c = int(input("Enter third integer:"))

print(is_pythagorean_triplet(a, b, c)) 


#Bubble Sort

arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]: 
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array is:", arr)

#Binary Search


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1 
    return -1  

arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))


target = int(input("Enter target from list: "))

index = binary_search(arr, target)
print("Index of target:", index)


#Find Subarray with Given Sum

def find_subarray_with_sum(nums, target_sum):
    prefix_sums = {0: -1}
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num

        if current_sum - target_sum in prefix_sums:
            return prefix_sums[current_sum - target_sum] + 1, i

        prefix_sums[current_sum] = i

    return -1

nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
target_sum = int(input("Enter target from list: "))
result = find_subarray_with_sum(nums, target_sum)

if result != -1:
    print(f"Subarray found between indices {result[0]} and {result[1]}")
else:
    print("No such subarray exists")
