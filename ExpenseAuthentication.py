def authentication(userName, password): #created a function and passed two arguments

    valid_username = "Expense"
    valid_password = "Ajay@2023"

#Build a condition to check validation

    if userName == valid_username and password == valid_password: 
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed. Invalid username or password. Please entet the correct ")
        return False
    
#taking input from the user
user = input("Enter your username: ") 
pwd = input("Enter your password: ")

authentication(user, pwd)