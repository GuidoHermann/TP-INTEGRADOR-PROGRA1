import csv

rutacsv = "paises.csv"  

#Función para cargar los países desde el csv.
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

# =========================
# Guardar un país en el archivo CSV
# =========================
def guardar_paises(rutacsv, paises):
    with open(rutacsv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)

# ===============================
# Opción 1) Agregar un país con todos los datos necesarios para almacenarse 
# ===============================
def agregar_pais(paises):
    print("\n--- Agregar nuevo país ---")

    # Solicitar nombre y validar duplicado
    while True:
        nombre = input("Nombre: ").strip().lower()
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            continue

        existe = False
        for pais in paises:
            if pais["nombre"].lower() == nombre:
                existe = True
                break

        if existe:
            print(f"El país '{nombre}' ya existe en la base de datos. Ingrese otro nombre.")
        else:
            break

    # Validar que la población sea solo números, si esta vacío o no es un número válido se le muestra un mensaje de error al usuario.
    while True:
        poblacion = input("Población (en número entero): ").strip()
        if poblacion == "":
            print("Error: este campo no puede estar vacío.")
        elif not poblacion.isdigit():
            print("Valor inválido. Ingrese un número entero para la población.")
        else:
            poblacion = int(poblacion)
            break

    # Validar que la superficie sean solo números, si esta vacío o no es un número válido se le muestra un mensaje de error al usuario.
    while True:
        superficie = input("Superficie en km²: ").strip()
        if superficie == "":
            print("Error: este campo no puede estar vacío.")
        elif not superficie.isdigit():
            print("Valor inválido. Ingrese un número entero para la superficie.")
        else:
            superficie = int(superficie)
            break

    # Validar que el continente no este vacío y no haya sensibilidades por mayúscula o espacios.
    while True:
        continente = input("Continente: ").strip().lower()
        if continente == "":
            print("Error: el continente no puede estar vacío.")
        else:
            break

    # Agregar el país a la lista
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)
    print(f"País '{nombre}' agregado correctamente.")

    return paises

# ======================================
# Opción 2) Actualizar los datos de Población y Superfice de un País. 
# ======================================
def actualizar_pais(paises, rutacsv):
    print("\n--- Actualizar país ---")
    nombre = input("Ingrese el nombre del país a actualizar: ").strip().lower()
    encontrado = False

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            encontrado = True
            print(f"País encontrado: {pais['nombre']}")
            nueva_pob = input("Nueva población (dejar vacío para mantener actual): ").strip()
            nueva_sup = input("Nueva superficie (dejar vacío para mantener actual): ").strip()

            actualizado = False

            if nueva_pob != "":
                if nueva_pob.isdigit():
                    pais["poblacion"] = int(nueva_pob)
                    actualizado = True
                else:
                    print("Valor inválido. No se modificó la población.")

            if nueva_sup != "":
                if nueva_sup.isdigit():
                    pais["superficie"] = int(nueva_sup)
                    actualizado = True
                else:
                    print("Valor inválido. No se modificó la superficie.")

            if actualizado:
                guardar_paises(rutacsv, paises)
                print("Datos actualizados correctamente y guardados en el archivo.")
                print(f"\nPaís actualizado: {pais['nombre']}, población: {pais['poblacion']}, superficie: {pais['superficie']}")
            else:
                print("No se realizaron cambios válidos.")
            break

    if not encontrado:
        print("No se encontró el país indicado.")
    return paises

# ============================
# Menú principal
# ============================
def mostrar_menu():
    rutacsv = "paises.csv"
    paises = cargar_paises(rutacsv)

    # Muestra las opciones disponibles del menú principal
    while True: 
        print("\n=== Gestor de Países ===")
        print("1) Agregar país")
        print("2) Actualizar población / superficie")
        print("3) Buscar país por nombre (parcial/exacto)")
        print("4) Filtrar")
        print("5) Ordenar países")
        print("6) Mostrar estadísticas")
        print("7) Salir del menú")

        opcion = input("Ingrese opción: ").strip()

        match opcion:
            case "1":
               paises = agregar_pais(paises)
            case "2":
               paises = actualizar_pais(paises, rutacsv)
            case "3":
                print("opcion")
            case "4":
                print("opcion")
            case "5":
                print("opcion")
            case "6":
                print("opcion")
            case "7":
                print("Muchas gracias por visitar nuestra aplicación. Vuelva pronto.\n")
                break
            case _:
                print("La opción seleccionada no se encuentra en nuestro menú, por favor intentelo con una opción válida\n")

mostrar_menu()


