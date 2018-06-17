


class Car(object): # Car factory
    
    MAX_SPEED = 140
    MAX_BACK_SPEED = -10
    
    def __init__(self, color):
        self.color = color
        
    def __repr__(self):
        return 'I am your ' + self.color + ' ' + self.__class__.__name__
        
    def drive(self, speed):
        speed = min(speed, self.MAX_SPEED)
        speed = max(speed, self.MAX_BACK_SPEED)
        print 'I am driving', speed, 'km/hr'

class Volkswagen(Car):
    pass

class Ferrari(Car):
    
    MAX_SPEED = 350

    def __init__(self, color):
        self.color = 'yellow'
         
# ---------------------------------------------------------

myCar = Volkswagen('blue')
print myCar
myCar.drive(90)
myCar.drive(120)
myCar.drive(12000000000)
myCar.drive(-5000000)

myFastCar = Ferrari('pink')
print myFastCar
myFastCar.drive(12000000000)
myFastCar.drive(-5000000)
