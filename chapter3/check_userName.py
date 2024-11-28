userName = input("Please enter your username(3-50 words): ")

#len(userName) 获取用户名长度
if len(userName) <3:
    print("Please retype your username(must over 3 words).")
elif len(userName) > 50:
    print("Please retype your username(don't over 50 words).")
else:
    print("Your username is valid.")