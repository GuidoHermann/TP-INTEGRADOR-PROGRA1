import csv

# Ruta de archivo CSV que contiene los datos de países
rutacsv = "paises.csv"  

# Función para cargar los países desde el archivo CSV.
def cargar_paises (rutacsv): 
    paises = []
    with open(rutacsv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convierte los campos de población y superficie a enteros, eliminando separadores
            pais = {
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"].replace(".","").replace(",","")),
                "superficie": int(fila["superficie"].replace(".","").replace(",","")),
                "continente": fila["continente"]
            }
            paises.append(pais)
        return paises
    
# =============================== 
# Funciones auxiliares para ordenar
def obtener_nombre(pais):
    return pais["nombre"].lower()

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]

# Mostrar los datos de un país con formato uniforme
def mostrar_pais(pais):
    """Imprime los datos de un país con formato uniforme."""
    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']:,}")
    print(f"Superficie: {pais['superficie']:,} km²")
    print(f"Continente: {pais['continente']}\n")

# Guardar la lista de países en el archivo CSV
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

    # Solicitar nombre y validar que no esté vacío, no tenga números ni duplicados
    while True:
        nombre = input("Nombre: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            continue
        elif not nombre.replace(" ", "").isalpha():  # solo letras y espacios
            print("Error: el nombre no puede contener números ni símbolos.")
            continue

        nombre_formateado = nombre.title()

        # Validar duplicado sin importar mayúsculas/minúsculas
        existe = False
        for pais in paises:
            if pais["nombre"].lower() == nombre_formateado.lower():
                existe = True
                break

        if existe:
            print(f"El país '{nombre_formateado}' ya existe en la base de datos. Ingrese otro nombre.")
        else:
            nombre = nombre_formateado
            break

    # Validar población: debe ser un número entero positivo
    while True:
        poblacion = input("Población (en número entero): ").strip()
        if poblacion == "":
            print("Error: este campo no puede estar vacío.")
        elif not poblacion.isdigit():
            print("Valor inválido. Ingrese un número entero positivo.")
        elif int(poblacion) <= 0:
            print("La población debe ser mayor que cero.")
        else:
            poblacion = int(poblacion)
            break

    # Validar superficie: debe ser un número entero positivo
    while True:
        superficie = input("Superficie en km²: ").strip()
        if superficie == "":
            print("Error: este campo no puede estar vacío.")
        elif not superficie.isdigit():
            print("Valor inválido. Ingrese un número entero positivo.")
        elif int(superficie) <= 0:
            print("La superficie debe ser mayor que cero.")
        else:
            superficie = int(superficie)
            break

    # Validar continente: solo letras, sin símbolos ni números
    while True:
        continente = input("Continente: ").strip()
        if continente == "":
            print("Error: el continente no puede estar vacío.")
        elif not continente.replace(" ", "").isalpha():
            print("Error: el continente no puede contener números ni símbolos.")
        else:
            continente = continente.title()
            break

    # Agregar el país a la lista
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)
    guardar_paises(rutacsv, paises)
    print(f"País '{nombre}' agregado correctamente.")

    return paises



