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
age_0 = 22
age_1 = 18
print(age_0 >=21 and age_1>=21)

banned_users = ['andrew','carolina','david']
user  = 'marie'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish")

