"""
函数
1. 定义函数
2.函数传递信息，位置参数
3.函数处理字典、列表
4. 装饰器
"""
# 函数结构
def greet_user():
    # 打印出“Hello!”
    print('Hello!')
greet_user()

## 向函数传递信息
def greet_users (username):
    """
    输入名字
    """
    print(f"Hello, {username.title()}!")
greet_users('qiao')

## 位置实参
def describe_pet(animal_type, pet_name):
    """
    显示宠物的信息
    """
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type} is name is {pet_name.title()}")

describe_pet(animal_type='boy', pet_name='erwin')

## 默认值
def describe_pet(pet_name, animal_type = 'dog'):
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type} is name is {pet_name.title()}")

describe_pet('erwin')
describe_pet(pet_name="erwin",animal_type='cat')

## 返回值
def add_unmbers(a,b):
    print(a+b)
add_unmbers(1,2)

def get_formatted_name(first_name,last_name):
    """
    返回标准格式的姓名
    """
    full_name = f"{first_name}{last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

## 让实参变成可选的
def get_formated_name(first_name, middle_name, last_name):
    """
    return stand name
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musican = get_formated_name('jimi','lee','hendrix')
print(musican)

def get_formatted_name(first_name, last_name, middle_name=''):
    """
    return stand name
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musican = get_formatted_name('jimi','lee',)
print(musican)

## 返回字典
def build_person(first_name, last_name):
    person = {'first':first_name, 'last':last_name}
    return person

musican = build_person('jimi','hendrix')
print(musican)

def build_person(first_name, last_name, age = None):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musican = build_person('jimi','hendrix',age=27)
print(musican)

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     l_name = input("Last name:")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")
#     break

## 传递列表
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

## 函数处理列表
def print_modles(unpriented_designs,completed_models):
    while unpriented_designs:
        current_design = unpriented_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

## 传递任意数量的实参
def make_pizza (*toppins):
    print(toppins)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    return f"Making a pizza with the following toppings: {toppings}"

toppings = make_pizza("apple")
print(toppings)

def make_pizza(*toppings):
    print(f"Making a pizza with the following toppings: {toppings}")
    for topping in toppings:
        print(f"- {topping}")

## 结合使用位置实参和任意数量的实参
def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

## 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#import Pythonfile.pizza as pizza
#pizza.make_pizza(17, 'mushrooms', 'green peppers', 'extra cheese')

#from Pythonfile.pizza import make_pizza as mp
#mp(17, 'mushrooms', 'green peppers', 'extra cheese')

## 模块as alias
#import Pythonfile.pizza as p
#p.make_pizza(17, 'mushrooms', 'green peppers', 'extra cheese')

# 函数补充
## 基础if函数
def fun_bmi (person,height,weight):
    """功能：根据身高和体重计算BMI指数
    person:姓名
    height:身高，单位：米
    weight:体重，单位：千克
    """
    print(person + "的身高:" +str(height) + "米 \t 体重："
          + str(weight) + "千克")
    # 用于计算BMI指数
    bmi = weight / (height * height)
    print("BMI指数为：" + str(bmi))
    if bmi < 18.5:
        print("体重过轻")
    if 18.5 <= bmi < 24.9:  # 18.5 <= bmi < 24.9
        print("正常范围，注意保持")
    if 24.9 <= bmi < 29.9:
        print("体重过重")
    if bmi >= 29.9:
        print("肥胖")

fun_bmi("小明",1.75,70)

x = []
y = [[1,2,3],[4,5,6],[7,8,9]]
x.append([row[i] for row in y for i in range(3)])
print(x)

## pass语句
def func():
    pass

## 参数传递 值传递
def modify (x):
    print("函数内部修改前：",x)
    x +=10
    print("函数内部修改后：",x)

a = 5
modify(a)
print("函数外部修改后：",a)
print(modify(a))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

## 引用传递
def modifty(list):
    print("函数内部修改前：",list)
    list.append(10)
    print("函数内部修改后：",list)

a = [1,2,3]
modifty(a)
print("函数外部修改后：",a)

## 参数默认值
def demo(obj = []):
    print("obj的值:",obj)
    obj.append(1)
    return obj

print(demo())
print(demo())
print(demo())

## 可变参数
def printplayer(*name):
    print("\n My favorite player is:")
    for item in name:
        print(item)

param = ['james','harden','curry']
printplayer(*param)

def printsign(**sign):
    print()
    for key,value in sign.items():
        print(key + " : " + value)

## 返回值
def fun_checkout(name):
    nickName = ""
    if name == "james":
        nickName = "king"
    elif name == "harden":
        nickName = "brother"
    else:
        nickName = "unknown"
    return nickName

print(fun_checkout("james"))

## 局部变量
def f_demo():
    message = "anvc"
    print('局部变量：',message)

f_demo()
print(f_demo())
# print('全局变量：',message)

## 全局变量
message = "anvc"
print("函数外 message= ",message)
def f_demo():
    message = 'sfadf'
    print("函数内 message= ",message)
f_demo()
print("函数外 message= ",message)

message ="anvc"
print("函数外 message= ",message)
def f_demo():
    global message
    message = 'sfadf'
    print("函数内 message= ",message)

f_demo()
print("函数外 message= ",message)

# 装饰器的使用
## 装饰器的基础
import time

def record_time(func):
    """
    定义一个装饰功能
    因为不知道被装饰的函数有怎么养的参数，所以使用*args和**kwargs
    Python中函数可以嵌套的定义
    """
    def wrapper(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()
        print("函数执行时间：", end - start)
        return result
    return wrapper

import random
@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')

download('Python基础教程')

import random
import time
from functools import wraps

## warp装饰器
def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}执行时间:{end - start:.2f}秒")
        return result
    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')
download('Python基础教程.pdf')

## 取消装饰器
download.__wrapped__('Python基础教程.pdf')

# 递归调用
def fac(num):
    if num in (0,1):
        return 1
    return num * fac(num - 1)

print(fac(500))

# 装饰器
import random
import time

from functools import wraps

def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}执行时间:{end - start:.2f}秒")
        return result
    return wrapper
@record_time
def downliad(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')
@record_time
def  upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}上传完成.')

downliad('Python基础教程.pdf')
upload('Python基础教程.pdf')

## 取消装饰器
download.__wrapped__('Python基础教程.pdf')

## 打印对象
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
    
    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}')
    
    def play(self):
        """玩"""
        print(f'{self.name}正在玩')
    def __repr__(self):
        return f'{self.name}:{self.age}'

stu1 = Student('小明', 20)
print(stu1)

# 定义时钟
import time
class Clock(object):
    """数字时钟"""
    def __init__(self, hour = 0, minute = 0, sec = 0):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def run(self):
        """ 走字"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour +=1
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        """显示时间"""
        print(f"{self.hour:0>2d}:{self.minute:0>2d}:{self.sec:0>2d}")
clock = Clock(23, 59, 58)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()

## 属性限制
class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'

