#f(x) = |x|
"""
x = int(input("please enter a number: "))

if x >= 0:
    y = x
else:
    y = -x

print(y)
"""
# 三目运算
"""
x=int(input("please enter a number: "))

y = x if x >= 0 else -x
print(y)
"""

#max/min
a=int(input("please enter a number: "))
b=int(input("please enter another number: "))
max = a if a >= b else b
print(max)
