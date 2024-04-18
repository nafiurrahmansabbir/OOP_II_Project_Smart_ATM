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
            print("Remaining balance:", self.__balance)
        else:
            print("Invalid amount or insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
            print("Remaining balance:", self.__balance)
        else:
            print("Invalid amount.")

class User(Account):
    def __init__(self, name, pin, balance=0):
        super().__init__(balance)
        self.__name = name
        self.__pin = pin
    
    def get_name(self):
        return self.__name
    
    def authenticate(self, pin):
        return self.__pin == pin

class ATM:
    def __init__(self, users):
        self.__users = users
    
    def authenticate_user(self, name, pin):
        for user in self.__users:
            if user.get_name() == name and user.authenticate(pin):
                return user
        return None
    
    def main_menu(self):
        print("Welcome to the ATM!")
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        
        user = self.authenticate_user(name, pin)
        
        if user:
            while True:
                print("\n1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")
                choice = input("Enter your choice: ")
                
                if choice == '1':
                    print("Your balance is:", user.get_balance())
                elif choice == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                elif choice == '3':
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
                elif choice == '4':
                    print("Thank you for using the ATM!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Authentication failed. Invalid name or PIN.")

# Sample usage
user1 = User("sabbir", "0000", 1000)
user2 = User("rony", "0000", 500)
user3 = User("sabrin", "000", 500)
user4 = User("tiyas", "0000", 500)
users = [user1, user2,user3,user4]

atm = ATM(users)
atm.main_menu()
