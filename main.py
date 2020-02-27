# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:31:28 2020

@author: 劉又聖
"""

import os, sys
from Pack.Fun.Add_Dish  import Add_Dish
from Pack.Fun.Pick_Dish import Pick_Dish
from Pack.Fun.common    import Get_Menu, Show_Menu

def main():
    prompt = 'input 1 for Add Dish, 2 for Pick Dish, ' \
             '3 for Modify Dish, 4 for Delete Dish, ' \
             '5 for Show All Dish, Q for leave.\n>> '
    f_name = 'menu.txt'
    menu   = Get_Menu(f_name)
    ID     = 1 if not len(menu) else max([x.getID() for x in menu]) + 1
             
    while True:
        choice = input(prompt)
        
        if   choice == '1':
            Add_Dish(ID, f_name)
            ID += 1
        elif choice == '2':
            result = Pick_Dish(f_name)
            if result:
                for dish in result:
                    print(dish)
            else:
                print('No result')            
        elif choice == '3':
            #Modify_Dish()
            pass
        elif choice == '4':
            #Delete_Dish()
            pass
        elif choice == '5':
            Show_Menu(f_name)
        elif choice == 'Q':
            break
        else:
            print(f'No {choice} this option')

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    main()