# # a class is a recipe
# # an object is the food you made with the recipe
# # the recipe can be used lots, and lots of times
# # Our blueprint for making cars is called Car
# class Car(object):
#     # whenever we start making a new car, __init__ will run
#     # we ALWAYS pass self first
#     def __init__(self):
#         # self is special.
#         # self refers to THIS object
#         self.make = "Honda"
#         self.model = "Accord"
#         self.year = 2007
# myCar = Car()
# print myCar.make
# yourCar = Car()
# print yourCar.make
# yourCar.make = "Toyota"
# print myCar.make
# print yourCar.make
# myCar = {
#     "make": "Honda",
#     "model": "Accord",
#     "year": 1997
# }
#yourCar = {
#     "make": "Honda",
#     "model": "Accord",
#     "year": 2007
# }
# print myCar['make']
 # myCar = [
#     "Honda",
#     "Accrod",
#     2007
# ]
# print myCar[0]
# class Car(object):
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model
#     def changeModel(self,newModel):
#         self.model = newModel
#  zachsCar = Car('Ford',"F150")
# chrisCar = Car('Chevy',"Silverado")
# zachsCar.isCool = "Awesome!"
# zachsCar.changeModel("Fiesta")
# zachsCar.model = "Fiesta"
# print zachsCar.model
# # print zachsCar.make
# # print chrisCar.make
# # print zachsCar.model
# # print chrisCar.model
# # print zachsCar.isCool
# # zachsCar.model = "Focus"
# # # ZACHS CAR: DONT MESS WITH ME!!
# # print zachsCar.model

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self): 
        print("%s %s %s") % (self.year, self.make, self.model )
car = Vehicle('Nissan', 'Leaf', 2015)    
# print (car.make)  
# print (car.model)
# print (car.year)  
car.print_info()
# Create a class Vehicle. A Vehicle object will have 3 attributes:

# make
# model
# year
# A vehicle is created thus:

# car = Vehicle('Nissan', 'Leaf', 2015)
# And you can access it's attributes individually like so:

# print car.make, car.model, car.year
# Add a method
# Add a print_info method to the Vehicle class. 
# It will print out the vehicle's information like so:

# >>> car.print_info()
# 2015 Nissan Leaf