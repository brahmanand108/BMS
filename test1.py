print("Enter the correct choice \n 1: Add an order \n 2: View an odrer \n 3: Update an order \n 4: Save to excel ")
order_menu1 = int(input())
if order_menu1 >= 1 and order_menu1 <= 4 :
    if order_menu1 == 1 :
        print("add_order()")
    elif order_menu1 == 2:
        print("view_order()")
    elif order_menu1 == 3 :
        print("update_order()")
        
    else :
        print("save_to_excel()")
else:
    print("enter a correct value")