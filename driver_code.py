import Credit_Card_Validator as cr

if __name__ == '__main__':
    card_number = (input("Enter Card No in format (XXXX-XXXX or XXXX XXXX or XXXXXXXX) :"))

    if " " in card_number:
        card_number = int(card_number.replace(" ",""))
    elif "-" in card_number:
        card_number = int(card_number.replace("-",""))
    
    

    card = cr.CreditCard.set_card(card_number)
    print(card.company)
    print('Card : ', card.card_no)
    print(card.first_check())
    print(card.checksum)
    print(card.validate())

    

# 4388 5760 1840 2626
# 4388576018402626
# 379354508162306
# 5300202020302098