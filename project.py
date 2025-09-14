class chohanbook:
    
     __user_id = 0 # static variable

     def __init__(self):
        # attributes

        self.__name = 'Huraira'
        self.id = chohanbook.__user_id
        chohanbook.__user_id += 1
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.messege = ""
        self.post = ""
     #    self.menu()

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
             self.user_post()
        elif user_input == '4':
             self.snd_message()
        else:
             exit()


     @staticmethod  # Not giving self, obj can't access it only class can.
     def get_id():
         return chohanbook.__user_id


     @staticmethod
     def set_id(value):
         chohanbook.__user_id = value


     def get_name(self):   # getter
         return self.__name


     def set_name(self,value): # setter
         self.__name = value


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
                self.loggedin = True
                self.menu()
           else:
                print("Enter right credidentials.")
                print("")
                self.menu()


     def user_post(self):
        if self.loggedin == True:
            txt = input("Enter your content : ")
            self.post_text = txt   # save it
            print(f"Posted : {txt}")
            self.menu()
        else:
            print("Plz signin first...")
            self.menu()




     def snd_message(self):
        if self.loggedin == True:
             user = input("Type friend_name : ")
             message = input("Type your message here : ")
             print(f"Your message {message} has been sent to {user}")
             self.menu()
        else:
             print("Plz signin first...")         
             self.menu()



x = chohanbook()
    