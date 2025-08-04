# Question 1 : 
#1. Even or Odd Checker
# Write a function called check_even_odd(num) that:
# Takes an integer as input.
# Prints "Even" if the number is even, otherwise prints "Odd".

# def check_even_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# print(check_even_odd(4))    

# question2 
# 2. Grade Calculator
# Create a function calculate_grade(score) that:
# Accepts a number from 0 to 100.
# Uses if-else statements to return a letter grade:
# A: 90–100
# B: 80–89
# C: 70–79
# D: 60–69
# F: below 60

# def calculate_grade(score):
#     if score>=90 and score<=100:
#         return "A"
#     elif score>=80 and score<=89:
#         return "B"
#     elif score>=70 and score<=79:
#         return "C"
#     elif score>=60 and score<=69:
#         return "D"
#     elif score<60 and score>=0:
#         return "F"
#     else:
#         return "Invalid number"
# print(calculate_grade(0))    

# 3. Maximum of Three Numbers
# Write a function find_max(a, b, c) that:
# Takes three numbers as arguments.
# Returns the largest among them using if-else (don’t use max()).
# def find_max(a, b, c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(find_max(23,24 ,56 )) 
# print(find_max(23,-34 ,0 ))   
# print(find_max(20,20 ,20 ))
# print(find_max(-1,-10000 ,-56 ))

# 4. Leap Year Checker
# Create a function is_leap_year(year) that:
# Returns True if the year is a leap year, else False.
# (Hint: A year is a leap year if it's divisible by 4, not divisible by 100 unless divisible by 400.)
# def is_leap_year(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         return True
#     else:
#         return False
# print(is_leap_year(2018))
# print(is_leap_year(2016))

# 5. Positive, Negative, or Zero
# Write a function check_sign(num) that:
# Prints "Positive" if the number is > 0,
# "Negative" if < 0,
# "Zero" if == 0.

def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_sign(56))
print(check_sign(0))
print(check_sign(-56))
