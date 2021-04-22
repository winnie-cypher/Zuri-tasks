
name = input("what is your name? \n")
allowedUsers = ['winner','olamide','kemi']
allowedPassword = ['passwordWinner','passwordOlamide','passwordKemi']


if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password in allowedPassword):
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('3. Logout')

        selectedOption = int(input('please select an option:'))

        if(selectedOption == 1):
            print('You selected %s' % selectedOption)
            
        elif(selectedOption == 2):
            print('You selected %s' % selectedOption)
            
        elif(selectedOption == 3):
            print('You selected %s' % selectedOption)
            
        elif(selectedOption == 4):
            exit()   
            
        else:
            print('Invalid option selected, please try again')
            
            
print("Welcome, what would you like to do?")
print("1. Login")
print("2. Register")

actionSelect = int(input("Select an option \n"))

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()


    
    
    name = input("What is your name? \n")

allowedUserDictionary = {
    'winner':'passwordWinner',
    'olamide':'passwordOlamide',
    'kemi':'passwordKemi'
    }

if(name in allowedUserDictionary):
    password = input("Your password? \n")    

    if(password == allowedUserDictionary[name]):
        
        print('Welcome %s' % name)
          
    
    
def withdrawal():
    
    amount = float(input("How much would you like to withdrawal?")
    #print('processing..')
    #print('take your cash')               
        
            
        
   # else:
       # print('Password incorrect, please try again')



