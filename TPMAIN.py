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
    
# Funciones auxiliares
def obtener_nombre(pais):
    return pais["nombre"]

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]

# Guardar un país en el archivo CSV
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



# ======================================
# Opción 3 Buscar países
# ======================================
def buscar_pais(paises):
    texto = input("\nIngrese el nombre del pais a buscar: \n").strip().lower()
    encontrados = []

    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) > 0:
        print(f"\nSe encontraron {len(encontrados)} paises que coinciden: \n")
        for pais in encontrados:
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']:,}")
            print(f"Superficie: {pais['superficie']:,} km²")
            print(f"Continente: {pais['continente']}\n")
    else:
        print("No se encontro ningun pais que coincida con la busqueda.")

# ======================================
# Opción 4) Filtrar países
# ======================================
def filtrar_paises(paises):
    print("\n=== Filtrar Países ===")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Seleccione una opción de filtrado: ")

    resultados = []

    #filtro por continente
    if opcion == "1":
        continente = input("Ingrese el continente: ").strip().lower()
        for pais in paises:
            continente_pais = pais["continente"].lower()
            if continente in continente_pais:
                resultados.append(pais)

    #filtro por poblacion
    elif opcion == "2":
        minimo = input("Ingrese la poblacion minima: ").strip()
        maximo = input("Ingrese la poblacion maxima: ").strip()
        if minimo.isdigit() and maximo.isdigit():
            minimo = int(minimo)
            maximo = int(maximo)
            for pais in paises:
                poblacion = pais["poblacion"]
                if poblacion >= minimo and poblacion <= maximo:
                    resultados.append(pais)
        else:
            print("Solo valores numericos.")

    #filtro por superficie
    elif opcion == "3":
        minimo = input("Ingrese la superficie minima: ").strip()
        maximo  = input("Ingrese la superficie maxima: ").strip()
        if minimo.isdigit() and maximo.isdigit():
            minimo = int(minimo)
            maximo = int(maximo)
            for pais in paises:
                superficie = pais["superficie"]
                if superficie >= minimo and superficie <= maximo:
                    resultados.append(pais)
        else:
            print("Solo valores numericos.")

    else:
        print("Opcion invalida.")

    if len(resultados) > 0:
        print(f"\nSe encontraron {len(resultados)} países:\n")
        for pais in resultados:
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']:,}")
            print(f"Superficie: {pais['superficie']:,} km²")
            print(f"Continente: {pais['continente']}\n")
    else:
        print("\nNo se encontraron países con esos criterios.")

# ======================================
# Opción 5) Ordenar países por: Nombre | Población | Superficie (ascendente o descendente)  
# ======================================
def ordenar_paises(paises):
    print("\n--- Ordenar países ---")

    # Validar opción numérica (1, 2 o 3)
    while True:
        print("1) Por nombre")
        print("2) Por población")
        print("3) Por superficie")
        opcion = input("Seleccione opción (1-3): ").strip()
        if opcion not in ("1", "2", "3"):
            print("Opción inválida. Ingrese 1, 2 o 3.")
        else:
            break

    # Validar tipo de orden (A o D)
    while True:
        orden = input("Ascendente (A) o Descendente (D): ").strip().lower()
        if orden not in ("a", "d"):
            print("Entrada inválida. Escriba 'A' para ascendente o 'D' para descendente.")
        else:
            break

    invertido = (orden == "d")

    # Ordenar según la opción elegida
    if opcion == "1":
        paises_ordenados = sorted(paises, key=obtener_nombre, reverse=invertido)
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=invertido)
    elif opcion == "3":
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=invertido)

    # Mostrar resultados
    print("\nListado ordenado:")
    for p in paises_ordenados:
        print(f"{p['nombre']} - {p['poblacion']} hab. - {p['superficie']} km² - {p['continente']}")



# ======================================
# Opción 6) Mostrar estadísticas: País con mayor y menor población | Promedio de población | Promedio de superficie | Cantidad de países por continente 
# ======================================
def mostrar_estadisticas(paises):
    print("\n--- Estadísticas ---")

    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    # Mayor y menor población
    mayor = paises[0]
    menor = paises[0]
    suma_pob = 0
    suma_sup = 0
    conteo_continentes = {}

    for pais in paises:
        suma_pob += pais["poblacion"]
        suma_sup += pais["superficie"]

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        cont = pais["continente"]
        if cont not in conteo_continentes:
            conteo_continentes[cont] = 1
        else:
            conteo_continentes[cont] += 1

    prom_pob = suma_pob / len(paises)
    prom_sup = suma_sup / len(paises)

    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {int(prom_pob)}")
    print(f"Promedio de superficie: {int(prom_sup)} km²")
    print("Cantidad de países por continente:")
    for c, n in conteo_continentes.items():
        print(f"  {c}: {n}")

# ============================
# Menú principal
# ============================
def mostrar_menu():
    rutacsv = "paises.csv"
    paises = cargar_paises(rutacsv)

    while True: 
        print("\n=== Gestor de Países ===")
        print("1) Agregar país")
        print("2) Actualizar población / superficie")
        print("3) Buscar país por nombre (parcial/exacto)")
        print("4) Filtrar países")
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
                buscar_pais(paises)
            case "4":
                filtrar_paises(paises)
            case "5":
                ordenar_paises(paises)
            case "6":
                mostrar_estadisticas(paises)
            case "7":
                print("Muchas gracias por visitar nuestra aplicación. Vuelva pronto.\n")
                break
            case _:
                print("La opción seleccionada no se encuentra en nuestro menú, por favor intentelo con una opción válida\n")

mostrar_menu()
