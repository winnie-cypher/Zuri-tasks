#register
# -  username, password, email
# - generation user account



#login
# - (username or email) and password

#bank operations

#initializing the system
import random
import validation
import database
from getpass import getpass


def init():
    
    #isValidOptionSelected = false
    print("welcome to bankPHP")
    
   # while isValidOptionSelected == False:
        
    haveAccount = int(input("do you have account with us: 1 (yes) 2 (no) \n"))
    
    if(haveAccount == 1):
        isValidOptionSelected =  True
        login()
    elif(haveAccount == 2):
        isValidOptionSelected =  True
        register()
    else:
        print("You have selected invalid option")
        
    
def login():
    print("***** Login *****")
    
    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:
           

         print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits")
        init()
    
def register():
    print("***** Register *****")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create your own password \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()

    
def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)
        
        
def withdrawal_operation():
    print("withdrawal")
   


def deposit_operation():
    print("Deposit Operations")
    
    
def generateAccountNumber():
     return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()

#### ACTUAL BANKING SYSTEM ####
init()

    



 