# Packages will be sorted into zones
# International packages go to Zone A
# Domestic packages over 3 pounds go to Zone B
# Domestic packages equal or less than 3 pounds go to Zone C
# Any package over 40 pounds goes to Zone D
# Once in Zone, packages sorted by shipping carrier where DHL is vehicle 1, Fedex is vehicle 2, and UPS is vehicle 3

# Here we are defining one large and inefficient function.  This is NOT the correct
# way to write code.  Refer to the functions-correct.py file for the correct way 
# to write the code below.
def sort_packages():
    
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
    
    items_to_ship = [item1, item2, item3, item4]
    
    # Figure out Zone
    for item in items_to_ship:
        if item["international"] == True:
            if item["carrier"] == "DHL":
                print("Zone A, Vehicle 1")
            elif item["carrier"] == "Fedex":
                print("Zone A, Vehicle 2")
            else:
                print("Zone A, Vehicle 3")
        elif item["weight"] > 3 and item["weight"] <= 50 and item["international"] == False:
            if item["carrier"] == "DHL":
                print("Zone B, Vehicle 1")
            elif item["carrier"] == "Fedex":
                print("Zone B, Vehicle 2")
            else:
                print("Zone B, Vehicle 3")
        elif item["weight"] <= 3 and item["international"] == False:
            if item["carrier"] == "DHL":
                print("Zone C, Vehicle 1")
            elif item["carrier"] == "Fedex":
                print("Zone C, Vehicle 2")
            else:
                print("Zone C, Vehicle 3")
        else:
            if item["carrier"] == "DHL":
                print("Zone D, Vehicle 1")
            elif item["carrier"] == "Fedex":
                print("Zone D, Vehicle 2")
            else:
                print("Zone D, Vehicle 3")


sort_packages()