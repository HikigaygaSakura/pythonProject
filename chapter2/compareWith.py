"""
a = 2
b = 67
print(a > b)
"""

# 判断成绩
"""
grade = float(input("Enter grade: "))

if grade >= 60:
    print("Pass")
else :
    print("Fail")
"""

# 判断数字
import random
numbers =random.randint(0,9)
num = int(input("Enter a number from 0-9: "))

if num == numbers:
    print("Correct")
else:
    print("Incorrect","This number is",numbers)