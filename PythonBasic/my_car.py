from car import Car

my_car = Car('audi','a4',2024)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 23
my_car.read_odometer()