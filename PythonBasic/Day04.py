"""
Day04 主要是列表的使用
1. 列表
2. 列表的方法
3. 列表进阶

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

