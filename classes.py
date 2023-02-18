#syntax for creating a class
#class <ClassName>
class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        return self.length * self.breadth

#create an object
study_room = Room()

#access class variables
study_room.length = 10.0
study_room.breadth = 15.0

#access class method
print(study_room.calculate_area())

#constructor syntax
#def __init__(self, [attributes...])

class Bike:
    name = ""

    def __init__(self, name=""):
        self.name = name

bike = Bike()
print(bike.name) #empty value

bike1 = Bike("Mountain Bike")
print(bike1.name) #Mountain Bike