# This file shows how to loop through an array in Python.

# Here, we are defining our array.  It is a simple array with 4 integers 
my_array = [534, 837, 173, 637]

# Here, we are looping through the array above
for j in my_array:
    
    # j represents the current item in the array that we are at in the loop
    # therefore, j represents a single integer value.
    # Here, we are checking whether j is less than 600, and if it is, we 
    # print the value of j to the terminal
    if j < 600:
        print(j)
    # If j is 600 or greater, we print a simple string value.
    else: 
        print("not printing")
