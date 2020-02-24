import json
from Pack.DS.DataStructure import Dish, tags_map

def Select_Tag():
    num_map = {}
    idx = 1
    for key in tags_map:
        num_map[str(idx)] = key
        idx += 1
    # Show prompte
    print('選擇你要的標籤, 請輸入數字')
    # Show tags
    for key, value in num_map.items():
        print(int(key), tags_map[value])
    
    d_tags = input('標籤分類:').split(' ')
    
    return [num_map[t] for t in d_tags]

def Get_Menu(f_name='..\\..\\menu.txt'):
    return [Dish(*dish) for dish in json.load(open(f_name,'r'))]
    

if __name__ == '__main__':
    # Debug
    print(Select_Tag())
    
    for dish in Get_Menu():
        print(dish)