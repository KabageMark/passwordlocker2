from dataclass import Account,Passwords
import pyperclip
import unittest
class testContact(unittest.TestCase):
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_account = Account("Mark","Chege","kabagemark@gmail.com") # create account object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.firstname,"Mark")
        self.assertEqual(self.new_account.lastname,"Chege")
        self.assertEqual(self.new_account.email,"kabagemark@gmail.com")


    def test_save_Account(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the contact list
        '''
        self.new_account.saveaccount() # saving the new contact
        self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Account.account_list = []    
    
    def test_save_multiple_Account(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the contact list
        '''
        self.new_account.saveaccount() # saving the new contact
        test_account = Account("Test","user","test@user.com") # new contact
        test_account.saveaccount()
        self.assertEqual(len(Account.account_list),2)

    def test_find_by_credential(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the contact list
        '''
        self.new_password.savepassword() 
        test_password = Passwords("konshens","kabagemark@gmail.com","facebook") # new contact
        test_password.savepassword()

        found_credential =  Passwords.find_by_credential("facebook")

        self.assertEqual(found_credential.password , test_password.email) 
         

if __name__ == '__main__':
    unittest.main() 