# ======================================
# Opción 2) Actualizar los datos de Población y Superficie de un País. 
# ======================================
def actualizar_pais(paises, rutacsv):
    print("\n--- Actualizar país ---")

    # Mostrar lista de países disponibles
    print("\nPaíses disponibles:")
    for p in paises:
        print(f"- {p['nombre']}")
    print("--------------------------------")

    # Pedir el país a actualizar
    nombre = input("\nIngrese el nombre exacto del país a actualizar: ").strip().title()
    encontrado = False

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            encontrado = True
            print(f"\nPaís encontrado: {pais['nombre']}")
            print(f"Población actual: {pais['poblacion']:,}")
            print(f"Superficie actual: {pais['superficie']:,} km²\n")

            actualizado = False

            # Validar nueva población (opcional)
            while True:
                nueva_pob = input("Nueva población (dejar vacío para mantener actual): ").strip()
                if nueva_pob == "":
                    break  # no se modifica
                elif not nueva_pob.isdigit():
                    print("Error: la población debe ser un número entero positivo.")
                elif int(nueva_pob) <= 0:
                    print("Error: la población debe ser mayor que cero.")
                else:
                    pais["poblacion"] = int(nueva_pob)
                    actualizado = True
                    break

            # Validar nueva superficie (opcional)
            while True:
                nueva_sup = input("Nueva superficie (dejar vacío para mantener actual): ").strip()
                if nueva_sup == "":
                    break  # no se modifica
                elif not nueva_sup.isdigit():
                    print("Error: la superficie debe ser un número entero positivo.")
                elif int(nueva_sup) <= 0:
                    print("Error: la superficie debe ser mayor que cero.")
                else:
                    pais["superficie"] = int(nueva_sup)
                    actualizado = True
                    break

            # Guardar los cambios si hubo alguna modificación
            if actualizado:
                guardar_paises(rutacsv, paises)
                print("\n✅ Datos actualizados correctamente y guardados en el archivo.")
                print(f"País actualizado: {pais['nombre']} — Población: {pais['poblacion']:,}, Superficie: {pais['superficie']:,} km²")
            else:
                print("\nNo se realizaron cambios.")
            break

    if not encontrado:
        print("\nNo se encontró el país indicado. Revise el nombre e intente nuevamente.")

    return paises



# ======================================
# Opción 3 Buscar países
# ======================================
def buscar_pais(paises):
    texto = input("\nIngrese el nombre del pais a buscar: \n").strip().lower()
    encontrados = []

    # Recorre los países y si el nombre existe lo agrega a la lista de 'encontrados'
    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    # Verifica que la lista tenga al menos un elemento y lo muestra, sino le muestra un mensaje al usuario informandole que no se han encontrado
    if len(encontrados) > 0:
        print(f"\nSe encontraron {len(encontrados)} paises que coinciden: \n")
        for pais in encontrados:
           mostrar_pais(pais)
    else:
        print("No se encontro ningun pais que coincida con la busqueda.")

# ======================================
# Opción 4) Filtrar países
# ======================================
def filtrar_paises(paises):
    print("\n=== Filtrar Países ===")

    # Convierte el texto a entero
    def parse_int(valor):
        if valor is None:
            return None
        texto = valor.replace(".", "").replace(",", "").strip()
        if texto.isdigit():
            return int(texto)
        return None

    # Valida que la opción que seleccione el usuario sea una de las mencionadas
    while True:
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        opcion = input("Seleccione una opción de filtrado (1-3): ").strip()
        if opcion not in ("1", "2", "3"):
            print("Opción inválida. Ingrese 1, 2 o 3.")
        else:
            break

    resultados = []

    # filtro por continente
    if opcion == "1":
        while True:
            continente = input("Ingrese el continente: ").strip().lower()
            if continente == "":
                print("El continente no puede estar vacío. Intente de nuevo.")
            else:
                break
        for pais in paises:
            continente_pais = pais["continente"].lower()
            if continente in continente_pais:
                resultados.append(pais)

    # filtro por poblacion
    elif opcion == "2":
        # Pide el mínimo para filtrar la población
        while True:
            minimo_raw = input("Ingrese la población mínima: ").strip()
            minimo = parse_int(minimo_raw)
            if minimo is None:
                print("Valor inválido. Ingrese un número entero para la población mínima.")
            else:
                break
        # Pide el máximo para filtrar la población
        while True:
            maximo_raw = input("Ingrese la población máxima: ").strip()
            maximo = parse_int(maximo_raw)
            if maximo is None:
                print("Valor inválido. Ingrese un número entero para la población máxima.")
            else:
                break
        # Comprueba que el orden mínimo sea <= máximo
        while minimo > maximo:
            print("La población mínima no puede ser mayor que la máxima. Ingrese los valores nuevamente.")
            # Vuelve a pedir ambos
            while True:
                minimo_raw = input("Ingrese la población mínima: ").strip()
                minimo = parse_int(minimo_raw)
                if minimo is None:
                    print("Valor inválido. Ingrese un número entero para la población mínima.")
                else:
                    break
            while True:
                maximo_raw = input("Ingrese la población máxima: ").strip()
                maximo = parse_int(maximo_raw)
                if maximo is None:
                    print("Valor inválido. Ingrese un número entero para la población máxima.")
                else:
                    break
        # Filtra los resultados
        for pais in paises:
            poblacion = pais["poblacion"]
            if minimo <= poblacion <= maximo:
                resultados.append(pais)

    # Filtro por superficie
    elif opcion == "3":
        # Pide el mínimo para filtrar la superficie
        while True:
            minimo_raw = input("Ingrese la superficie mínima: ").strip()
            minimo = parse_int(minimo_raw)
            if minimo is None:
                print("Valor inválido. Ingrese un número entero para la superficie mínima.")
            else:
                break
        # Pide el máximo para filtrar la superficie
        while True:
            maximo_raw = input("Ingrese la superficie máxima: ").strip()
            maximo = parse_int(maximo_raw)
            if maximo is None:
                print("Valor inválido. Ingrese un número entero para la superficie máxima.")
            else:
                break
        # comprueba que el orden mínimo sea <= máximo
        while minimo > maximo:
            print("La superficie mínima no puede ser mayor que la máxima. Ingrese los valores nuevamente.")
            while True:
                minimo_raw = input("Ingrese la superficie mínima: ").strip()
                minimo = parse_int(minimo_raw)
                if minimo is None:
                    print("Valor inválido. Ingrese un número entero para la superficie mínima.")
                else:
                    break
            while True:
                maximo_raw = input("Ingrese la superficie máxima: ").strip()
                maximo = parse_int(maximo_raw)
                if maximo is None:
                    print("Valor inválido. Ingrese un número entero para la superficie máxima.")
                else:
                    break
        #Filtra los resultados
        for pais in paises:
            superficie = pais["superficie"]
            if minimo <= superficie <= maximo:
                resultados.append(pais)

    # Muestra los resultados del filtrado
    if len(resultados) > 0:
        print(f"\nSe encontraron {len(resultados)} países:\n")
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print("\nNo se encontraron países con esos criterios.")

