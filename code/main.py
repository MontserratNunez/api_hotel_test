import requests
from colorama import Fore, Style, init

init()
url = "http://127.0.0.1:5000"

def fetch(endpoint):
    """Collects the data from the api"""
    try:
        response = requests.get(url + endpoint, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data
        print(error("La opción ingresada no es válida"))
    except Exception:
        print(error("Error de conexion, inténtelo de nuevo"))

def hotels():
    """Shows all the names of all the hotels"""
    response = fetch("/hotels")
    if response:
        for r in response:
            print(f"=======================\nId del hotel: {r["ID_Hotel"]}\nNombre del hotel: {r["Name"]}\n=======================")

def hotel_info():
    """Shows the selected hotel info"""
    while True:
        hotel_id = input("1. Ingrese el id de un hotel: \n2. O escriba 'volver' o 'v' para volver atrás: ")
        if hotel_id in ("volver", "v"):
            break
        response = fetch(f"/hotel/{hotel_id}")
        if response and response != "Error":
            print(f"=======================\nId del hotel: {response["ID_Hotel"]}\nNombre del hotel: {response["Name"]}\nDirección: {response["Adress"]}\nTeléfono: {response["Phone"]}\n=======================") #
        else:
            print(error("El id ingresado no corresponde a ningún hotel"))
            break

def room_info():
    """Shows the rooms that the selected hotel have"""
    while True:
        print("Escriba 'volver' o 'v' para volver atrás.")
        hotel_id = input(dialog("1. Ingrese el id de un hotel."))
        if hotel_id in ("volver", "v"):
            break
        response = fetch(f"/hotel/{hotel_id}/rooms")
        if response and response != "Error":
            for r in response:
                print(f"=======================\nNúmero de habitación: {r[2]}\nTipo de habitación: {r[1]}\nDisponibilidad: {r[4]}\nPrecio: {r[3]}\n=======================")
        else: 
            print(error("El id ingresado no corresponde a ningún hotel"))
            break

def reserve():
    """Allows the user to make a reservation"""
    hotel_id = input(dialog("1. Ingrese el id de un hotel: "))
    while True:
        room = input(dialog("2. Ingresa el numero de la habitación: "))
        if is_available(room, hotel_id):
            break
        print(error("La habitación seleccionada no esta disponible"))
    names = []
    passengers_num = input(dialog("3. Cantidad de pasajeros: "))
    print("Ingrese el nombre y apellido de cada pasajero.")
    for i in range(passengers_num):
        name = input("1. ")
        names.append(name)
    print(dialog("4. Seleccione un autobús."))
    while True:
        bus = input("Lista de autobuses disponibles:\n[2], [6], [8], [9], [11], [12] [13], [14], [20], [23]\n")
        if bus in ("2", "6", "8", "9", "11", "12", "13", "14", "20", "23"):
            break
        print(error("El autobús elegido no se encuentra disponible"))
    print("6. Confirme su reserva.")
    while True:
        print("Datos de reserva:")
        print(f"ID del hotel: {hotel_id}")
        print(f"Número de habitación: {room}")
        print(f"Pasajeros: {names}")
        print(f"Número de autobús: {bus}")
        reserva = input(dialog("¿Es correcto? [si/no] "))
        if reserva == "si":
            send_reservation(hotel_id, names, room , bus)
            break
        elif reserva == "no":
            print(dialog("Reserva cancelada"))
            break
        else:
            print(error("La opción ingresada no es válida"))

def send_reservation(hotel_id, names, room, bus):
    """Send the data of the reservation to store it"""
    try:
        for name in names:
            endpoint = '/hotel/reservation'
            body = {
                "hotel_id": hotel_id,
                "name": name,
                "bus_number": bus,
                "room_number": room
            }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url + endpoint, json=body, headers=headers, timeout=10)
            if response.status_code == 200:
                print(dialog("Reserva enviada exitosamente"))
    except Exception:
        print("Error al enviar la reserva")

def passengers_info():
    """Shows the passengers information from the selected bus"""
    while True:
        bus_num = input("1. Ingrese el numero de un autobús: \n2. O escriba 'volver' o 'v' para volver atrás ")
        if bus_num in ("volver", "v"):
            break
        response = fetch(f"/hotel/bus/{bus_num}")
        if response and response != "Error":
            for r in response:
                print("=========================")
                print(f"Nombre: {r[0]}")
                print(f"Número de autobús: {r[1]}")
                print(f"Número de habitación: {r[2]}")
                print("=========================")
        else:
            print(error("No se han encontrado pasajeros para el autobús seleccionado"))

def details():
    """Shows the details of the stay"""
    while True:
        hotel_id = input("1. Ingrese el ID del hotel: ")
        room = input("2. Ingrese el número de habitación: ")
        if room in ("volver", "v"):
            break

def do_checkout():
    """Allows the user to checkout"""
    hotel_id = input("1. Ingrese el ID del hotel: ")
    room = input("2. Ingrese el número de habitación: ")
    confirm = input("Confirmar checkout [si/no]: ")
    while True:
        if confirm == "si":
            endpoint = "/hotel/checkout"
            body = {
                "hotel_id": hotel_id,
                "room_number": room
            }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url + endpoint, json=body, headers=headers, timeout=10)
            if response.status_code == 200:
                print(dialog("Checkout enviado exitosamente"))
            break
        elif confirm == "no":
            break
        else:
            print(error("La opción ingresada no es válida"))

def is_available(room_num, hotel_id):
    """Checks if the room is available"""
    rooms = fetch(f"/hotel/{hotel_id}/rooms")
    for room in rooms:
        if room[2] == room_num and room[4] == "Disponible":
            return True
    return False

def error(error_message):
    """Retorns a red string"""
    return f"{Fore.RED}{error_message}{Style.RESET_ALL}"

def dialog(dialog_message):
    """Retorns a yellow string"""
    return f"{Fore.YELLOW}{dialog_message}{Style.RESET_ALL}"

def highlight(highlight_message):
    """Retorns a yellow string"""
    return f"{Fore.CYAN}{highlight_message}{Style.RESET_ALL}"

if __name__ == "__main__":
    while True:
        print("=====================================================")
        print(highlight("Bienvenido a Planea tu Viaje, seleccione una opción"))
        print("1. Ver hoteles disponibles.")
        print("2. Consultar informacion de un hotel.")
        print("3. Reservar una habitacion y asientos.")
        print("4. Mostrar pasajeros de autobús.")
        print("5. Detalles de estadia.")
        print("6. Checkout.")
        print("7. Salir")
        option = input("Su opción: ")
        if option == "1":
            hotels()
        elif option == "2":
            hotel_info()
        elif option == "3":
            room_info()
        elif option == "4":
            passengers_info()
        elif option == "6":
            do_checkout()
        elif option == "7":
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 7")

#python main.py