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

## 使用多个elif代码块
age = 12
if age <4:
    price = 0
elif age <18:
    price = 25
elif age<65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price }")

## Test
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print("You get 5 points!")

if 'green' in alien_color:
    print("You get 5 points!")
else:
    print("You get 10 points!")

## if list使用
requested_topping = ["nushrooms","green peppers","extra cheese"]
for reqyested_topping in requested_topping:
    if reqyested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {reqyested_topping}.")
print("\nFinished making your pizza!")

## 空列表
requested_toppings = []
if requested_toppings:
    for requseted_topping in requested_toppings:
        print("Adding "+requseted_topping+".")
else:
    print("Are you sure you want a plain pizza?")

## Test
current_users = ['a','b','c','d','e']
new_users = ['d','e','f','g','h']
for name in new_users:
    if name in current_users:
        print(f"{name} is not avaiable")
    else:
        print(f"{name} is not used")

number = list(range(1,10))
for num in number:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

# 顺序语句结构
## 字符串分解赋值
a,b,c,d = 'xymn'
print(a,b,c,d)
print(a)