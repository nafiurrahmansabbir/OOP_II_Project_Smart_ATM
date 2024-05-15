# class User:
#     def __init__(self, name, password, balance):
#         self.name = name
#         self.password = password
#         self.balance = balance

#     def __repr__(self):
#         return f"User(name='{self.name}', password='{self.password}', balance={self.balance})"

# def create_user():
#     name = input("Enter the user's name: ")
#     password = input("Enter the user's password: ")
#     balance = int(input("Enter the user's balance: "))
#     return User(name, password, balance)

# users = []

# # Prompt user to enter the number of users they want to create
# num_users = int(input("How many users do you want to create? "))

# for x in range(num_users):
#     user = create_user()
#     users.append(user)

# # Output the list of users
# for user in users:
#     print(user)
