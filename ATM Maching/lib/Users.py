from Voic_Controller import speak

# from abc import ABC, abstractmethod
# class Account(ABC):

class Account():
    def __init__(self, balance):
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
        

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
            # money check korte hbe.......
            print("Wait for processing.........")
            speak("Checking deposited Money\n processing......")
            
            print("Deposit successful.")
            speak("Deposit successful.")
            print("Remaining balance:", self.__balance)
        

class User(Account):
    def __init__(self, name, pin, balance):
        super().__init__(balance)
        self.__name = name
        self.__pin = pin
    
    def get_name(self):
        return self.__name
    
    def authenticate(self, pin):
        return self.__pin == pin
    
    
    
    # Polimorphisom Added.
    # 
    
    def withdraw(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            super().withdraw(amount)
        else:
            print("Invalid amount or insufficient balance.")
            speak("Invalid amount or insufficient balance.")  
          
    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount) 
        else:
            print("Invalid amount.")
            speak("Invalid amount.") 

