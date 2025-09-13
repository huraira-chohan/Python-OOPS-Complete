class chohanbook:
    def __init__(self):
        # attributes
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.messege = ""
        self.post = ""
        self.menu()

        # methods
    def menu(self):
        user_input = (input("""
            Press 1 for signup.
            Press 2 for signin.
            Press 3 to post.
            Press 4 to message a friend.
            Press any other key to exit."""))
        
        if user_input == '1':
             self.signup()
        elif user_input == '2':
             self.signin()
        elif user_input == '3':
             pass
        elif user_input == '4':
             pass
        else:
             exit()



    def signup (self):
         email = input("Plz enter your email : ")
         pwd = input("Plz setup your passcode : ")
         self.username = email
         self.password = pwd
         print("You have signed up." 
                "Sucessfully")
         print("")
         self.menu()



    def signin (self):
        if self.username== "" and self.password == "":
              print("")
              print("Press 1 to signup first...")
              self.menu()
              
        else:
           uemail =  input("Plz enter your email : ")
           upwd = input("Plz enter your password : ")
           if self.username == uemail  and self.password == upwd:
                print('You have signed in sucessfully.')
                print("")
                self.menu()
                self.loggedin == True
           else:
                print("Enter right credidentials.")
                print("")
                self.menu()



x = chohanbook()
    