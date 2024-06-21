import user as u
import user_service as service
import pwinput
import bcrypt
import datetime

# Will attempt to authenticate a user with inputted username
# User has 3 attempts to enter the correct password before they are rejected
def attemptLogin(tempUsername:str) -> bool:
    tries = 0
    while tries < 3:
        tempPassword = pwinput.pwinput(prompt='Enter password: ')
        login = service.authenticate(tempUsername, tempPassword)
        if login:
            tries = 3
        else:
            print('Incorrect password, please try again')
            tries += 1
    return login

# Runs the signup form for the user
def signUp() -> list:
    exit = False
    userDetails = []
    
    fullName = input('Enter full name: ')
    role = service.checkUser(fullName)
    if role == -1:
        print('Account already exists for this user')
        return []
    if role == -2:
        print('Invalid user, does not exist in the system')
        return []

    badUser = True
    while badUser:
        tempUser = input('Enter Username: ')
        result = service.checkUsernameDup(tempUser)
        if result:
            userDetails.append(tempUser)
            badUser = False
        else:
            print('Username already exists, please try another username')
    
    
    # Prompts user to reenter passwords until a strong password is accepted
    badPass = True
    while badPass:
        tempPass = pwinput.pwinput(prompt='Enter password: ')
        result = service.passwordChecker(tempUser,tempPass)
        if result[0]:
            userDetails.append(service.hashPassword(tempPass))
            badPass = False
        else:
            print(result[1])
    
    userDetails.append(str(u.User.generateUID()))
    userDetails.append(role)
    userDetails.append(fullName)
    userDetails.append(input('Enter email: '))
    userDetails.append(input('Enter phone number: '))

    return userDetails

