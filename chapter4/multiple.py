# while 嵌套
#乘法表 for while
"""
i=1
while i<10:
    j=1
    while j<=i:
        print(j,"x",i,"=",j*i,end='  ')
        #列数+1
        j+=1
    print('\n')
    # 行数+1
    i+=1
"""
#乘法表  for “for”
for  i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",j*i,end='  ')
    print('\n')
