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

def get_carrier(item):
    if item["carrier"] == "DHL":
        return "Vehicle 1"
    elif item["carrier"] == "Fedex":
        return "Vehicle 2"
    else:
        return "Vehicle 3"
    
def get_zone(item):
    if item["international"]:
        return "Zone A"
    elif item["weight"] > 3 and item["weight"] <= 50 and item["international"] == False:
        return "Zone B"
    elif item["weight"] <= 3 and item["international"] == False:
        return "Zone C"
    else:
        return "Zone D"
        
def sort_packages(items):
    for item in items:
        zone = get_zone(item)
        carrier = get_carrier(item)
        print(zone + ", " + carrier)

sort_packages(items_to_ship)
        
