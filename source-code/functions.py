# Packages will be sorted into zones
# International packages go to Zone A
# Domestic packages over 3 pounds go to Zone B
# Domestic packages equal or less than 3 pounds go to Zone C
# Any package over 40 pounds goes to Zone D
# Once in Zone, packages sorted by shipping carrier

def sort_packages():
    
    zone = ""
    vehicle = ""
    
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
                return "Zone A, DHL"
            elif item["carrier"] == "Fedex":
                return "Zone A, Fedex"
            else
                return "Zone A, UPS"
        elif item["weight"] > 3 and item["weight"] <= 50 and item["international"] == False:
            if item["carrier"] == "DHL":
                return "Zone B, DHL"
            elif item["carrier"] == "Fedex":
                return "Zone B, Fedex"
            else
                return "Zone B, UPS"
        elif item["weight"] <= 3 and item["international"] == False:
            if item["carrier"] == "DHL":
                return "Zone C, DHL"
            elif item["carrier"] == "Fedex":
                return "Zone C, Fedex"
            else
                return "Zone C, UPS"
        else
            if item["carrier"] == "DHL":
                return "Zone D, DHL"
            elif item["carrier"] == "Fedex":
                return "Zone D, Fedex"
            else
                return "Zone D, UPS"
        
    