import csv

def write(name, columns):
    """Write the header of a file with the values of the arguments"""
    with open(f".\\information\\{name}.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

def append(name, values):
    """Appends the values to a file with the name argument"""
    with open(f".\\information\\{name}.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(values)

    print("Hecho")

def read(name):
    """Read the file with the name argument"""
    info = []
    with open(f".\\information\\{name}.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            info.append(row)
        return info      

all_hotels = read("hotels")
all_rooms = read("rooms")
all_passengers = read("passengers")

def infoHotel(hotel_id):
    index = 0
    for hotel in all_hotels:
        if hotel["ID_Hotel"] == hotel_id:
            return hotel
        elif index == len(all_hotels) - 1:
            return "Error"
        else:
            index += 1

def searchRooms(hotel_id):
    index = 0
    hotel_rooms = []
    for room in all_rooms:
        if room["ID_Hotel"] == hotel_id:
            hotel_rooms.append([room["ID_Room"], room["Type"], room["Number"], room["Price"], room["Status"]])
        elif index == len(all_rooms) - 1:
            return "Error"
        else:
            index += 1
    return hotel_rooms


def searchPassengers(bus_num):
    index = 0
    passengers = []
    for passenger in all_passengers:
        if passenger["Bus_Number"] == bus_num:
            passengers.append([passenger["Name"], passenger["Bus_Number"], passenger["Room_Number"]])
        elif index == len(all_passengers) - 1:
            return "Error"
        else:
            index += 1
    return passengers
