from datetime import datetime
import pandas as pd
import logging
import regex as rg

import add_odr
import view_odr
import update_odr
import save_excel

"""
pip install pandas
Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
Successfully installed numpy-1.26.4 pandas-2.2.1 python-dateutil-2.9.0.post0 pytz-2024.1 six-1.16.0 tzdata-2024.1

"""

def order_menu():
    print("Enter the correct choice \n 1: Add an order \n 2: View an odrer \n 3: Update an order \n 4: Save to excel ")
    order_menu1 = int(input())
    if order_menu1 >= 1 and order_menu1 <= 4 :
        if order_menu1 == 1 :
            add_order()
        elif order_menu1 == 2:
            view_order()
        elif order_menu1 == 3 :
            update_order()
        else :
            save_to_excel()
    else:
        print("enter a correct value")
        

  

def main():
    order_menu()




if __name__ ==" __main__" :
    try:
        main()
    except Exception as ex:
        print("there is an error : \n", ex)
    else:
        print("Code sucessful")