from Pack.Fun.common import Get_Menu, Select_Tag

def Pick_Dish(f_name):
    menu       = Get_Menu(f_name)
    input_tags = Select_Tag()
    
    #Store all output into a huge list
    output_list = []
    
    for dish in menu:
        for tag in input_tags:
            if dish.hasTag(tag):
                output_list.append(dish)
    
    return output_list