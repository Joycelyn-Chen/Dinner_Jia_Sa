from DataStructure import Dish
import json

def Add_Dish(Dish_ID):
    d_name = input('菜名:')
    r_name = input('餐廳:')
    d_tags = input('標籤分類:').split(' ')

    add = Dish(Dish_ID, d_name, r_name, d_tags)

    file = open('menu.txt','r')
    menu = json.load(file)
    file.close()

    menu.append(add.getALLAttrs())

    file = open('menu.txt','w')
    json.dump(menu,file)
    file.close()

    
