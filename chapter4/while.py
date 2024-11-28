# i =0
# while i<10:
#     print(i)
#     i+=1

#sum 1-100
# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
# print(sum)

# while 嵌套
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