# Python program to convert JSON file to CSV 
import json 
import csv 

# Opening JSON & loading the data into variable data 
with open('data.json') as json_file: 
	data = json.load(json_file) 

# now we will open a file for writing 
data_file = open('data_file.csv', 'w') 
csv_writer = csv.writer(data_file)

key_list = list(data.keys())

for item in key_list:
    if item != "timing":
        csv_writer.writerow(data[item])

time_data = data['timing'] 

for item in time_data:
    temp = list(item.keys())
    for val in temp:
        print(item[val])

#print("\n".join(key_list))
#csv_writer.writerow(name_data)
#for emp in time_data: 
#    csv_writer.writerow(emp.keys()) 

data_file.close() 
