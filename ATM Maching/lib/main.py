from ATM import ATM
from Users import User
from Voic_Controller import speak

# bank theke kisu data nilam
user1 = User("sabbir", "0000", 1000)
user2 = User("rony", "0000", 500)
user3 = User("sabrin", "000", 500)
user4 = User("tiyas", "0000", 500)
#list er moddhe raikha dilam sob obj.
users = [user1, user2, user3, user4] 



def new_user():
       
# full_name=input("Emter your Full name: ")
    print("\n\n*** Registation Form ***")
    print("Please fill our registation form,sir.")
    speak("Please fill our registation form,sir.")
    name = input("Enter the user's name: ")
    password = input("Enter the user's password: ")
    balance = int(input("Enter the inisital Deposit: "))
    new_users = User(name, password, balance)
    users.append(new_users)
        
    print(f"Welcome {name} sir, You are a member of our Smart ATM Bank")
    speak(f"Welcome {name} sir, You are a member of our Smart ATM Bank")
    print("Your first Deposit Succesful....\n\n")
    speak("Your first Deposit Succesful")
        
        
        
    print("For Login")
    speak("For Login")

def main(): 
           

    # Notun Member Add: 
    cmd=input("Are you new member in our bank? Y/N : ")
    if(cmd=='y' or cmd=='Y'):
        new_user()
        atm = ATM(users)
        atm.main_menu()
        
    elif(cmd=='n' or cmd=='N'):
        
        
        atm = ATM(users)
        atm.main_menu()
    else:
        print("Invalid Input")
    
    
    

if __name__ == "__main__":
    print("Welcome to the ATM!")
    speak("Welcome to the ATM!")
    main()
