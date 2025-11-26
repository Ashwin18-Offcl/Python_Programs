"""Class inheritance 
Given:
Create a Bus class that ingerits from the vehicle class. Given the capacity argument of Bus.seating-capacity()
a default value of 50.
Use the following code for your parent vehicle class."""
class Vehicle:
    def _init_(self, name, max_speed, mileage):
    self.name = 
    self.max_speed = maxs_speed
    self.mileage = mileage
    
    def sitting_capacity(self,capacity):
        return f"sitting capacity of bus {self.name} is {capacity} passanger"
    
    class Bus(Vehicle):
        #assign default value to capacity 50
        def sitting_capacity(self,capacity=50):
            return super().sitting_capacity(capacity=50)
        School_bus=Bus("Volvo",120,23)
        School_bus.sitting_capacity()
        