from DataStructure import tags_map, Dish
import json

#Read data from file using json


#Initiallize data
dish1 = Dish(*[1, 'Steak', 'Joy kitchen', ['main04']])
dish2 = Dish(*[2, 'Steamed dumpling', 'Joy kitchen', ['main03']])

#Create the menu
menu = []
menu.append(dish1.getAllAttrs())
menu.append(dish2.getAllAttrs())


filename = "menu.txt"
#Write into the file
json.dump(menu, open(filename, 'w'))



#Testing data for input tags
input_tags = ['main04', 'main03']



def Pick_Dish(input_tags):

	#Read from file
	menu_s = json.load(open(filename, 'r'))

	#Transfer list to Dish
	menu = []
	for elem in menu_s:
		menu.append(Dish(*elem))

	#Show result
	for d in menu:
		print(d)

	#Store all output into a huge list
	Output_List = []

	for i in range(len(data)):
		for j in range(len(input_tags)):			#run through every data 
			if hasTag(data[i], input_tags[j]):
				Output_List.append(data[i])
				break

	#To see if output list stores the correct data
	#Need to be deleted when successfully merged
	for i in range(len(Output_List)):
		print(Output_List[i])

	return Output_List



