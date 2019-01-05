/*
You can write a multi-line comment in C with this syntax.

This file is meant to demonstrate how you would create the objects
that are in the clean-room.py file in the C language.

Scroll through to find comments on each line.
*/


// This is another way to write a C comment, but it is only a single-line comment
// Below are two "include" statements.  The reason we need these at the top of 
// this file is so we can use some of the C standard library functions
// For example, stdio.h has the printf() function that we use to print output
// to the terminal
#include <stdio.h>
#include <string.h>

// No need to understand structs yet.  If you take CS50, you will 
// be introduced to them.  They are essentially a custom object.
struct Item {
	char* type;
	char* description;
};

// Every C program needs a "main" function in order to execute it.
int main()
{
	// Here we are using our struct declaration above to create 3 
	// item objects and then place those item objects in an array
	struct Item item1;
	struct Item item2;
	struct Item item3;
	struct Item items_in_room[3];

	// Here, we are assigning values to the "type" property of the Item struct
	item1.type = "clothing";
	item2.type = "clothing";
	item3.type = "trash";

	// Here, we are assigning values to the "description" property of the Item struct
	item1.description = "hoodie";
	item2.description = "t-shirt";
	item3.description = "orange peel";

	items_in_room[0] = item1;
	items_in_room[1] = item2;
	items_in_room[2] = item3;
	
	// This is a loop.  We are looping through each Struct object 
	// and printing the type and description properties to the terminal
	// with the C standard library printf() function
	int i;
	for (i = 0; i < 3; i++) {
		printf("Item %d Type: %s\tDescription: %s\n", i+1, items_in_room[i].type, items_in_room[i].description);	
	}
	
	// Every C program must return something, so we return 0, which 
	// indicates that everything went okay.
	return 0;
}