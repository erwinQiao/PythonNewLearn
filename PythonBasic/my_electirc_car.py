from car import ElectriCar
my_leaf = ElectriCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
#my_leaf.battery.get_range()

from car import Car,ElectriCar
my_car = Car('audi','a4',2024)
print(my_car.get_descriptive_name())

import car
my_mustang = car.Car('ford','mustang',2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectriCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())