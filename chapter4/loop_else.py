# while-else

# i = 1
# while i <= 6:
#     if i == 4:
#         break
#     print(i)
#     i+=1
# else:
#     print("Finish")

"""
在不遇到break的情况下，while-else的else部分依旧会被执行,if-else 同样
使用场景：遍历所有条件之后依旧找不到目标值，或者抛出一个错误
"""

#for-else
for i in range(10):
    print(i)
else:
    print("Finish")