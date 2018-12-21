# This is a Python comment.  If I place the hashtag at the beginning of the line, the Python interpreter will ignore it!

# This is a function.  It takes an array as an argument.
def sort_clothes(items_array):
    # This is the main part of our program.  We are 'looping' through each item in our items_in_room array and logically deciding where to put them
    for item in items_array:
        
        # If the value of the item's 'type' property is clothing, we want to put that item in the dresser
        if item["type"] is "clothing":
            print("I put the " + item["description"] + " in my dresser!")
        
        # If the value of th item's 'type' property is not clothing, this means that it must be trash so we can throw it in the trash
        else:
            print("I threw the " + item["description"] + " in the trash can!")

# This is a simple string variable that stores the name of our program
name_of_this_program = "clean-room.py"


# Item 1, 2, and 3 are all called 'objects'.  Each object has a type property and a description property
item1 = {
    "type": "clothing",
    "description": "hoodie"
}

item2 = {
    "type": "clothing",
    "description": "t-shirt"
}

item3 = {
    "type": "trash",
    "description": "orange peel"
}

# This is an array.  An array stores a list of variables, objects, other arrays, etc.
# We need to put the items in this array so we can loop through them and sort the items in the room!
items_in_room = [item1, item2, item3]


# A simple Python print statement that will print out the name of the program
# notice the + sign.  This combines two strings together!
print ("Program: " + name_of_this_program)
print("----------------------------------------")
sort_clothes(items_in_room)
    