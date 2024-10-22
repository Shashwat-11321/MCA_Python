class Dog:
    #Class attrib shared by all instances
    species="Canis Familiaris"
    
    #Constructor
    def init(self , age, name):
        self.name = name
        self.age = age

    def bark(self):

        return f"{self.name} say woof!"
    
    def get_age(self):
        return f"{self.name}is {self.age} years old "


dog1 = Dog("Buddy", 3)

dog2 = Dog("Brian", 5)

