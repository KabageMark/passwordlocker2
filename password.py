from dataclass import Account
from dataclass import Passwords

def createaccount(firstname,lastname,email):
    new_account = Account(firstname,lastname,email)
    return new_account
