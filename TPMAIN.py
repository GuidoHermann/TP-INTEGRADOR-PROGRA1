import csv

rutacsv = "paises.csv"  

def cargar_paises (rutacsv):
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
    
def mostrar_menu():
    print(" ===== Menu principal ===== ")
    print("1. Listar todos los paises.")
    print("2. Buscar pais por nombre")
    print("3. Filtrar paises.")
    print("4. Ordenar Paises.")
    print("5. Mostrar estadisticas")
    print("6. Salir.")

def listar_paises(paises):
    print("=== Listado de Países ===")
    for pais in paises:1
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']:,}")  # separador de miles con comas
        print(f"Superficie: {pais['superficie']:,} km²")
        print(f"Continente: {pais['continente']}\n")


paises = cargar_paises(rutacsv)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        listar_paises(paises)

    elif opcion == "2":
        print()

