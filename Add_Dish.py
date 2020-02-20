from DataStructure import Dish, tags_map
import json

def Select_Tag():
    num_map = {}
    idx = 1
    for key in tags_map:
        num_map[str(idx)] = key
        idx += 1
    # Show tags
    for key, value in num_map.items():
        print(int(key), tags_map[value])
    
    d_tags = input('標籤分類:').split(' ')
    
    return [num_map[t] for t in d_tags]

def Add_Dish(Dish_ID):
    d_name = input('菜名:')
    r_name = input('餐廳:')
    d_tags = Select_Tag()
    
    #Create dish
    add = Dish(Dish_ID, d_name, r_name, d_tags)
    
    #Read menu
    file = open('menu.txt', 'r', encoding='UTF-8')
    menu = json.load(file)
    file.close()
    #Add dish
    menu.append(add.getAllAttrs())
    #Update menu
    file = open('menu.txt','w')
    json.dump(menu,file)
    file.close()

