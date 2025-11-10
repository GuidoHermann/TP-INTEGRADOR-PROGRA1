# TP-INTEGRADOR-PROGRAMACIÓN 1

Repositorio del trabajo practico integrador de Programacion 1 UTN VIRTUAL

## Comisión:

Comisión n° 6

## Integrantes:

Alzogaray, Guido Hermann
Godoy, Sabrina Anabella

### Participación de los integrantes:

Ambos integrantes trabajamos de manera conjunta en todas las etapas del proyecto: desde el análisis de la consigna, la recolección de información, la planificación del código y su desarrollo, hasta las pruebas, validaciones y documentación final.
Cada decisión y mejora fue realizada en equipo, garantizando una participación equitativa y colaborativa durante todo el proceso.

## Descripción del programa:

Este programa es un gestor de información de países, desarrollado en Python.
Permite administrar y analizar datos de distintos países, almacenados en un archivo CSV, aplicando los principales conceptos aprendidos en la materia:

- Uso de estructuras de datos (listas y diccionarios).

- Implementación de funciones modulares.

- Control de errores y validaciones de entrada.

- Procesamiento de archivos CSV.

- Operaciones de búsqueda, filtrado, ordenamiento y estadísticas.

El usuario puede agregar nuevos países, actualizar sus datos, buscar y filtrar información, ordenar los resultados y obtener estadísticas generales, todo desde un menú interactivo en consola.

## Instrucciones de uso:

Al iniciar, se mostrará el menú principal con las siguientes opciones:
=== Gestor de Países ===

1. Agregar país
2. Actualizar población / superficie
3. Buscar país por nombre (parcial/exacto)
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Salir del menú

El usuario debe ingresar el número correspondiente a la acción que desee realizar.
El programa validará todas las entradas para evitar errores (por ejemplo, que los valores sean numéricos donde corresponda o que no existan campos vacíos).

Todos los cambios realizados se guardan automáticamente en el archivo paises.csv.

### Comando para clonar el proyecto:

git clone https://github.com/GuidoHermann/TP-INTEGRADOR-PROGRA1.git

## Ejemplo de entradas y salidas:

### Ejemplo:

- Entrada del usuario:
  1
  Nombre: Uruguay
  Población (en número entero): 3423100
  Superficie en km²: 176215
  Continente: América

- Salida esperada:
  País 'Uruguay' agregado correctamente.

### Ejemplo:

- Entrada del usuario:
  3
  Ingrese el nombre del país a buscar:
  arg

- Salida esperada:
  Se encontraron: 1 países que coinciden:

Nombre: Argentina
Población: 45,376,763
Superficie: 2,780,400 km²
Continente: América

### Ejemplo:

- Entrada del usuario:
  6

- Salida esperada:
  --- Estadísticas ---
  País con mayor población: China (1,411,778,724)
  País con menor población: Islandia (343,599)
  Promedio de población: 76,434,122
  Promedio de superficie: 1,542,880 km²
  Cantidad de países por continente:
  América: 12
  Europa: 10
  Asia: 8
  África: 9
  Oceanía: 5
