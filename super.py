# Using Super Keyword :

class Animal :
    def __init__(self):
        self.name = 'bud'

    def speak(self):
        print(f"{self.name} has a sound.")

class Dog(Animal):

    def __init__(self, breed):
         super().__init__() # taking animal attributes
         self.breed = breed

    def speak(self):
        super().speak() # using animal methods
        print(f"{self.name} barks. He is a {self.breed}")

dog = Dog("GR")
dog.speak()
