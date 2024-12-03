name = 'freessd'
login_time = 3
cost = 14.734

#使用f-string 格式化 格式：在字符串前加f/F，在中间用{}显示替换，{}中可以直接使用变量名称来标识
print(f"Hello {name}, you are already login {login_time} times.You cost {cost:.2f}$.Welcome {name} become VIP")
