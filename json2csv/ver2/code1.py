# Python program to convert 
# JSON file to CSV 

import json 
import csv 

# Opening JSON & loading the data into variable data 
with open('data.json') as json_file: 
	data = json.load(json_file) 

# now we will open a file for writing 
data_file = open('data_file.csv', 'w') 

# create the csv writer object 
csv_writer = csv.writer(data_file)

key_list = list(data.keys())

for item in key_list:
    if item != "timing":
        csv_writer.writerow(data[item])
    else:
        for val in data[item]:
            for sub_val in val.values():
                for req in sub_val:
                    for req_val in req.values():
                        csv_writer.writerow(req_val.values())

#print("\n".join(key_list))

#employee_data = data['emp_details'] 
#time_data = data['timing'] 

#csv_writer.writerow(name_data)

#for emp in time_data: 
#    #csv_writer.writerow(emp.values()) 
#    csv_writer.writerow(emp.keys()) 

data_file.close() 

