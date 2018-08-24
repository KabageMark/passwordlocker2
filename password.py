from dataclass import Account,Passwords
import hashlib

def createaccount(firstname,lastname,email):
    new_account = Account(firstname,lastname,email)
    return new_account
    
def saveaccount(account):
     account.saveaccount()    

def createcredential(credentialname,password,email):
    new_account2 =Passwords(credentialname,password,email)
    return new_account2

def savecredential(password):
     password.savepassword()

def check_existing_password(credentialname):
    return Passwords.find_by_credential(credentialname)         

def getcredential(credentialname):
    return Passwords.find_by_credential(credentialname)

def main():
    print("Hello Welcome to your password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    print("Use these short codes : , ca - create account, ex -exit application")
    while True:
                    # print("Use these short codes : lg - log in account, cr - create credential, fp -find a password, ex -log out")
                    
                    short_code = input().lower()
                    if short_code == 'ca':
                            print("Create Account")
                            print("-"*10)

                            print ("Firstname ....")
                            firstname = input()

                            print("Last name ...")
                            lastname = input()

                            print("email ...")
                            email = input()

                            saveaccount(createaccount(firstname,lastname,email)) 
                            print ('\n')
                            print(f"Account{firstname} {lastname} has been created")
                            print("Use these short codes : lg - log in account,ex -exit the application")
                            print ('\n')
                    
                    

                    if short_code == "ex":
                            print("You are logged out .......")
                            break


                    if short_code == 'lg':
                            print("Log in")
                            print("-"*10)

                            print ("Firstname ....")
                            firstname = input()

                            print("Last name ...")
                            lastname = input()

                            print("email ...")
                            email = input()

                            saveaccount(createaccount(firstname,lastname,email)) 
                            print ('\n')
                            print(f"logged in as {firstname} {lastname}")
                            print("Use these short codes : cr - create credential, fp -find a password, ex -log out")        
                            print ('\n')
                    

                    if short_code == 'cr':
                            print("New credential")
                            print("-"*10)

                            print ("Account name ....")
                            credentialname = input()

                            print("Password ...")
                            password = input()

                            print("email ...")
                            email = input()

                            savecredential(createcredential(credentialname,password,email)) 
                            print ('\n')
                            print(f"New Password {credentialname} {password} created")
                            print("Use these short codes :cr - create credential, fp -find a password, ex -log out") 
                            print ('\n')
                                  
                    
                    if short_code == 'fp':

                            print("Enter the name of credential you want to search for?")

                            search_credential = input()
                            if check_existing_password(search_credential):
                                    check_credential = getcredential(search_credential)
                                    print(f"{check_credential.credentialname} {check_credential.password}")
                                    print('-' * 20)

                                    print(f"Credential.......{check_credential.credentialname}")
                                    print(f"password.......{check_credential.email}")
                            else:
                                    print("That credential does not exist")
                                    print("Use these short codes :cr - create credential, fp -find a password, ex -log out") 
                                    print ('\n')
                    
                    if short_code == "ex":
                            print("You are now logged out .......")
                            break

if __name__ == '__main__':

    main()
