""" Create a Vehicle class without any variable and methods"""
class vehicle:
    def_init_(self,max_speed,mileage):
    self.max_speed = max_speed
    self.mileage = mileage
class Bus(Vehicle):
    pass
School_bus=Bus(70,10)
print(School_bus.max_speed,School_bus.mileage)