# Provides the user with a simple GUI to conduct their actions
# Some GUIs are unqiue based on the role of the user
def roleMenu(user:u.User):
    role = u.Role(int(user.role))
    exit = False

    # Menu for regular clients
    if role == u.Role.CLIENTS:
        print('Welcome Client '+user.fullName)
        print('-----------------------------------------------')
        print('Please enter the number of the action you wish to perform...')
        print('')
        while not exit:
            print('Logout[0]  Account Balance[1]  Investment Portfolio[2] Contacts[3]')
            try:
                command = int(input())
            except:
                print('Unknown command')
            print('')

            if(command == 0):
                break
            if(command == 1):
                print('Here is your account balance view')
            if(command == 2):
                print('Here is your investment portfolio view')
            if(command == 3):
                print('Here is your financial advisor contact')
            if(command > 3):
                print('Unknown command')
            print('')

    # Menu for premium clients
    if role == u.Role.PREMIUM:
        print('Welcome Premium Client '+user.fullName)
        print('-----------------------------------------------')
        print('Please enter the number of the action you wish to perform...')
        print('')
        while not exit:
            print('Logout[0]  Account Balance[1]  Investment Portfolio[2] Contacts[3]')
            try:
                command = int(input())
            except:
                print('Unknown command')
            print('')

            if(command == 0):
                break
            if(command == 1):
                print('Here is your account balance view')
                print('')
            if(command == 2):
                print('Here is your investment portfolio')
                loop = True    
                while loop:
                    print('Back[0]  View[1]  Edit[2]')
                    try:
                        miniCommand = int(input())
                    except:
                        print('Unknown command')
                        print('')

                    if(miniCommand == 0):
                        loop = False
                    if(miniCommand == 1):
                        print('You viewed your investment portfolio')
                    if(miniCommand == 2):
                        print('You editted your investment portfolio')
                    if(command > 2):
                        print('Unknown command')
                    print('')
            if(command == 3):
                print('Here is your contacts')
                loop = True    
                while loop:
                    print('Back[0]  Financial Advisor[1]  Financial Planner[2] Investment Analyst[3]')
                    try:
                        miniCommand = int(input())
                    except:
                        print('Unknown command')
                        print('')

                    if(miniCommand == 0):
                        loop = False
                    if(miniCommand == 1):
                        print('You viewed your financial advisors contact')
                    if(miniCommand == 2):
                        print('You viewed your financial planners contact')
                    if(miniCommand == 3):
                        print('You viewed your invesment analysts contact')
                    if(command > 3):
                        print('Unknown command')
                    print('')
            if(command > 3):
                print('Unknown command')
            print('')

    # Menu for planners
    if role == u.Role.PLANNER:
        print('Welcome Financial Planner '+user.fullName)
        print('-----------------------------------------------')
        print('Please enter the number of the action you wish to perform...')
        print('')
        while not exit:
            print('Logout[0]  View Client Account Balance[1]  Clients Investment Portfolio[2]')
            print('View Money Market Instruments[3] View Private Consumer Instruments[4]')
            try:
                command = int(input())
            except:
                print('Unknown command')
            print('')

            if(command == 0):
                break
            if(command == 1):
                print('Here is the clients account balance view')
                print('')
            if(command == 2):
                print('Here is the clients investment portfolio')
                loop = True    
                while loop:
                    print('Back[0]  View[1]  Edit[2]')
                    try:
                        miniCommand = int(input())
                    except:
                        print('Unknown command')
                    print('')

                    if(miniCommand == 0):
                        loop = False
                    if(miniCommand == 1):
                        print('You viewed your investment portfolio')
                    if(miniCommand == 2):
                        print('You editted your investment portfolio')
                    if(command > 2):
                        print('Unknown command')
                    print('')
            if(command == 3):
                print('You have viewed money market instruments')
            if(command == 4):
                print('You have viewed money market instruments')
            if(command > 4):
                print('Unknown command')
            print('')

    # Menu for advisors
    if role == u.Role.ADVISOR:
        print('Welcome Financial Advisor '+user.fullName)
        print('-----------------------------------------------')
        print('Please enter the number of the action you wish to perform...')
        print('')
        while not exit:
            print('Logout[0]  View Client Account Balance[1]  Clients Investment Portfolio[2]')
            try:
                command = int(input())
            except:
                print('Unknown command')
            print('')

            if(command == 0):
                break
            if(command == 1):
                print('Here is the clients account balance view')
                print('')
            if(command == 2):
                print('Here is the clients investment portfolio')
                loop = True    
                while loop:
                    print('Back[0]  View[1]  Edit[2]')
                    try:
                        miniCommand = int(input())
                    except:
                        print('Unknown command')
                        print('')

                    if(miniCommand == 0):
                        loop = False
                    if(miniCommand == 1):
                        print('You viewed your investment portfolio')
                    if(miniCommand == 2):
                        print('You editted your investment portfolio')
                    if(command > 2):
                        print('Unknown command')
                    print('')
            if(command == 3):
                print('You have viewed private consumer instruments')
            if(command > 3):
                print('Unknown command')
            print('')

    # Menu for analysts
    if role == u.Role.ANALYST:
        print('Welcome Financial Analyst '+user.fullName)
        print('-----------------------------------------------')
        print('Please enter the number of the action you wish to perform...')
        print('')
        while not exit:
            print('Logout[0]  View Client Account Balance[1]  Clients Investment Portfolio[2]')
            print('View Money Market Instruments[3] View Derivatives Trading[4]')
            print('View Interest Instruments[5] View Private Consumer Instruments[6]')
            try:
                command = int(input())
            except:
                print('Unknown command')
            print('')

            if(command == 0):
                break
            if(command == 1):
                print('Here is the clients account balance view')
            if(command == 2):
                print('Here is the clients investment portfolio')
                loop = True    
                while loop:
                    print('Back[0]  View[1]  Edit[2]')
                    try:
                        miniCommand = int(input())
                    except:
                        print('Unknown command')
                        print('')
                        
                    if(miniCommand == 0):
                        loop = False
                    if(miniCommand == 1):
                        print('You viewed the clients investment portfolio')
                    if(miniCommand == 2):
                        print('You editted the clients investment portfolio')
                    if(command > 2):
                        print('Unknown command')
                    print('')
            if(command == 3):
                print('You have viewed money markets instruments')
            if(command == 4):
                print('You have viewed derivatives trading')
            if(command == 5):
                print('You have viewed interest instruments')
            if(command == 6):
                print('You have viewed private consumer instruments')
            if(command > 6):
                print('Unknown command')
            print('')

    # Menu for tech support
    if role == u.Role.SUPPORT:
        # add timing restriction
        print('Welcome Technical Support '+user.fullName)
        print('-----------------------------------------------')
        print('Please enter the number of the action you wish to perform...')
        print('')
        while not exit:
            print('Exit[0]  View Client Information[1]  Request Client Access[2]')
            try:
                command = int(input())
            except:
                print('Unknown command')
            
            if(command == 0):
                break
            if(command == 1):
                print('Here is the clients information')
            if(command == 2):
                print('Request sent for client access')
            if(command > 2):
                print('Unknown command')
            print('')

    # Menu for tellers
    if role == u.Role.TELLER:
        now = datetime.datetime.now()
        today9am = now.replace(hour=9,minute=0,second=0,microsecond=0)
        today5pm = now.replace(hour=17,minute=0,second=0,microsecond=0)
        if(now > today9am and now < today5pm):
            print('Welcome Teller '+user.fullName)
            print('-----------------------------------------------')
            print('Please enter the number of the action you wish to perform...')
            print('')
            while not exit:
                print('Logout[0]  View Client Account Balance[1]  View Client Investment Portfolio[2]')
                try:
                    command = int(input())
                except:
                    print('Unknown command')
                
                if(command == 0):
                    break
                if(command == 1):
                    print('View client account balance')
                if(command == 2):
                    print('View client investment portfolio')
                if(command > 2):
                    print('Unknown command')
                print('')
        else:
            print('Welcome Teller '+user.fullName)
            print('-----------------------------------------------')
            print('It is currently after business hours.')
            print('If you wish to access the system please return between 9am to 5pm')
            print('')

    # Menu for compliance officers
    if role == u.Role.OFFICERS:
        print('Welcome Compliance Officer '+user.fullName)
        print('-----------------------------------------------')
        print('Please enter the number of the action you wish to perform...')
        print('')
        while not exit:
            print('Logout[0]  View Client Account Balance[1]  View Client Investment Portfolio[2] Validate Investment Portfolios[3]')
            try:
                command = int(input())
            except:
                print('Unknown command')
            
            if(command == 0):
                break
            if(command == 1):
                print('View client account balance')
            if(command == 2):
                print('View client investment portfolio')
            if(command == 3):
                print('Validate client investment portfolio')
            if(command > 3):
                print('Unknown command')
            print('')

def run():
    exit = False
    login = False
    command = -1

    print('Finvest Holdings')
    print('Client Holdings and Information System')
    print('-----------------------------------------------')
    print('Please enter the number of the action you wish to perform...')
    print('')
    while not exit:
        print('Exit[0] Login[1] Signup[2]')
        try:
            command = int(input())
        except:
            print('Unknown command')
        
        # Exit
        if(command == 0):
            exit = True
        
        # Login
        if(command == 1):
            tempUsername = input('username: ')
            login = attemptLogin(tempUsername)
            if login:
                print('Login Successful')
                userDetails = service.getUser(tempUsername)
                authUser = u.User(userDetails[0],userDetails[1],userDetails[2],userDetails[3],userDetails[4],userDetails[5],userDetails[6])
                roleMenu(authUser)
            else:
                print('Incorrect Username and Password')
        
        #   Sign up
        if(command == 2):
            userDetails = signUp()
            if userDetails:
                print('Signup Successful')
                authUser = u.User(userDetails[0],userDetails[1],userDetails[2],userDetails[3],userDetails[4],userDetails[5],userDetails[6])
                service.enrol(userDetails)
                roleMenu(authUser)

        if(command > 2):
            print('Unknown command')

        print('')


if __name__ == '__main__':
    run()