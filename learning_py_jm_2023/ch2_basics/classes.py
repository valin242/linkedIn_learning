#
# Example file for working with Classes
# LinkedIn Learning Python course by Joe Marini

class Vehicle():
    def __init__(self, bodystyle): # __init__ func that py calls when the object has been created and its time to initialize the object data
        self.bodystyle = bodystyle # defined a property on the class that'll hold the val that was passed in
    
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car") # initialize the super class (vehicle class) that we passed in and initialize it with the bodystyle "Car"
        self.wheels = 4
        self.doors = 4
        self.engintype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engintype, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle") # initialize the super class (vehicle class) that we passed in and initialize it with the bodystyle "Car"
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engintype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engintype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.engintype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)