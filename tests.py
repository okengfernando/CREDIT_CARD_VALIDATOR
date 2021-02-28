import unittest
import Credit_Card_Validator as cr
import driver_code as dr

class Testing_Credit_Card_Methods(unittest.TestCase):

    def test_sample(self):
        pass
    
    def test_if_VALID_removal_of_symbols_and_spaces(self):
        self.assertEqual(dr.pre_process('3000-2300-1235-678') , 300023001235678)
        self.assertEqual(dr.pre_process('3000 2300 1235 678') , 300023001235678)
        self.assertEqual(dr.pre_process('3000 23001235 678') , 300023001235678)

    def test_INVALID_removal_of_symbols_and_white_spaces(self):
        self.assertFalse(dr.pre_process('3000=2300+1235+678') == 300023001235678)
        self.assertFalse(dr.pre_process('3000&23001235&678') == 300023001235678)
        

    def test_VALID_length_of_the_credit_card_digits(self):
        self.assertTrue(cr.CreditCard(4388576018402626).first_check() == "PASSED First check : Valid in terms of length.")
        self.assertTrue(cr.CreditCard(340000000000009).first_check() == "PASSED First check : Valid in terms of length.")
       
    
    def test_AN_INVALID_length_of_the_credit_card_digits(self):
        self.assertFalse(cr.CreditCard(12245678349).first_check() == "PASSED First check : Valid in terms of length.")
        self.assertFalse(cr.CreditCard(122456783412).first_check() == "PASSED First check : Valid in terms of length.")

    def test_IF_A_VALID_credit_card_is_entered(self):
        self.assertEqual(cr.CreditCard(4111111111111111).validate() ,'Valid Card')
        self.assertEqual(cr.CreditCard(5500000000000004).validate(),'Valid Card')
        self.assertEqual(cr.CreditCard(340000000000009).validate(),'Valid Card')
        self.assertEqual(cr.CreditCard(4300123456780987).validate() , 'Invalid Card')

    def test_IF_AN_INVALID_credit_card_is_entered(self):
        self.assertEqual(cr.CreditCard(4300123456780987).validate() , 'Invalid Card')
        self.assertEqual(cr.CreditCard(1319941220072011).validate() , 'Invalid Card')
    

if __name__ == '__main__':
    '''
    Nain code driver to run the above unnit tests
    '''
    unittest.main()