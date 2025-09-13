# gari ki class
class gari:

    def __init__(self):
        # gari ky attributes
        self.color = 'red'
        self.milage = 500
        self.engine = 'V12'

        # gari ka method

    def milage_eng(self):
        print(self.milage,self.engine)


# gari ka object
bugatti = gari()

# calling att
print(bugatti.engine)
    
# calling method    
bugatti.milage_eng()

