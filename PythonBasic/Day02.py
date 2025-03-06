"""
1. 保留字和标识符
2. 数据类型
3. 字符串的常用操作
"""
# _*_ coding:utf-8 _*_

# 保留字
import keyword
print(keyword.kwlist)

#if= "I'm strong"
# print(if)

# 标识符 各种变量的名称
name = "Tom"
print(type(name))

no = number = 2048
print(id(no))
print(id(number))

# 基本数据类型
## 数值类型
print(0x1032) 

# 字符串的常用操作
## 拼接字符串
a = 'erwin'
b = 'Qiao'
c = 123
print(a+b)
print(a +' '+ b + str(c))

first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name}{last_name}"
print(full_name)
full_name = first_name+last_name
print(full_name)

print(f"Hello,{full_name.title()}!")

## 字符串长度
string = "人生苦短，要学python！"
print(len(string))
print(len(string.encode())) # 计算UTF-8
print(len(string.encode('gbk')))

## 截取字符串
str1 = '人生苦短，我用python！'
print(str1[2:8:2])
try:
    substr1 = str1[15]
except IndexError:
    print('指定索引不存在')

## 使用制表符和换行符来添加空白
print("\t Python")
print("Languages:\nPython c \nJava")
print("Languages:\n\tPython\n\tC")

## 删除空白
favoreite_language = '\tpython abc'
print(favoreite_language)
print(favoreite_language.lstrip())
print(favoreite_language.strip())

## 删除前缀
nostarch_url = 'https://www.nostarch.com'
print(nostarch_url.removeprefix('https://'))

## test
# name = input("Please input your name:")
# print(f"hell,{name}, would you like to learn some Python today?")
# print(name.upper())
# print(name.title())
# print(name.lower())

text_name = 'python_notes.txt'
print(text_name.removesuffix('.txt'))

## 分割字符串
str = "你 有 多 自   信, \n世界 就 有 多 相信你～"
print(str.split())
print(str.split(sep = " "))
print(str.split(" ",maxsplit=5))

str1 = "@明日科技 @扎克伯格 @乔 @erwin"
list1 = str1.split()
print(list1)
for item in list1:
    print(item[1:])
    print(type(item))

## 合并字符串
list1 = ['明日科技','erwin','Qiao','python']
item1 = ""
for item in list1:
    item1 = item + "@"
print(item1)
print("@".join(list1))

## 检索字符串
str1 = "@qiao @erwin @zhang"
print('字符串',str,'字符串中@个数',str1.count('@',2,10))
print(str1.find('@',2))

print(str1.index('@',2))
print(str1.startswith('*'))

## 删除字符串中的特殊字符
str1 = " @ https://www.minger.com \t\n\r"
print(str1)
print(str1.strip(' @'))

# 高级字符串内置函数
## eval函数
print(eval('3+4'))
n =2
print(eval("n+2"))
# str = input("Please input a expression: ")
# print(eval(str))
i = 0
list1 = []
while i<10:
    list1.append(eval("pow (i,3)"))
    i+=1
print(list1)

a = "[1,2,3,4]"
print(a)
print("转换后的类型",type(eval(a)))

## exec函数
code="""
import random
i = 0
list1 =[]
while i <10:
    list1.append(random.randint(0,100))
    i+=1
print(list1)
"""
exec(code)

## ascii函数
print(ascii(67))
print(ascii('a'))
print (ascii('中'))
print(ascii("\b31"))

## complie函数
code ="""
for i in range(10):
    if i %2 ==0:
        print(i,end="")
"""
byteExec = compile(code,'','exec')
exec(byteExec)