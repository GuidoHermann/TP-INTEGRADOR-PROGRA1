import csv

rutacsv = "paises.csv"  

def cargar_paises (rutacsv): #funcion para cargar los paises desde el csv.
    paises = []
    with open(rutacsv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            pais = {
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"].replace(".","").replace(",","")),
                "superficie": int(fila["superficie"].replace(".","").replace(",","")),
                "continente": fila["continente"]
            }
            paises.append(pais)
        return paises
    
def mostrar_menu(): #funcion para mostrar las opciones disponible al usario.
    print(" ===== Menu principal ===== ")
    print("1. Listar todos los paises.")
    print("2. Buscar pais por nombre")
    print("3. Filtrar paises.")
    print("4. Ordenar Paises.")
    print("5. Mostrar estadisticas")
    print("6. Salir.")

def listar_paises(paises): 
    # funcion para recorrer una lista con todos los paises del csv y los muestra en un formato legible.
    # se utiliza la "," como separador de miles en poblacion y superficie.
    print("\n=== Listado de Países ===\n")
    for pais in paises:
        print(f"Nombre: {pais["nombre"]}")
        print(f"Población: {pais["poblacion"]:,}")  # separador de miles con comas
        print(f"Superficie: {pais["superficie"]:,} km²")
        print(f"Continente: {pais["continente"]}\n")
    
def buscar_pais(paises):
    # funcion que solicita al usuario un texto para buscar paises.
    # la busqueda es parcial y no distingue mayuscula/minusculas.
    # muetra todos los resultados que coincidan o un mensaje si no encuentra ninguno.
    texto = input("\nIngrese el nombre del pais a buscar: \n").strip().lower()
    encontrados = []


    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} paises que coinciden: \n")
        for pais in encontrados:
            print(f"Nombre: {pais["nombre"]}")
            print(f"Población: {pais["poblacion"]:,}")  # separador de miles con comas
            print(f"Superficie: {pais["superficie"]:,} km²")
            print(f"Continente: {pais["continente"]}\n")
    
    else:
        print("No se encontro ningun pais que coincida con la busqueda.")


paises = cargar_paises(rutacsv)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        listar_paises(paises)

    elif opcion == "2":
        buscar_pais(paises)

    elif opcion == "3":
        print("Opción 3: Filtrar países (pendiente de implementar)")

    elif opcion == "4":
        print("Opción 4: Ordenar países (pendiente de implementar)")

    elif opcion == "5":
        print("Opción 5: Mostrar estadísticas (pendiente de implementar)")

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
