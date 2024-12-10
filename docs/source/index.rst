Generador de Calendario Deportivo
=================================

Bienvenido al generador de calendario deportivo para equipos. Este proyecto permite generar calendarios de partidos entre equipos, teniendo en cuenta las distancias entre las sedes y asegurando que los equipos no jueguen demasiados partidos consecutivos como local o visitante.

Índice
======
- Introducción
- Instalación
- Estructura del Código
- Funciones del Código
- Descripción y análisis de las pruebas realizadas.
- Conclusiones y aspectos a mejorar.

.. toctree::
   :maxdepth: 2
   :caption: Contenidos:

   introducción
   instalacion
   estructura del codigo
   funciones
   descripcion y pruebas
   conclusiones

Introducción
============

Este proyecto permite cargar un archivo de texto con los datos de equipos y distancias entre ellos. A partir de esos datos, genera un calendario de partidos de ida y vuelta, respetando las restricciones de partidos consecutivos de local y visitante, y muestra la matriz de distancias entre los equipos.

El propósito principal es organizar de manera eficiente el calendario deportivo en función de la distancia entre los equipos, maximizando la equidad en términos de viajes.

Instalación
===========
Para instalar y ejecutar el proyecto, asegúrese de tener **Python 3.x** y las dependencias necesarias instaladas.


Estructura del Código
=====================

El código está organizado de la siguiente manera:

Cargar y leer archivo: 
----------------------
Esta función se encarga de abrir un cuadro de diálogo para seleccionar un archivo de texto que contiene el nùmero de equipos y las distancias entre ellos. Después, el archivo es procesado línea por línea para cargar los datos en matrices y listas.

La complejidad depende de la cantidad de datos en el archivo y de la operacion que se realice. Si el archivo contiene n equipos, el código necesita leer nxn líneas de datos en la matriz de distancia y procesarlas. La complejidad para cargar los datos es O(n^2).

Generación del calendario: 
--------------------------
Esta función es responsable de generar los calendarios de los partidos tanto de ida como de vuelta. Dado un número de equipos n, la función genera todas las combinaciones posibles de partidos entre equipos para cada jornada. Cada jornada involucra n/2 partidos, y el número total de jornadas es 2(n−1).
La generación de calendarios tiene una complejidad O(n^2) porque se realizan múltiples combinaciones entre equipos para crear las jornadas. Por cada partido, es necesario iterar sobre los equipos y asignarles una localía (local o visitante), lo que se hace en n^2 iteraciones.

Cálculo de distancias
---------------------
Después de generar los calendarios, esta función calcula la distancia recorrida por cada equipo sumando las distancias entre los partidos programados en el calendario. Para cada partido, se obtiene la distancia de la matriz de distancias.
Al igual que la generación de calendarios, el cálculo de distancias también tiene una complejidad cuadrática O(n^2), ya que para cada jornada de partidos, se necesita acceder a la matriz de distancias de nxn equipos, lo que lleva O(n^2) 

Interfaz gráfica: 
-----------------
Esta parte es más sencilla, ya que solo implica la actualización de la interfaz gráfica con los resultados. Visualizar las distancias recorridas y los calendarios generalmente tiene un impacto temporal bajo, cercano a O(1) (es decir, constante), ya que se limita a la actualización de elementos gráficos, sin realizar cálculos complejos.




Funciones del Código
====================

A continuación, se describen las principales funciones del proyecto:

1. **cargar_archivo()**:
   La función cargar_archivo() usa un cuadro de diálogo de tkinter para permitir que el usuario seleccione un archivo. Luego, procesa las líneas del archivo y las almacena en las variables adecuadas: los equipos, las distancias y las configuraciones mínimas y máximas.

2. **leer_archivo()**:
   En la función leer_archivo(), el código valida que el número de equipos sea par (ya que no se pueden emparejar equipos si hay un número impar) y procesa las distancias en una matriz. Este paso asegura que los datos sean consistentes y estén listos para usar en la generación del calendario.
   Lee el archivo de texto, extrae los equipos, las distancias y otros datos necesarios, y devuelve estos valores para ser procesados.

