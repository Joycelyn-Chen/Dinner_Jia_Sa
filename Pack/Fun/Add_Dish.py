import json
from Pack.DS.DataStructure import Dish
from Pack.Fun.common import Select_Tag


def Add_Dish(Dish_ID, f_name):
    d_name = input('菜名:')
    r_name = input('餐廳:')
    d_tags = Select_Tag()
    
    #Create dish
    add = Dish(Dish_ID, d_name, r_name, d_tags)
    
    #Read menu
    file = open(f_name, 'r')
    menu = json.load(file)
    file.close()
    #Add dish
    menu.append(add.getAllAttrs())
    #Update menu
    file = open(f_name,'w')
    json.dump(menu,file)
    file.close()