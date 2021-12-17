from locations.areas import Areas_location
from locations.start import Start_location

location_list = {
    "start": Start_location,
    "Areas": Areas_location,
    "tavern": Start_location,
    "church": Start_location,
    "gallows": Start_location,
    "quarter a": Start_location,
    "quarter b": Start_location,
    "apothecary": Start_location,
    "unknown road": Start_location
}

def get_start_zone(reader, writer):
    return Start_location(reader, writer, get_location_by_name, {})

def get_location_by_name(location_name):
    return location_list[location_name]