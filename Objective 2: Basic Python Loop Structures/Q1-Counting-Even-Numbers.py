'''
Question 1: Counting Even Numbers

Description: Write a program that counts how many even numbers there are in a list of numbers (from 1 to 20).
'''

# This program will count even numbers in a list
numbers = list(range(1, 21))
even_count = 0





# Loop through the numbers and check for even numbers
for numbers in range(1, 21):
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    if numbers not in odd: 
        even_count = even_count + 1

print(f"There are {even_count} Even numbers")