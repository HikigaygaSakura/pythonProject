name = 'freessd'
login_time = 3
cost = 14.734
print("Hello，" + name + ",you are already login ", login_time, "times", sep='')

# %格式化
print("Hello %s , you are already login %d times" % (name, login_time))
#变量很多就不是很好用，太乱了，且 %() 括号里的元组只支持string int，float，等基本类型，不支持字典
#下面是非要用 % 打印字典类型(说的就是你sst)

data = {'name': 'freessd', 'login_time': 3, 'cost': 3.0}
tuple_val = (data['name'], data['login_time'])
print("Hello %s , you are already login %d times" % tuple_val )

#str.format
print("Hello {}, you are already login {} times.You cost {:.2f}$.".format(name, login_time, cost))
print("Hello {}, you are already login {} times.You cost {:.2f}$.Welcome {} become VIP".format(name, login_time, cost, name))
print("Hello {0}, you are already login {1} times.You cost {2:.2f}$.Welcome {0} become VIP".format(name, login_time, cost))
#.format()可以不按顺序输出，%需要对应,在{}内启用标识符后，不需要再重复写实参，当然，也可以为了提高可读性使用以下写法
print("Helo {name}, you are already login {log} times.You cost {cost:.2f}$.Welcome {name} become VIP".format(name = name,log = login_time, cost = cost))

#输出字典
print("Hello {} , you are already login {} times.You cost {:.2f}".format(data['name'], data['login_time'], data['cost']) )

#但是万一字符串足够长了，.format()依旧太长了
