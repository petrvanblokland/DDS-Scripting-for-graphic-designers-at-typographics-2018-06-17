
# A class can be seen as a factory of objects. 
# It worth mentioning that a factory is an object too, but in this stage you can ignore that.
# class Car(object): means that we define the behavior of a Car factory, starting to make it
# inheriting from the super-generic Python "objects" class.
# It is a convention to write class names with an initialial capitial, to differentiate class
# names from object name (which start with a lower case.
# (It is a bit of a Python syntax anomaly that the super-object class does not start with a capital.

class Car(object):
    # This is the space where the behavior of the Car factory is defined, starting with
    # "class constants", traditionally written in all caps. Although technically they are 
    # just variables that can be changed, they function a not-to-be-changed.
    # If it good practice to define here the values that you don't want to be altered by
    # objects or user programs. The ALL_CAPS of the name indicates that.
    # In this case the maximum speed of a car obtect is build in during manufacturing, but it
    # can vary between car models or types of Car factories.
	MAX_SPEED = 150 # Class constant
	MAX_BACKSPEED = -20

    # The "methods" are defined. These are functions that belong to a class and object.
    # Some of them are methods that already exist by inheriting from the super-object.
    # They can be recognizes by names starting and ending with a double "_" underscore.
    # The most important one is the "__init__", which will be called by the factory itself,
    # during construction of the object. The values (attributes) it takes between the parenthesis
    # is what the designer of the factory thinks is needed during the fabrication process.
    # In our example that is the color of the car.
    # The "self" in this method is the actual car object that is produced.
    # The "self.color = color" is the symbol for characteristics of the car (that become 
    # intrinsic part of the car object) during the production phase.
    
    # In this example the Car factory needs the color of the car as "ordering parameter"
	def __init__(self, color='Black', automatic=False):
		self.color = color # Store color as part of the car instance = self
		self.automatic = automatic # Can be True or False 
		
    # Then there are other methods that define how the car object functions.
    # Note that the definintion of the method is done in the factory (making the object know
    # how to drive) without actually driving inside the factory.
    # The actual calling of the method is done when the car is used, where it takes the
    # speed (which can a positive or negative value or even zero.
	def drive(self, speed):
		speed = min(speed, self.MAX_SPEED) # Limit requested speed to the maximum speed of the car.
		speed = max(speed, self.MAX_BACKSPEED) # In case it is negative, limit to the maximum reverse speed.
		# In this example, show the driving by printing a line with information.
		# Since we don' know what kind of car we are here, the class name is used to identify.
		print 'I am a %s %s, driving %d mph' % (self.color, self.__class__.__name__, speed)

# An important advantage of programming with objects and classes, is that you often don't nee to 
# start from scratch. If there is an existing class (as the one above), a new class can start by
# inheriting all characteristing from the Car factory.
# In this example the "Volkswagen" behaves just like the default Car, so we don't have to change
# anything to the factory. The Python instruction "pass" is a place holder, in case there is no
# code to fill a certain area in a program.
class Volkswagen(Car):
	pass

# Here is an example of a car type that is different from the default. Fortunately, since the original
# Car factory code was written with this kind of inheritance in mind, we only need to change two
# of the characteristics: the MAX_SPEED and the way a Ferrari accepts a color request.
# The driving method is not changed, because the default definition was written in a generic way,
# taking the class name in the print, instead of a hard coded string.
class Ferrari(Car):
	MAX_SPEED = 350 # Class constant, defining the default value in the Car factory
	# Note that the reverse speed is not changed.

	def __init__(self, color):
	    # There the Volkswagen accepts any color, the Ferrari will always be produced in 'yellow',
	    # no matter what color was ordered.
		self.color = 'yellow' # Store color as part of the car instance = self

# ------------------------------------------------------

# Car = Car factory, blue print
# Car() produces a car instance or object.
#myCar = Volkswagen('red', True) # Call the Volkswagen factory, to create a new red car object (= instance)
#myCar = Volkswagen(automatic=True)
print Volkswagen
myCar = Volkswagen(color='Red')
print 'Is it automatic?', myCar.automatic
myCar.drive(-60000000) # Instruct the car to drive backwards, see the speed being limited to factory settings.
myCar.drive(60) # Normal driving within the speed limitaion of the car.
myCar.color = 'blue' # Repaint the car: same object, other color.
myCar.drive(108000000000) # Drive the car at maximum speed, see that is adjusted it color in the output.

myCar = Ferrari('blue') # Try to create a blue Ferrari
myCar.drive(108000000000) # See that is yellow and it drives in (adjusted) maximum factory speed.

# What are attributes?
print myCar.color # Attribute --> value
print myCar.drive # Attribute --> type is a method, so it can be called
#myCar.color() This does not work TypeError: 'str' object is not callable
myCar.drive
#yAirplane.drive = myCar.drive Never do this at home

