'''
Question 3: Nested Age Check
Description: Write a program that checks a person’s age and prints a message. The program should have the following logic:

If the person is below 13, print "Child".
If the person is between 13 and 19, print "Teenager".
If the person is between 20 and 64, print "Adult".
If the person is 65 or older, print "Senior".
If the person’s age is 18 or 21, print "Young Adult".
'''

# This program will check age categories

age = int(input("Enter your age: "))


# Add if-elif-else logic here with nested conditions
if age <= 13:
    print("Child")
elif age == 18 or age == 21:
    print("Young Adult")
elif age >= 13 and not age == 18 and not age > 19:
    print("Teenager")
elif age >= 20 and not age > 64:
    print("Adult")
elif age >= 65 and not age > 14000000000:
    print("Senior")
else:
    print("Hi Mr. Wells")