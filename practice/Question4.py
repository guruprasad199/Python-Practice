# Vehicle class
# 1. Create a Vehicle class with max_speed and mileage instance attributes 2. Create child class Bus and Taxi that will inherit all of the variables and methods of the Vehicle class 3. Create 2 methods fare and seating_capacity
# 4. You need to override the fare() and seating_capacity method of a Vehicle class in Bus and Taxi class.




# class Vehicle:
#     def __init__(self,name,  max_speed, mileage):
#         self.name = name

#         self.max_speed = max_speed
#         self.mileage = mileage

# modelX = Vehicle("my vehicle", 240, 18)
# print(modelX.max_speed, modelX.mileage)


# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 180, 12)
# print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)


# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         pass

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)

# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.seating_capacity())



class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

BMW = Vehicle("my vehicle", 1000, 200)
print( BMW.mileage , BMW.capacity)


class Bus(Vehicle):

    def fare(self):
        return super().fare() + self.capacity * 10


School_bus = Bus("School bus", 20, 80)
print(f"Total {School_bus.name} fare is:", School_bus.fare())