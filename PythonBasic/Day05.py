'''
元组
- 元组的不可变性
- 元组的访问，切片等
- 元组变量的替换
'''
# 元组
dimensions = (200,100)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 230

## 遍历元组
for item in dimensions:
    print(item)

## 修改元组变量
dimensions = (400,100)
dimensions = ('a','c','f','B')
#dimensions.sort()
print(dimensions)

# 元组特例
team = "Lakers","Sun","Rockets"
print(type(team))

team = ("Lakers")
print(type(team))

team1 = ("Lakers",)
print(type(team1))

team =()
tuple(range(10))

## 元组的连接
team = ("Lakers","Sun","Rockets")
team1 = ("Cavaliers","Warriors")
team2 = team + team1
print(team2)