# ======================================
# Opción 5) Ordenar países por: Nombre | Población | Superficie (ascendente o descendente)
# ======================================
def ordenar_paises(paises):
    print("\n--- Ordenar países ---")

    # Elegir criterio
    while True:
        print("1) Por nombre")
        print("2) Por población")
        print("3) Por superficie")
        opcion = input("Seleccione opción (1-3): ").strip()
        if opcion not in ("1", "2", "3"):
            print("Opción inválida. Ingrese 1, 2 o 3.")
        else:
            break

    # Elegir tipo de orden
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
        criterio = "nombre"
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=invertido)
        criterio = "población"
    elif opcion == "3":
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=invertido)
        criterio = "superficie"

    # Mostrar resultados
    print(f"\n--- Listado ordenado por {criterio} ({'descendente' if invertido else 'ascendente'}) ---\n")
    for p in paises_ordenados:
        print(f"{p['nombre']:20} | {p['poblacion']:>12,} hab | {p['superficie']:>10,} km² | {p['continente']}")

        
# ======================================
# Opción 6) Mostrar estadísticas: País con mayor y menor población | Promedio de población | Promedio de superficie | Cantidad de países por continente 
# ======================================
def mostrar_estadisticas(paises):
    print("\n--- Estadísticas ---")

    # Verifica si la lista de países está vacía
    if len(paises) == 0:
        print("No hay datos cargados.")
        return
     
    # Inicializa variables para encontrar país con mayor y menor población, y para acumular población y superficie total
    mayor = paises[0]
    menor = paises[0]
    suma_pob = 0
    suma_sup = 0
    conteo_continentes = {} # Diccionario para contar países por continente

    # Recorre la lista de países para calcular estadísticas
    for pais in paises:
        suma_pob += pais["poblacion"]
        suma_sup += pais["superficie"]

        #Actualiza los países con mayor o menor población si corresponde
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        # Cuenta cuántos países hay por continente
        cont = pais["continente"]
        if cont not in conteo_continentes:
            conteo_continentes[cont] = 1
        else:
            conteo_continentes[cont] += 1

    # Calcula promedios de población y superficie
    prom_pob = suma_pob / len(paises)
    prom_sup = suma_sup / len(paises)

    # Muestra los resultados estadísticos
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

    # Muestra el menú y se repite hasta que el usuario coloque la opción de 'Salir al menú'
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
