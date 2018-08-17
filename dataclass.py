class Account:
    account_list = []
    def __init__(self,firstname,lastname,email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def saveaccount(self):
        Account.account_list.append(self)