3. **generar_calendario()**:
   La función generar_calendarios() crea los calendarios de partidos de ida y vuelta para los equipos. En cada jornada, se organiza a los equipos en partidos, alternando la localía entre los equipos, es decir, un equipo juega en casa y el otro como visitante.

4. **Cálculo de distancias:**:
   la función calcular_distancias_recorridas() se implementa una vez generados los calendarios,  calcula la distancia total recorrida por cada equipo. Este cálculo es importante para conocer el impacto logístico y económico de la organización del torneo.

5. **Interfaz gráfica (GUI)**:
   Usando la librería tkinter, el código crea una interfaz de usuario con botones y cuadros de texto para que el usuario pueda cargar el archivo, generar los calendarios, y visualizar los resultados. Los calendarios, las distancias recorridas, y la matriz de distancias se muestran de forma clara y accesible para el usuario


Descripcion de Pruebas realizadas
=================================

En esta sección se describe las pruebas realizadas para asegurar que el programa funciona correctamente.

Prueba de carga de archivo:
---------------------------
Verificar que el archivo se carga correctamente y que los datos son interpretados de manera adecuada.
Se carga un archivo con información válida, asegurándose de que los equipos y las distancias se reflejan correctamente en la interfaz gráfica.
Ejemplo:

ARCHIVO TXT para cuatro equipos

+-------+-------+----------+
|Linea 1|   n   |     4    |
+-------+-------+----------+
|Linea 2|  min  |     1    |
+-------+-------+----------+
|Linea 3|  max  |     2    |
+-------+-------+----------+
|Linea 4| matriz| 0 1 2 3  |
|       |       | 1 0 6 7  |
|       |       | 2 6 0 10 |
|       |       | 3 7 10 0 |
+-------+-------+----------+

Resultado esperado: Los equipos deben aparecer en la lista y la matriz de distancias debe ser correcta. Si el archivo tiene errores (por ejemplo, datos mal formateados), el programa debe mostrar un mensaje de error adecuado.

.. image:: Imagen1.png
Imagen 1. Interfaz del programa

.. image:: Imagen2.png
Imagen 2. Seleccionamos el boton **Cargar archivo** para desplegar el selector de archivos

.. image:: Imagen3.png
Imgen 3. Se muestra como los datos inciales son cargados **Exitosamente**

.. image:: Imagen4.png
Imagen 4. Se muestra el valor minimo, maximo y la matriz de distancias.

.. image:: Imagen5.png
Imagen 5. Al seleccionar el boton **Generar Calendario** se muestra las jornadas de los partidos,

Conclusiones
============
El código cumple adecuadamente con algunas de los requisitos establecidos, realizando de manera efectiva las funciones principales como cargar archivos, generar calendarios y calcular distancias. Además, la interfaz gráfica facilita la interacción del usuario, siendo clara y comprensible para realizar las acciones necesarias.

Aunque el rendimiento del programa es satisfactorio en su funcionamiento básico, se observa que las operaciones de generación de calendarios y cálculo de distancias presentan una complejidad cuadrática, lo que puede generar ineficiencias cuando se trabaja con un gran número de equipos. Para optimizar el código, sería conveniente explorar el uso de algoritmos más eficientes o paralelizar algunas de las tareas para mejorar la velocidad de ejecución.

Otro aspecto a mejorar es la validación de los datos. Actualmente, la validación es limitada, lo que podría llevar a errores si los datos del archivo contienen distancias fuera de rango o valores inconsistentes. Mejorar esta validación garantiza la integridad de los datos y la confiabilidad de los resultados obtenidos.

Finalmente, la interfaz gráfica podría expandirse para ofrecer más opciones interactivas que enriquecen la experiencia del usuario. Funcionalidades como la posibilidad de modificar los calendarios generados, reorganizar los partidos o visualizar estadísticas adicionales sobre las distancias recorridas por los equipos que  proporcionarán mayor flexibilidad y valor al programa.
