import requests
from colorama import Fore, Style, init

init()

def fetch(endpoint):
    """Collects the data from the api"""
    url = "http://127.0.0.1:5000"
    try:
        response = requests.get(url + endpoint, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data
        print(error("La opción ingresada no es válida"))
    except Exception:
        print(error("Error de conexion, intentelo de nuevo"))

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

def reserve():
    """Allows the user to make a reservation in the selected hotel"""
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
        reservation = input(dialog("2. Escriba 'reservar' o 'r' para reservar"))
        if reservation not in ("reservar", "r"):
            print("La opción ingresada es inválida")
            break
        room = input(dialog("3.Ingresa el numero de la habitacion: "))
        names = []
        print(dialog("4. Escriba el nombre y apellido de cada pasajero."))
        while True:
            name = input("Ingresa un nombre y apellido O escriba 'finalizar' o 'f' si ya no hay mas pasajeros:\n")
            if name in ("finalizar", "f"):
                break
            names.append(name)
        print(dialog("5. Seleccione un autobus."))
        while True:
            bus = input("Se encuentran disponibles los siguientes autobuses:\n[2], [6], [8], [9], [11], [12] [13], [14], [20], [23]\nS")
            if bus in ("2", "6", "8", "9", "11", "12", "13", "14", "20", "23"):
                break
            print(error("El autobús elegido no se encuentra disponible"))
        print("6. Confirme su reserva.")
        while True:
            reserva = input(f"Datos de reserva:\nID del hotel: {hotel_id}\nNúmero de habitación: {room}\nPasajeros: {names}\nNúmero de autobús: {bus}\n¿Es correcto? [si/no] ")
            if reserva == "si":
                send_reservation(hotel_id, names, room , bus)
                break
            elif reserva == "no":
                print(dialog("Reserva cancelada"))
                break
            else:
                print(error("La opcion ingresada no es valida"))

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
            response = requests.post("http://127.0.0.1:5000" + endpoint, json=body, headers=headers, timeout=10)
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
                print(f"=======================\nNombre: {r[0]}\nNúmero de autobús: {r[1]}\nNúmero de habitación: {r[2]}\n=======================")
        else:
            print(error("No se han encontrado pasajeros para el autobús seleccionado"))

def error(error_message):
    """Retorns a red string"""
    return f"{Fore.RED}{error_message}{Style.RESET_ALL}"

def dialog(dialog_message):
    """Retorns a yellow string"""
    return f"{Fore.YELLOW}{dialog_message}{Style.RESET_ALL}"

if __name__ == "__main__":
    while True:
        print(f"""=============================================================
{Fore.CYAN}Bienvenido a Planea tu Viaje, seleccione una opción{Style.RESET_ALL}
1. Ver hoteles disponibles.
2. Consultar informacion de un hotel.
3. Reservar una habitacion y asientos.
4. Mostrar pasajeros de autobús.
5. Detalles de estadia
6. Checkout.
7. Salir
""")
        option = input("Su opción: ")
        if option == "1":
            hotels()
        elif option == "2":
            hotel_info()
        elif option == "3":
            reserve()
        elif option == "4":
            passengers_info()
        elif option == "7":
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 7")

#python main.py