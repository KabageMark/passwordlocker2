from dataclass import Account
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
    

if __name__ == '__main__':
    unittest.main() 