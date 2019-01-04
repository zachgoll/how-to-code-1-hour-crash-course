# Importing a Python library to help us work with the csv file
import csv

num_of_target_shoppers = 0

# Opens our large data file that is in the same directory as this file.
with open('./large-data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    # LOOPING through data 
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            #print(row)
            if row[2] == "M" and row[3] == "36-45":
                num_of_target_shoppers += 1
            line_count += 1
    print("processed all lines")
    print("Number of male shoppers aged 36-45 is " + str(num_of_target_shoppers))