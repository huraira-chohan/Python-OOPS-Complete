# Simple Inheritance :

class Animal :

    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} has a sound.")


    
class Cat(Animal) :  # This class will inheret all the attributes and 
                    #the methods of the parent class.
    
    def speak(self):
        print(f"{self.name} meows")



# dog = Animal('Cat')
# dog.sound()

cat = Cat('cat')
cat.speak()








