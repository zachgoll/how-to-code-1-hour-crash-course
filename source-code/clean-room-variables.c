#include <stdio.h>
#include <string.h>

struct Item {
	char* type;
	char* description;
};

int main()
{
	struct Item item1;
	struct Item item2;
	struct Item item3;
	struct Item items_in_room[3];

	item1.type = "clothing";
	item2.type = "clothing";
	item3.type = "trash";

	item1.description = "hoodie";
	item2.description = "t-shirt";
	item3.description = "orange peel";

	items_in_room[0] = item1;
	items_in_room[1] = item2;
	items_in_room[2] = item3;
	
	int i;
	for (i = 0; i < 3; i++) {
		printf("Item %d Type: %s\tDescription: %s\n", i+1, items_in_room[i].type, items_in_room[i].description);	
	}
	return 0;
}