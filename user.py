from enum import Flag
from uuid import uuid4


class Role(Flag):
    CLIENTS = 1
    PREMIUM = 2
    PLANNER = 3
    ADVISOR = 4
    ANALYST = 5
    SUPPORT = 6
    TELLER = 7
    OFFICERS = 8


class User:
    def __init__(self, username:str, password:str, uid:str, role:int, fullname:str,email:str, phonenumber:str) -> None:
        self.username = username
        self.password = password
        self.UID = uid
        self.role = role
        self.fullName = fullname
        self.email = email
        self.phoneNumber = phonenumber
    
    def fromCSV(self, csvInput) -> None:
        self.username = csvInput[0]
        self.UID = csvInput[1]
        self.password = csvInput[2]
        self.role = int(csvInput[3])
        self.email = csvInput[4]
        self.phoneNumber = csvInput[5]

    def toString(self) -> str:
        string = self.username + ':' + self.password + ':' + self.uid + ':' + str(self.role) + ':' + self.fullName + ':' + self.email + ':' + self.phoneNumber
        return string
    
    def generateUID() -> str:
        return uuid4()
    

