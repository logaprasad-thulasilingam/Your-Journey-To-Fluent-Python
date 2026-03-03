# class Vehicle:
#     def __init__(self, wheels, color):
#         self.wheels = wheels
#         self.color = color
# class Car(Vehicle):
#     def __init__(self, wheels, color, gears):
#         super().__init__(wheels, color)
#         self.gears = gears
#     def gear_info(self):
#         return (f"{self.color} Car has {self.gears} gears")
#
# honda = Vehicle(wheels=2, color="White")
# honda_car = Car(wheels=4, color="Black", gears= 6)
# print(honda.color, honda.wheels)
# print(honda_car.color, honda_car.wheels)
# print (honda_car.gear_info())


class Vehicle:
    def __init__(self):
        self.wheels = 2
        self.color = "Black"
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = 4

bike = Vehicle()
car = Car()

print (bike.color , bike.wheels)
print (car.color, car.wheels)