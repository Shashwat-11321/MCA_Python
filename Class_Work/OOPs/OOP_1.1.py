class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
        self.__age__=age  #Private Priperty
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."
       # def __str__ return f"{self.name} is {self.age}"
# Creating instances (objects) of the Dog class

class Cat:
    species =""

    def __init__(self , name , age):
        self.name=name
        self.age=age;
    
    def mewo(self):
        return f"{self.name} says Mewo"

    def get_age(self):
        return f"{self.name} is {self.age} years old "

cat1= Cat("cat ")


dog1 = Dog("Buddy", 3)

dog2 = Dog("Brian", 5)

print(dog1.bark())   
print(dog1.age)      # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris






