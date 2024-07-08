from flask import Flask, request, jsonify
import read_write

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "SECRET_KEY"

@app.route("/hotels", methods=["GET"])
def index():
    all_hotels = read_write.read("hotels")
    return jsonify(all_hotels)

@app.route("/hotel/<hotel_id>")
def hotel(hotel_id):
    hotel_info = read_write.infoHotel(hotel_id)
    return jsonify(hotel_info)

@app.route("/hotel/<hotel_id>/rooms")
def rooms(hotel_id):
    all_rooms = read_write.searchRooms(hotel_id)
    return jsonify(all_rooms)

@app.route("/hotel/bus/<bus_num>")
def seats(bus_num):
    all_passengers = read_write.searchPassengers(bus_num)
    return jsonify(all_passengers)

@app.route("/hotel/reservation", methods=["POST"])
def reservation():
    if request.method == "POST":
        data = request.json
        hotel_id = data.get("hotel_id")
        name = data.get("name")
        bus_number = data.get("bus_number")
        room_number = data.get("room_number")
        read_write.append("passengers", ["ID_Hotel","Name","Bus_Number","Room_Number"], [hotel_id, name, bus_number, room_number])
    return jsonify({"message": "Reserva realizada exitosamente"})

if __name__ == "__main__":
    app.run()