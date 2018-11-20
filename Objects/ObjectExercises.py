
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)




# # 1. Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# # 2. Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# jordan = Person('Jordan', 'jordan@aol.com','495-586-3456')
# # 3.Have sonny greet jordan using the greet method.
# sonny.greet(jordan)
# # 4. Have jordan greet sonny using the greet method.
# jordan.greet(sonny)
# # 5. Write a print statement to print the contact info (email and phone) of Sonny.
# print sonny.email, sonny.phone
# # 6. Write another print statement to print the contact info of Jordan.
# print jordan.email, jordan.phone


class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print("%s %s %s") % (self.year, self.make, self.model )
car = Vehicle('Nissan', 'Leaf', 2015)    
print("%s %s %s") % (car.make, car.model, car.year)  
# print ()
# print ()  
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