"""
Day04 主要是列表的使用
1. 列表
2. 列表的方法: 添加，删除，排序，长度等
3. 列表进阶：切片，遍历，列表生成式

"""
# 列表
print(list(range(1,5)))
bicyles = ['trek','cannondale','redline','specialized']
print(type(bicyles))
print(bicyles)

## 访问列表元素
print(bicyles[0])
print(bicyles[0].title())
print(bicyles[-1])

## 修改、添加和删除元素
motorcycles = ['honda','yamaba','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

pop_name = motorcycles.pop()
print(pop_name)
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

## Test
guest = ['zhangsan','lisi','erwin','qiao']
print(guest)

guest.insert(4,'zhang')
print(guest)

print(f'welcome t my dinner {guest}')
for name in guest:
    print(f"welcome to my dinner {name}")

print(f"{guest[0]} can't come to my dinner")
guest[0] = 'wangwu'
print(f"welcome to my dinner {guest}")

print(guest)
guest.insert(round(len(guest)/2),'liu')

guest.append('zhangliu')
print(guest)

guest.pop()
print(guest)

# 管理列表
cars = ['bmw','audi','toyota','subaru']
print(cars)
#cars.sort()
print(cars)
print(sorted(cars))
print(len(cars))

# 操作列表
## for 循环
magicians = ['alice','david','carolina']
for item in magicians:
    print(item)

## 创建数值列表
for value in range(1,5):
    print(value)

numbers = list(range(1,5))
print(numbers)

suqares = []
for value in range(1,11):
    suqare = value ** 2
    suqares.append(suqare)
print(suqares)

suqares = []
for value in range(1,11):
    suqares.append(value **2)
print(suqares)

## 对数值列表执行简单的统计运算
min(suqares)
max(suqares)
sum(suqares)

## 列表推导式
squares = [value**2 for value in range(1,10)]
print(squares)

## Test
numer = list(range(1,21))
print(numer)

# num2 = list(range(1,1_000_001))
# #print(num2)
# for item in num2:
#     print(item)

num3 = list(range(1,1_000_001))
print(min(num3))
print(max(num3))
print(sum((num3)))

print(list(range(1,20,2)))
num = [value for value in range(3,31) if value %3 ==0]
print(num)

num4 = [value **3 for value in range(1,11)]
print(num4)

players = ['charles','martine','michael','florence','eli']
print(players[:4])
for item in players[:3]:
    print(item.title())

## 复制列表
my_foods = ['pizza','falafel','carrot','cake']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('ice cream')
friend_foods.append('cannoli')
print(friend_foods,my_foods)

words = "Three items from the middle of the list are:"
print(words[-3:])

## 序列相加
num = [1,2,3,4,5,6]
nba = ['Janmes','jordan','kobe','wade']
print(num + nba)

## 乘法
phone = ['iphone','vivo','huawei']
print(phone*3)
print([None]*5)

## 检查某个元素in
print('iphone' in phone)

## 最大最小值
print(max(phone))
print(min(phone))