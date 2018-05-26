import random


class Car(object):
    vin = random.randint(10000000000, 99999999000)

    def __init__(self, color="Black", wheels=5):
        self.wheels = wheels
        self.vin = Car.vin
        Car.vin += 1
        self.color = color
        if self.color is "Red":
            self.wheels = wheels - 1

    # there were no methods defined in previous form of my task6(class_Car.py)
    # so here it is the right one!
    def diag(self):
        return self.color, self.wheels


mazda = Car(color="Red")
zhiguli = Car()
lada = Car(color="Blue")

print zhiguli.diag()
print mazda.diag()
print lada.diag()
