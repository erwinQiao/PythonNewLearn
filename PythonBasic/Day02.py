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
#print(01032) 

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
name = input("Please input your name:")
print(f"hell,{name}, would you like to learn some Python today?")
print(name.upper())
print(name.title())
print(name.lower())

text_name = 'python_notes.txt'
print(text_name.removesuffix('.txt'))


