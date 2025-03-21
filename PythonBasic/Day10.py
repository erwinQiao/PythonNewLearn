'''
类的使用
- 创建类
- 创建对象
- 访问属性
- 访问方法
- 继承
- 多态
'''

# 创建类
## 创建Dog类
class Dog:
	"""一次模拟小狗的简单尝试"""
	def __init__(self, name, age):
		"""初始化属性 name 和 age"""
		self.name = name
		self.age = age
	def sit(self):
		"""模拟小狗收到命名时坐下"""
		print(f"{self.name} is now sitting.")
	def roll_over(self):
		"""模拟小狗收到命名时打滚"""
		print(f"{self.name} roll_over!")

