# 简单的输出

print('ssd')

# 输出变量

price = 10
number = 100
print(price)
print(number)
print(price,number)
print('总计花费',price*number)

#sep 分隔符
print('hello','world')
print('hello','world',sep=',')
print('2024','11','26',sep='-')
print('freessd','outlook.com',sep='@')

#end 结束符
print('hello')
print('world')
print('hello',end='\n')
print('world')

#file
file_source = open('Text.txt','w')
print('freessd','outlook.com',sep = '@',file = file_source)
file_source.close()