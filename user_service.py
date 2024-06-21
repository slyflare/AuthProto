import csv
import user as u
import bcrypt


#-------------------Password Checker-------------------

# Checks given password against the list of weak passwords
def checkWeakList(password:str) -> bool:
    with open('weak_list.txt') as f:
        if str.lower(password) in f.read():
            return True
        return False

# Checks if password set by user is strong
# A strong password is between 8 to 50 characters
# Password must not be in the list of weak passwords
# Password must contains a lowercase letter, uppercase letter, digit and one character from !@#$%?*
# Password must not have more than 2 consecutive digits
def passwordChecker(username:str,password:str) -> (bool, str):
    
    # Basic checks
    if len(password) < 8:
        return (False, "Password too short, minimum length of 8 required")
    if len(password) > 50:
        return (False, "Password too long, maximum length of 50")
    if username in password:
        return (False, "Password should not contain your username")
    if checkWeakList(password):
        return (False, "Password is too common")

    # character checks
    if not any(c.islower() for c in password):
        return (False, "Password must contain at least one lowercase letter")
    if not any(c.isupper() for c in password):
        return (False, "Password must contain at least one uppercase letter")
    if not any(c.isdigit() for c in password):
        return (False, "Password must contain at least one number")
    if not any(c in "!@#$%?*" for c in password):
        return (False, "Password must contain at least one special character")
    
    # consecutive digits check
    consecutiveDigit = 0
    for c in password:
        if consecutiveDigit > 2:
            return (False, "Password must not contain more than 2 consecutive numbers")
        else:
            if c.isdigit():
                consecutiveDigit += 1
            else:
                consecutiveDigit = 0

    return(True,"")

#-------------------Authenticator-------------------

# Authenication function
# Takes in username and password user has sent
# Finds corresponding password of inputted username in passwd.csv and 
def authenticate(tempUser:str, tempPass:str) -> bool:
    with open('passwd.txt', newline='') as pFile:
        reader = csv.reader(pFile, delimiter=':')
        for row in reader:
            if tempUser == row[0]:
                password = row[1].encode('utf-8')
                break
    return bcrypt.checkpw(tempPass.encode('utf-8'), password)

# Retrieves user data once they are authenticated
# Returns user data as list[str]
def getUser(tempUser:str) -> list:
     with open('passwd.txt', newline='') as pFile:
        reader = csv.reader(pFile, delimiter=':')
        for row in reader:
            if tempUser == row[0]:
                return row

#-------------------Enrolment-------------------

# Adds a new user's details into passwd.txt to allow authentication at a later date
def enrol(userRow:str) -> bool:
    with open('passwd.txt', 'a', newline='') as pFile:
        csvwriter = csv.writer(pFile, delimiter=':')
        csvwriter.writerow(userRow)

# Hashs a password using bcrypt
# Returns the hashed password decode from utf-8
def hashPassword(password:str) -> str:
    hashpw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
    return hashpw.decode('utf-8')

# Checks if the user's desired username is already taken
def checkUsernameDup(username:str) -> bool:
    with open('passwd.txt', newline='') as pFile:
        reader = csv.reader(pFile, delimiter=':')
        for row in reader:
            if username == row[0]:
                return False
        return True
    
# Checks if user has an account
# If the user does not have an account, then usersdb is checked to see if user exists in db.
# Return -1 if account exists, return -2 if user not in db, else return specified role in db.
def checkUser(fullname:str) -> int:
    with open('passwd.txt', newline='') as pFile:
        reader = csv.reader(pFile, delimiter=':')
        for row in reader:
            if fullname == row[4]:
                print(row[4])
                return -1 # User already has an account
    with open('usersdb.txt', newline='') as db:
        reader = csv.reader(db, delimiter=':')
        for row in reader:
            if fullname == row[1]:
                return int(row[0]) # Returns users role
    return -2 # User does not exist in db

