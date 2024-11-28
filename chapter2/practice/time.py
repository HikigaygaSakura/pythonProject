second = int(input("请输入秒数："))

theSecond = second % 60
minute = second // 60
theHours = minute // 60
theMinute = minute % 60
print("转换的时间为：",theHours,"小时", theMinute,"分钟", theSecond,"秒")