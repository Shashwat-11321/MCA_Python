# Question3 : Python Control Statements (20 Marks)
# You are given a list of integers:
    
# numbers = [12, 7, 19, 24, 5, 17, 28, 13]
# Perform the following tasks using control statements in Python:

# Q1 Even or Odd (5 Marks)
# Write a Python function that iterates through the list and prints whether each number is even or odd.

# Q2 Sum of Numbers (5 Marks)
# Using a while loop, write a Python program that calculates and prints the sum of all numbers in the list.

# Q3 Maximum and Minimum (5 Marks)
# Write a Python function find_max_min(numbers) that uses if-else statements to find and return the maximum and minimum numbers from the list.

# Q4 Prime Numbers (5 Marks)
# Write a Python function find_primes(numbers) that uses a nested for loop and if-else statements to find and return a list of prime numbers from the given list.

numbers = [12, 7, 19, 24, 5, 17, 28, 13]
for num in numbers:
    if ( num % 2 == 0):
        print("the even number is :",num)
    else:
        print("The odd number is :",num)
try:
    sum = 0
    i = 0
    while i < len(numbers):
        sum+=numbers[i]
        i+1
    print("Sum of number is =",sum)

except:
    print("error in this block")

max=numbers[0]
min=numbers[0]

for num in numbers:
    if (num > max):
        max=num
    elif(num<min):
        min=num

print(f"min={min}")
print(f"max={max}")



