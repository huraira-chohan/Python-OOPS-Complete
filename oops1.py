# initialize a class :

class employee :
    # initialize special magic/dunder method - constructor
    # attributes are called by themselves

    def __init__(self):

        print(id(self))
        # print("attributes being initiated")

        self.__name = 'Huraira' # encapsulation
        self.id = 123
        self.salary = 5000
        self.dep = 'SDE'

        # print('attributes initiated')


    # func made inside a class is called a method
    # we call method manually

    def travel(self,destination):
        #  print("Manually Initialized")
         print(f"Employee is going to {destination}")


# Make an obj of the class :

# sam = employee()
# print(id(sam))

# Making an attribute outside of the class :

# sam.name = 'Shaktiman'
# print(sam.name)


# Calling Attributes :

# print(sam.salary)
# sam.id
# sam.dep

# Calling a method :

# print(sam.travel('isl'))
