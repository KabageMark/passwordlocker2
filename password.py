from dataclass import Account
from dataclass import Passwords

def createaccount(firstname,lastname,email):
    new_account = Account(firstname,lastname,email)
    return new_account
    
def saveaccount(account):
     account.saveaccount()    

def createcredential(credentialname,password,email):
    new_account2 = Passwords(credentialname,password,email)
    return new_account2