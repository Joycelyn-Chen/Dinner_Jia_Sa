# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:39:22 2020

@author: 劉又聖
"""
from Pack.Fun.Pick_Dish import Pick_Dish
from Pack.Fun.common import Get_Menu
import json

def _List_Dish(mode, f_name):
    """
    Input,  mode,   為列出選擇類型
    Output, result, 為該次列出的所有菜色，方便後續刪除，需要在這邊回傳
    """
    func = {
        '1' : Get_Menu,    # 列出全部
        '2' : Pick_Dish,   # 列出部分，透過標籤篩選
    }
    
    idx    = 0
    result = func.get(mode, lambda:-1)(f_name)
    
    # 使用者輸入 1、2 以外的東西，回傳 -1 表示錯誤輸入
    # 否則應該回傳 list
    if result != -1:
        for dish in result:
            print(str(idx)+'.', dish)
            idx += 1
    
    return result


def _Del_Dish(f_name, menu, ID_list):
    """
    Input:
        menu is a list of all dish(Dish instance)
        ID_list is a list of dish ID which all needs to pop
    """
    for ID in ID_list:
        for dish in menu:
            if ID == dish.getID():
                menu.pop(menu.index(dish))
                break
    
    fp = open(f_name, 'w')
    json.dump([d.getAllAttrs() for d in menu], fp)
    fp.close()
    return True

def Delete_Dish(f_name):
    # 取得輸入，選擇列出類型(列出全部、使用標籤選擇)
    prompt = 'Input 1 for listing all dish to select, ' \
             '2 for listing dish by tags to select.\n>> '
    choice = input(prompt)
    
    listed_item = _List_Dish(choice, f_name)  # 列出可選選項
    
    if listed_item == -1:
        print(f'No {choice} this option')
        return False
    
    # 列出選擇後，取得使用者輸入，輸入為哪幾項需要刪除
    # 使用者輸入的是我們列出的index不等於dish的ID，需要轉換
    prompt   = 'Choose dish you want to delete.\n>> '
    idx_list = list( map(int, input(prompt).split(' ')) )
    ID_list  = [ listed_item[idx].getID() for idx in idx_list ]
    
    # 執行刪除動作
    _Del_Dish(f_name, Get_Menu(f_name), ID_list) 
    return True