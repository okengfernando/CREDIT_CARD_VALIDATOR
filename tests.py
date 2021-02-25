import unittest
import Credit_Card_Validator as cr

class Testing_Credit_Card_Methods(unittest.TestCase):

    def test_sample(self):
        pass

    def test_length_of_the_credit_card_digits(self):
        self.assertTrue(cr.CreditCard(4388576018402626).first_check() == "First check : Valid in terms of length.")
        self.assertFalse(cr.CreditCard(12245678349).first_check() == "First check : Valid in terms of length.")
        self.assertFalse(cr.CreditCard(122456783412).first_check() == "First check : Valid in terms of length.")
    
    def test_







if __name__ == '__main__':
    unittest.main()