from DataStructure import tags_map, Dish
import json


def Pick_Dish(input_tags):

	#Read from file
	menu_s = json.load(open(filename, 'r'))

	#Transfer list to Dish
	menu = []
	for elem in menu_s:
		menu.append(Dish(*elem))

	input_tags = Select_tag()
	#Store all output into a huge list
	Output_List = []

	for dish in menu:
		for tag in input_tags:
			if dish.hastag(tag):
				Output_List.append(dish)
	return Output_List



