

class Car(object): # Factory
    MAX_SPEED = 150
    
    def __init__(self, color):
        self.color = color
        
    def drive(self, speed):
        print('I am a %s %s and driving %d m/h' % (self.color, self.__class__.__name__, min(self.MAX_SPEED, speed)))

class Volkswagen(Car):
    pass
    
class Maserati(Car):
    MAX_SPEED = 300  

    def __init__(self, color):
        if color != 'Yellow':
            #raise ValueError("Maserati's only come in yellow, not in %s" % color)
            print("$$$# Maserati's only come in yellow, not in %s" % color)
        self.color = 'Yellow'

# -----------------------------------------
   
car = Volkswagen('Blue') # instance, object
print(car.color)
car.drive(50)
car.drive(80)
car.drive(4322342343454534354533241234080)

myDreamCar = Maserati('Blue')
myDreamCar.drive(4322342343454534354533241234080)


# car.__class__.__dict__('drive')(car, 50)