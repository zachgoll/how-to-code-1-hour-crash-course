# This file is just an example that I show in the video on looping through large
# datasets.  Some of the code in this file is more advanced than this course
# is meant to be, so if you do not understand what is going on, that is okay.

# Importing a Python library to help us work with the csv file
import csv

# Initialize a "counter" variable that will eventually store the number
# of shoppers in the data set that match our conditions below.
num_of_target_shoppers = 0

# Opens our large data file that is in the same directory as this file.
with open('./large-data.csv') as csv_file:
    
    # Here we are using the external csv Python library that we imported at
    # the top of the file to convert our large data file into a bunch of 
    # arrays with different attributes.
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    # LOOPING through data 
    for row in csv_reader:
        
        # skip the first line.
        if line_count == 0:
            line_count += 1
        else:
            
            # If the current line of the data file represents a shopper that is a male 
            # between the ages of 36 and 45, we will "increment" the counter variable
            # we defined at the top of the file and then go to the next line
            if row[2] == "M" and row[3] == "36-45":
                num_of_target_shoppers += 1
            line_count += 1
            
    # These next two lines are not in the loop.  They will be read by Python
    # when Python is done looping through every line in the data file.
    # Once we get here, we know that the num_of_target_shoppers variable will
    # reflect the total number of male shoppers aged 36-45
    print("processed all lines")
    
    # In this print statement, notice how we have our variable passed in as an 
    # argument to the str() function.  This function is built in to the Python
    # coding language and will "typecast" or convert an integer into a string
    # so that we can combine everything into one line of output.
    print("Number of male shoppers aged 36-45 is " + str(num_of_target_shoppers))