"""
文件读写和异常处理机制
- 文件打开
- 文件读写
- 异常处理机制
"""

# 文件读写
# file = open('test.txt','r', encoding='utf-8')
# print(file.read())
# file.close()

# file = open('test.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line, end = '')

# file = open('test.txt', 'r', encoding='utf-8')
# lines = file.readlines()
# for line in lines:
#     print(line, end = '')

# file = open('致橡树.txt', 'a', encoding='utf-8')
# file.write('\n标题：《致橡树》')
# file.write('\n作者：舒婷')
# file.write('\n时间：1977年3月')
# file.close()

# 异常处理机制
file = None
try:
    file = open('test.txt','r',encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')

except LookupError:
    print('指定了未知的编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误！')
finally:
    if file:
        file.close()

print(BaseException.__dict__)
print(BaseException.__doc__)
print(BaseException.__module__)
print(dir(BaseException))

## raise
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("除数不能为 0")
    return x / y

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print("出错啦：", e)

## 异常
class InputError(ValueError):
    """自定义异常类型"""
    pass
def fac(num):
    if num < 0:
        raise InputError("输入的数字不能为负数")
    if num in (0,1):
        return 1
    return num * fac(num - 1)

## 上下文
try:
    with open('test.txt','r',encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')  

## 二进制文件
try:
    with open('guido.jpg','rb') as file1:
        data = file1.read()
    with open('guido_copy.jpg','wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('无法打开指定的文件！')

# 基本文件操作
import os
print(os.name)
print(os.linesep)
print(os.sep)
print(os.getcwd())

## 绝对路径
print(os.path.abspath('test.txt'))

## 遍历目录
tuples = os.walk('/Users/qiaowu/Desktop/PythonNewLearn/')
for tuple in tuples:
    print(tuple,"\n")

## 删除目录文件
# import os
# path = ""
# if os.exit(path):
#     os.remove(path)
# else:
#     print("文件不存在")

## 文件基本信息
import os
print(os.stat('ReadMe.md'))

# 异常处理及程序调试
# def division():
#     num1 = int(input("请输入第一个数字："))
#     num2 = int(input("请输入第二个数字："))
#     result = num1 / num2
#     print("结果是：", result)
# if __name__ == "__main__":
#     division()