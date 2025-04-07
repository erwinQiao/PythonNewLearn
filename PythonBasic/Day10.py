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

my_dog = Dog('Willie',6)
print(f"My dog name is {my_dog.name}") 
print(f"My dog age is {my_dog.age}")
## 调用方法
my_dog.sit()
my_dog.roll_over()
print(Dog.__dict__)

class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(f"The restaurant name is {self.restaurant_name}")
		print(f"The cuisine type is {self.cuisine_type}")

	def open_restaurant(self):
		print(f"The restaurant is open.")

## 使用类和实例
class Car:
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())

## 补充属性
class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a4',2024)    
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print(f"This car has {self.odometer_reading} miles on it.")
	
	def update_odometer(self,mileage):
		self.odometer_reading = mileage

my_new_car = Car('audi','a4',2024)
my_new_car.update_odometer(50)
my_new_car.read_odometer()

## 方法让属性值递增
def update_odometer(self,mileage):
	if mileage >= self.odometer_reading:
		self.odometer_reading = mileage
	else:
		print("You can't roll back an odometer!")
def update_odometer(self,mileage):
	self.odometer_reading += mileage

list = ['apple','banana','orange','pear','watermelon','grape']
result = [i for i in list if len(i) > 5]
print(*result)

# 子类
## 继承
class Car:
	"""一次模拟汽车的简单尝试"""
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print(f"This car has {self.odometer_reading} miles on it.")
	
	def update_odometer(self,mileage):
		"""将里程表读数设置为指定的值"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles

class ElectriCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)

my_leaf = ElectriCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())

## 给子类定义属性和方法
class ElectriCar(Car):
	"""电动车的独特之处"""
	def __init__(self, make, model, year):
		"""
		先初始化父类的属性，再初始化电动车特有的属性
		"""
		super().__init__(make,model,year)
		self.battery_size = 50

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print(f" This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectriCar('tesla','model s',2024)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

## 重写父类的方法
class ElectriCar(Car):
	def fill_gas_tank(self):
		"""电动车没有油箱"""
		print("This car doesn't need a gas tank!")

## 组合
class Battery:
	"""一次模拟电动汽车电瓶的简单尝试"""
	def __init__(self, battery_size=75):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size
	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print(f"This car has a {self.battery_size}-kWh battery.")
	
class ElectriCar(Car):
	def __init__(self, make, model, year):
		"""电动汽车的独特之处"""
		super().__init__(make, model, year)
		self.battery = Battery()
my_leaf = ElectriCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

## 类的定义和使用
class Geese:
	"""大雁类"""
	pass

wildGoose = Geese()
print(wildGoose)

class Geese:
	'''大雁类'''
	def __init__(self):
		print('大雁类被创建了')
wildGoose = Geese()
print(wildGoose)

## init参数
class Geese:
	'''大雁类'''
	def __init__(self, beak, wing, claw):
		print('大雁类被创建了')
		print(beak)
		print(wing)
		print(claw)
beak1 = '长'
wing1 = '大'
claw1 = '强健'
wildGoose = Geese(beak1,wing1,claw1)
print(wildGoose)

