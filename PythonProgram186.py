""" Convert the following JSON into Vehicle Object
{"name": "Toyota Rav4", "engine":"2.5L","price":32000}"""
""" For example, we should be able to access Vehicle Object using the dot operator like this.
vehicleObj.name,vehicleObjengine,vehicleObj.price"""
import json
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine= engine
        self.price = price
def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])
vehcleObj = json.loads('{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}',object_hook=vehicleDecoder)
print("Type of decoded object from JSON Data")
print(type(vehcleObj))
print("Vehicle Details")
print(vehicleObj.name VehicleObj.engine, vehicleObj.price)