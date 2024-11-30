for i in range(1,10):
    if i == 5:
        break
    for j in range(1,i+1):
        print(j,"x",i,"=",j*i,end="  ")
    print()

#break 退出只看位置，只跳本层循环