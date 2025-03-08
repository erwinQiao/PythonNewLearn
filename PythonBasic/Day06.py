"""
IF语句的学习
- 条件测试
- if语句
- if-else语句
"""

# 简单示例
cars = ['audi','bmw','subaru','toyota']
for item in cars:
    if item =='bmw':
        print(item.upper())
    else:
        print(item.title())

## 字符串比较，数值比较
requested_topping = 'mushrooms'
if requested_topping!='anchovies':
    print("Hold the anchovies!")

answer = 17
if answer !=42:
    print("That is not the correct answer. Please try again!")

## 检查多个条件