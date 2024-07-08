import requests
from colorama import Fore, Style, init

init()

def fetch(endpoint):
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
    response = fetch("/hotels")
    if response:
        for r in response:
            print(f"=======================\nId del hotel: {r["ID_Hotel"]}\nNombre del hotel: {r["Name"]}\n=======================")

def hotel_info():
    while True:
        hotel_id = input("1. Ingrese el id de un hotel: \n2. O escriba 'volver' o 'v' para volver atrás ")
        if hotel_id in ("volver", "v"):
            break
        response = fetch(f"/hotel/{hotel_id}")
        if response and response != "Error":
            print(f"=======================\nId del hotel: {response["ID_Hotel"]}\nNombre del hotel: {response["Name"]}\nDirección: {response["Adress"]}\nTeléfono: {response["Phone"]}\n=======================") #
        else:
            print(error("El id ingresado no corresponde a ningún hotel"))
            break

def reserve():
     while True:
        hotel_id = input("1. Ingrese el id de un hotel: \n2. O escriba 'volver' o 'v' para volver atrás ")
        if hotel_id in ("volver", "v"):
            break
        response = fetch(f"/hotel/{hotel_id}/rooms")
        if response and response != "Error":
            for r in response:
                print(f"=======================\nNúmero de habitación: {r[2]}\nTipo de habitación: {r[1]}\nDisponibilidad: {r[4]}\nPrecio: {r[3]}\n=======================")
            reservation = input("1. Escriba 'reservar' o 'r' para reservar: \n2. O escriba 'volver' o 'v' para volver atrás ")
            if reservation in ("volver", "v"):
                break
            room = input("Ingresa el numero de la habitacion")
            names = []
            print("Escriba el nombre y apellido de cada pasajeros")
            while True:
                name = input("Ingresa un nombre y apellido:\nO escriba 'finalizar' o 'f' si ya no hay mas pasajeros")
                if name in ("finalizar", "f"):
                    break
            bus = input("Elija un autobus")
            send_reservation(hotel_id, room, names, bus)
        else:
            print(error("El id ingresado no corresponde a ningún hotel"))
            break

def send_reservation(hotel_id, names, room, bus):
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
                response = requests.post("http://127.0.0.1:5000" + endpoint, json=body, headers=headers)
                if response.status_code == 200:
                    print("Reserva enviada correctamente.")
        except Exception:
            print("Error al enviar la reserva")

def passengers_info():
    while True:
        bus_num = input("1. Ingrese el numero de un autobús: \n2. O escriba 'volver' o 'v' para volver atrás ")
        if id in ("volver", "v"):
            break
        response = fetch(f"/hotel/bus/{bus_num}")
        if response and response != "Error":
            for r in response:
                print(f"=======================\nNombre: {r["Name"]}, Número de autobús: {r["Bus_Number"]}, Número de habitación: {r["Room_Number"]}\n=======================")
        else:
            print(error("No se han encontrado pasajeros para el autobus seleccionado"))
            break

def error(error):
    return f"{Fore.RED}{error}{Style.RESET_ALL}"

if __name__ == "__main__":
    while True:
        print(f"""=============================================================
{Fore.CYAN}Bienvenido a Planea tu viaje, seleccione una opcion{Style.RESET_ALL}
1. Ver hoteles disponibles.
2. Consultar informacion de un hotel.
3. Reservar una habitacion y asientos.
4. Mostrar pasajeros de autobús.
5. Detalles de estadia
6. Checkout.
7. Salir
""")
        
        option = input("Tu opcion: ")
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