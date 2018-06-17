
class Car(object): # Factory of Cars --> generates cars -> Instance = object 
    
    MAX_SPEED = 120 # Class constant
    MIN_SPEED = -20
    
    def __init__(self, color):
        self.color = color # Paint the beams + hull in that color
        # Add engine
        # Add wheels
        # Add seats
        # Here the car (self) is finished and send to the dealer
        
    def __repr__(self):
        return 'I am a happy car'
        
    def drive(self, speed):
        speed = min(speed, self.MAX_SPEED) # What is the max speed of self
        speed = max(speed, self.MIN_SPEED)
        print('I am a %s and driving %d m/hr' % (self.__class__.__name__, speed))

class Ford(Car):
    pass
class Maserati(Car):
    MAX_SPEED = 200
    def __init__(self, color):
        self.color = 'Yellow' # Paint the beams + hull in that color
           
#----------------------------------------------------

myCar = Ford('Blue') # Buying the car
print(myCar.color)
myCar.drive(-120000)
myCar.drive(4500000)
myDream = Maserati('Orange')
myDream.drive(45000000000000000000)
print(myDream.color)
