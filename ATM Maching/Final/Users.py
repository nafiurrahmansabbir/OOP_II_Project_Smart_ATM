from Voic_Controller import speak

class Account:
    def __init__(self, balance=0):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        self.__balance = amount
    
    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print("Withdrawal successful.")
            speak("Withdrawal successful.")
            
            print("Remaining balance:", self.__balance)
        else:
            print("Invalid amount or insufficient funds.")
            speak("Invalid amount or insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
            speak("Deposit successful.")
            
            print("Remaining balance:", self.__balance)
        else:
            print("Invalid amount.")
            speak("Invalid amount.")
    
    

class User(Account):
    def __init__(self, name, pin, balance=0):
        super().__init__(balance)
        self.__name = name
        self.__pin = pin
    
    def get_name(self):
        return self.__name
    
    def authenticate(self, pin):
        return self.__pin == pin
