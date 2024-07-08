import requests
from colorama import Fore, Style, init

init()

def fetch(endpoint):
    url = 'http://127.0.0.1:5000'
    response = requests.get(url + endpoint)
    if response.status_code == 200:
        data = response.json()
        return data
    return "Error de conexion, intentelo de nuevo"

def hotels():
    response = fetch("/hotels")
    for r in response:
        print(f"=======================\nId del hotel: {r["ID_Hotel"]}\nNombre del hotel: {r["Name"]}\n=======================")

def hotel_info():
    while True:
        hotel_id = input("1. Ingrese el id de un hotel: \n2. O escriba 'volver' o 'v' para volver atrás ")
        if hotel_id in ("volver", "v"):
            break
        else:
            response = fetch(f"/hotel/{hotel_id}")
            print(f"=======================\nId del hotel: {response["ID_Hotel"]}\nNombre del hotel: {response["Name"]}\nDirección: {response["Adress"]}\nTeléfono: {response["Phone"]}\n=======================") #

def reserve():
     while True:
        hotel_id = input("1. Ingrese el id de un hotel: \n2. O escriba 'volver' o 'v' para volver atrás ")
        if id in ("volver", "v"):
            break
        else:
            response = fetch(f"/hotel/{hotel_id}/rooms")
            for r in response:
                print(f"=======================\nNúmero de habitación: {r[2]}\nTipo de habitación: {r[1]}\nDisponibilidad: {r[4]}\nPrecio: {r[3]}\n=======================")
            reservation = input("1. Escriba 'reservar' o 'r' para reservar: \n2. O escriba 'volver' o 'v' para volver atrás ")
            if reservation in ("volver", "v"):
                print("Reservacion exitosa")

def passengers_info():
    while True:
        bus_num = input("1. Ingrese el numero de un autobús: \n2. O escriba 'volver' o 'v' para volver atrás ")
        if id in ("volver", "v"):
            break
        else:
            response = fetch(f"/hotel/bus/{bus_num}")
            for r in response:
                print(f"=======================\nNombre: {r["Name"]}, Número de autobús: {r["Bus_Number"]}, Número de habitación: {r["Room_Number"]}\n=======================")

if __name__ == "__main__":
    while True:
        print(f"""=============================================================
{Fore.CYAN}Bienvenido a Planea tu viaje, seleccione una opcion{Style.RESET_ALL}
1. Ver hoteles disponibles.
2. Consultar informacion de un hotel.
3. Reservar una habitacion y asientos.
4. Pasajeros.
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

#python main.py