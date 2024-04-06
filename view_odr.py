
"""
    This module is related to addition of hte new order to the 
"""




def view_order():  
    print("Select to enter 1 order id \n 2 Customer name \n 3 Date")
    update_input = int (input ())
    if update_input >= 1 and update_input <= 3 : 
        if update_input == 1 :
            print("enter the order id")
            u_input1 = int(input())
        
        elif update_input == 2 :
            print("enter the customer name")
            u_input2 = str(input())
        
        else:
            print(" enter the date DDMMYYYY")
            u_input3 = int(input())
    else:
        print("enter correct value")
    
    
    
    """
    
    
    View details of the order by respective item detail
    
    
    
    """