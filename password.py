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

def savecredential(password):
     password.savepassword()     

def getcredential(credentialname):
    return Passwords.find_by_credential(credentialname)

def main():
    print("Hello Welcome to your password list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    print("Use these short codes : , ca - create account, ex -exit application")

if _name_ == 'name'
   main()       