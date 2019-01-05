# This is how we write a comment in python
# Packages will be sorted into zones
# International packages go to Zone A
# Domestic packages over 3 pounds go to Zone B
# Domestic packages equal or less than 3 pounds go to Zone C
# Any package over 40 pounds goes to Zone D
# Once in Zone, packages sorted by shipping carrier where DHL is vehicle 1, Fedex is vehicle 2, and UPS is vehicle 3

# We are defining four items to ship.  These are called "objects", and 
# each object has 3 "properties" - a weight, international, and carrier 
# property that are of type integer, boolean, and string respectively.
item1 = {
    "weight": 2,
    "international": False,
    "carrier": "Fedex"
}

item2 = {
    "weight": 20,
    "international": True,
    "carrier": "Fedex"
}

item3 = {
    "weight": 5,
    "international": True,
    "carrier": "DHL"
}

item4 = {
    "weight": 50,
    "international": False,
    "carrier": "UPS"
}

# We have defined and stored the data for 4 items above, and now we need
# to place these four items in an array so we can later loop through each
# item
items_to_ship = [item1, item2, item3, item4]

# Our first function will take a single item object as an argument, and then 
# based on carrier property of the item will decide which truck to place
# the item in 
def get_carrier(item):
    if item["carrier"] == "DHL":
        return "Vehicle 1"
    elif item["carrier"] == "Fedex":
        return "Vehicle 2"
    else:
        return "Vehicle 3"
    
# Our second function will also take a single item object as an argument and 
# will determine based on the item's weight and international properties which
# zone to assign the package to.
def get_zone(item):
    if item["international"]:
        return "Zone A"
    elif item["weight"] > 3 and item["weight"] <= 50 and item["international"] == False:
        return "Zone B"
    elif item["weight"] <= 3 and item["international"] == False:
        return "Zone C"
    else:
        return "Zone D"
        
# Our final function is the master function that will combine the previous two functions.
# In this function, we loop through each item, get that item's zone and carrier, and 
# then print out the zone and carrier.
def sort_packages(items):
    for item in items:
        zone = get_zone(item)
        carrier = get_carrier(item)
        print(zone + ", " + carrier)

# Here, we are calling our main function and passing our items_to_ship array as 
# an argument to this function.  If you think about it, we are calling all three 
# of our functions here.  The sort_packages() function will call both the get_carrier()
# and get_zone() functions.
sort_packages(items_to_ship)
        
