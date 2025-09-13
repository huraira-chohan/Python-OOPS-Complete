# gari ki class
class sell_your_gari:

    def __init__(self):
        # gari ky attributes
        self.model = ''
        self.color = ''
        self.milage = ''
        self.menu()
        
        # gari ka method


    def menu(self):
        user_input = input("""
                Press 1 to enter car model.
                Press 2 to enter car color.
                Press 3 to enter car milage.
                Press 4 to see car details.
                Press any other number to exit.
                >- """)

        if user_input == '1':
            self.gari_model()
        elif user_input == '2':
            self.gari_ka_color()
        elif user_input == '3':
            self.gari_milage()
        elif user_input == '4':
            self.show_details()
        else:
            exit()



    def gari_model(self):
        self.model = input("Plz enter gari ka model : ")
        self.menu()
        

    def gari_ka_color(self):
        self.color = input("Plz enter gari ka color : ")
        self.menu()

    def gari_milage(self):
        self.milage = input("Plz enter car milage : ")
        self.menu()

    def show_details(self):
        print(f"\nCar Model: {self.model}")
        print(f"Car Color: {self.color}")
        print(f"Car Milage: {self.milage}\n")

# gari ka object
bugatti = sell_your_gari()