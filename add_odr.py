
"""
    This module is related to addition of hte new order to the 
"""


def add_order():
    print ("Enter your name")
    name = str (input())
    print (" Enter the comodity reqired 1 samosa \n 2 pastery \n 3 jalebi \n 4 xyz   ")
    order_type = int(input())
    if (order_type >= 1 and order_type <= 4) :
    
        if order_type == 1 :
            order_oject = "samosa"
        elif order_type == 2 :
            order_oject = "pastery"
        elif order_type == 3:
            order_oject = "jalebi"
        else:
            order_oject = "xyz"
    else:
        print("Enter the correct choice")
        
    """
    add details of the order by provided details by the customer
    """