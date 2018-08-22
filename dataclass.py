class Account:
    account_list = []
    def __init__(self,firstname,lastname,email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def saveaccount(self):
        Account.account_list.append(self)

class Passwords:
    password_list = []
    def __init__(self,password,email,credentialtype):
        self.password = password
        self.email = email
        self.credentialtype = credentialtype

    def savepassword(self):
        Passwords.password_list.append(self)

    @classmethod
    def find_by_credential(cls,credential):
        for Passwords in cls.password_list:
                if Passwords.credentialtype == credential:
                    return credential                  
            