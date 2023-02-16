from CarFactory import *

print("Select type of car to construct: deportive or family:")
car_to_construct = input()
print("Insert a mark: examples: toyota, BMW, ford")
car_type = input()
print("Contruct a car type: ", car_to_construct, " mark: ", car_type)



car = Factory.get_car(car_to_construct, car_type)
