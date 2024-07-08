from flask import Flask, request, jsonify
import read_write

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret_key'

@app.route("/hotels", methods=['GET'])
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

if __name__ == "__main__":
    app.run()