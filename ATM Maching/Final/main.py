from ATM import ATM
from Users import User

def main():
    user1 = User("sabbir", "0000", 1000)
    user2 = User("rony", "0000", 500)
    user3 = User("sabrin", "000", 500)
    user4 = User("tiyas", "0000", 500)
    users = [user1, user2, user3, user4]

    atm = ATM(users)
    atm.main_menu()

if __name__ == "__main__":
    main()
