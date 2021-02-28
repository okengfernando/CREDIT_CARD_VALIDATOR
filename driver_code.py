import Credit_Card_Validator as cr

def pre_process(card_number):
    '''
    This Method removes spaces and hyphens so as to put it
    in a proprer int format
    '''
    if " " in card_number:
        card_number = int(card_number.replace(" ",""))
    elif "-" in card_number:
        card_number = int(card_number.replace("-",""))
    
    return card_number





if __name__ == '__main__':
    card_number = (input("Enter Card No in format (XXXX-XXXX or XXXX XXXX or XXXXXXXX) :"))
       
    x = pre_process(card_number)
    
    
    card = cr.CreditCard.set_card(x)
    print(card.company)
    print('Card : ', card.card_no)
    print(card.first_check())
    print(card.checksum)
    print(card.validate())



    

# 4388 5760 1840 2626
# 4388576018402626
# 379354508162306
# 5300202020302098