# join()
list_val = ['www','freessd','com']
str_val = ".".join(list_val)
print(str_val)

tuple = ('users','ssd','code')
str_val1 = '/'.join(tuple)
print(str_val1)

#大小写转换
str ="free ssd"
#upper()  全大写
print(str.upper())

#lower() 全小写
print(str.lower())

#tittle() 每个单词首字母大写
print(str.title())

#capitalize() 第一个字母大写
print(str.capitalize())

#swapcase() 大小写转换
print(str.swapcase())

#检索
#count()
print(str.count('e')) #计数字符串中e的个数,开始位置和结束位置可以省略

#find()
print(str.find('e')) #找到字符串中需要被检索的内容，如果有，返回索引，没有返回-1 (顺带一提，如果存在多个相同内容，找到第一个就返回了)

#index()
#基本与find一样，但找不到会返回一个error，而不是-1

#startswith()
print(str.startswith('e')) #查找字符串是否以某一个字符作为开头，找到了返回True，没有就False

#endswith()
#这个是找末尾，基本同stratswitch()

#切片
#split()
print(str.split()) #按照指定字符分割，若无指定，按空格分，分割次数可省略不写，默认有多少空格或者空格字符或者指定字符，切多少份(只要有就切）

#splitlines()
#使用行界定符分割，其余与split()一样

#partition()
print(str.partition('e')) #按照指定的字符将整段切成指定字符前，指定字符，与指定字符后三个元组，若有两个相同的且并排的指定字符，只切第一个


#修剪
#strip()
print(str.strip('f')) #移除头尾指定的字符，默认是空格或者换行，中间的删不了

#lstrip() and rstrip() 一个从左边剪，另一个从右边剪