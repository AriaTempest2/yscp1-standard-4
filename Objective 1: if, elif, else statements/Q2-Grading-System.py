'''
Question 2: Grading System
Description: Write a program that takes a student's score as input and assigns a grade based on the following criteria:

90 or above: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"
'''

# This program will assign grades based on the score

score = float(input("Enter the student's score: "))

# Complete the if-elif-else logic to assign grades

if score >= 90 and not score > 100:
    print("A")
elif score >= 80 and not score > 90:
    print("B")
elif score >= 70 and not score > 80:
    print("C")
elif score >= 60 and not score > 70:
    print("D")
elif score > 100:
    print("Liar!")
else:
    print("F")