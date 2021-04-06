#Initialize the system
import random
database = {}

def init():
    print("Welcome to bankPython")
    haveAccount = int(input("Do you have an account with us? 1 (yes) 2 (no)\n"))
    
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("Invalid Option\n")
        init()

def login():
    print("Login to your account\n")
    accountNumberfromUser = int(input("What is your account number?\n"))
    password = input("What is your password?\n")
    found = False
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberfromUser):
            found = True
            if(userDetails[3] == password):
                bankOperation(userDetails)
            else:
                print("Invalid password\n")
                init()
    
    if(found == False):
        print("Account not found, please try again\n")
        init()

def register():
    print("******* Register *******")
    firstName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    email = input("What is your email address?\n")
    password = input("Create a password\n")
    currentMoney = 0

    accountNumber = generationAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password, currentMoney]
    print("Your account has been created, your account number is ", accountNumber, "\n")
    init()

def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit\n"))

    if(selectedOption == 1):
        depositOperation(user)
    elif(selectedOption == 2):
        withdrawalOperation(user)
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected\n")
        bankOperation(user)

def withdrawalOperation(user):
    print("Your current balance is $", user[4], "\n")
    amount = int(input("How much would you like to withdrawl?\n"))
    if(amount > int(user[4])):
        print("Insuffient funds, please enter a different amount\n")
    else:
        user[4] = user[4] - amount
        print("Please take your money below, your updated balance is $", user[4])
    bankOperation(user)

def depositOperation(user):
    print("Your current balance is $", user[4], "\n")
    depositAmount = int(input("Please enter the amount you would like to deposit\n"))
    user[4] = user[4] + depositAmount
    print("Your updated balance is $", user[4], "\n")
    bankOperation(user)

def generationAccountNumber():
    return random.randrange(1000000000,9999999999)

def logout():
    init()

def exit():
    print("Goodbye\n")

#### ACTUAL BANKING SYSTEM ####

init()