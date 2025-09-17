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
    
paises = cargar_paises(rutacsv)

print("Datos cargados")


for pais in paises:
    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']:,} Habitantes") 
    print(f"Superficie: {pais['superficie']:,} km²")
    print(f"Continente: {pais['continente']}\n")
