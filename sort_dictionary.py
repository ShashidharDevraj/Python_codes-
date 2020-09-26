# Sort the Dictonary items based on the values given. 

#Input
data = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14}, 
        'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2}, 
        'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}} 

# Expected Output
# data = {'Nikhil': {'Maths': 2, 'English': 5, 'Science': 14},
# 		    'Akash': {'Science': 2, 'Maths': 7, 'English': 15},
# 		    'Akshat': {'English': 5, 'Science': 20, 'Maths': 50}}


for key, value in data.items():
	key_list = list(data[key].keys())
	value_list = list(data[key].values())
	sorted_value_list = sorted(value_list)

	new_data = {}
	for i in sorted_value_list:
		new_data[key_list[value_list.index(i)]] = i
		data[key] = new_data

print(data)
