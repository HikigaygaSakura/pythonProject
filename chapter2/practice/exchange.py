exchange_rate = 7.25

# CNY -> USD
'''
CNY = float(input("请输入人民币金额："))
USD = CNY / exchange_rate
print(f"对应美元金额为：{USD:.2f}") #字符串化处理，保留两位小数
'''

#USD ->CNY
USD = float(input("请输入美元金额："))
CNY = USD * exchange_rate
print(f"对应的人民币金额为：{CNY:.2f}") #字符串化处理，保留两位小数 我个人觉得汇率这块不太需要