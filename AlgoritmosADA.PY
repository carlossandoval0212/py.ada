import tkinter as tk
from tkinter import filedialog, messagebox, Scrollbar

# Función para cargar el archivo de texto
def cargar_archivo():
    archivo_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
    if archivo_path:
        try:
            global equipos, minimo, maximo, kilometros_matriz, distancias
            equipos, minimo, maximo, kilometros_matriz, distancias = leer_archivo(archivo_path)
            actualizar_lista_equipos()
            actualizar_minimo_maximo()
            messagebox.showinfo("Éxito", f"Se cargaron {len(equipos)} equipos y la matriz de distancias.")
            
            # Habilitar el botón para generar el calendario después de cargar el archivo
            generar_btn.config(state=tk.NORMAL)
            mostrar_matriz_distancias()  # Mostrar la matriz de distancias en el nuevo Text
        except ValueError as e:
            messagebox.showerror("Error", f"Error de datos: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

# Función para actualizar la lista de equipos en la interfaz
def actualizar_lista_equipos():
    equipos_lista.delete(0, tk.END)
    for equipo in equipos:
        equipos_lista.insert(tk.END, equipo)

# Función para actualizar los valores de mínimo y máximo en los cuadros de texto
def actualizar_minimo_maximo():
    minimo_text.delete(1.0, tk.END)
    minimo_text.insert(tk.END, str(minimo))

    maximo_text.delete(1.0, tk.END)
    maximo_text.insert(tk.END, str(maximo))

# Función para leer los datos del archivo de texto
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Leer el número de equipos (debe ser par)
            n = int(archivo.readline().strip())
            if n % 2 != 0:
                raise ValueError("El número de equipos debe ser par.")
            
            # Leer el valor mínimo y máximo
            minimo = int(archivo.readline().strip())
            maximo = int(archivo.readline().strip())

            # Leer la matriz de distancias (2(n-1) x n)
            distancias = []
            for i in range(2 * (n - 1)):
                fila = list(map(int, archivo.readline().strip().split()))
                distancias.append(fila)

        # Generamos las etiquetas para diferenciar cada equipo
        equipos = [f"Equipo {i+1}" for i in range(n)]

        # Crear la matriz de distancias (n x n)
        kilometros_matriz = [[0] * n for _ in range(n)]
        
        for i in range(len(distancias)):
            for j in range(len(distancias[i])):
                if distancias[i][j] > 0:
                    equipo1 = i
                    equipo2 = j
                    if i < j:  # Solo registrar las distancias de visitante a local
                        kilometros_matriz[equipo1][equipo2] = distancias[i][j]

        return equipos, minimo, maximo, kilometros_matriz, distancias
    except FileNotFoundError:
        raise ValueError("El archivo no fue encontrado.")
    except ValueError as e:
        raise ValueError(f"Error en los datos del archivo: {e}")
    except Exception as e:
        raise ValueError(f"Error al leer el archivo: {e}")

# Función para mostrar la matriz de distancias en el nuevo Text
def mostrar_matriz_distancias():
    # Limpiar el Text antes de insertar la nueva matriz
    matriz_text.delete(1.0, tk.END)

    matriz_text.insert(tk.END, "Matriz de Distancias:\n")
    for fila in distancias:
        matriz_text.insert(tk.END, " ".join(map(str, fila)) + "\n")

def generar_calendarios(equipos, kilometros_matriz):
    n = len(equipos)
    calendario_ida = []
    calendario_vuelta = []
    total_kilometros = 0

    # Generar el calendario de ida con alternancia de localía
    for i in range(n - 1):
        jornada_ida = []
        jornada_vuelta = []

        for j in range(n // 2):
            equipo1 = equipos[j]
            equipo2 = equipos[n - j - 1]

            # Alternar localía en ida
            if i % 2 == 0:
                jornada_ida.append(f"Jornada {i+1}: {equipo1} (Local) vs {equipo2} (Visitante)")
            else:
                jornada_ida.append(f"Jornada {i+1}: {equipo2} (Local) vs {equipo1} (Visitante)")

            # Alternar localía en vuelta (inversa a la ida)
            if i % 2 == 0:
                jornada_vuelta.append(f"Jornada {i+n}: {equipo2} (Local) vs {equipo1} (Visitante)")
            else:
                jornada_vuelta.append(f"Jornada {i+n}: {equipo1} (Local) vs {equipo2} (Visitante)")

            # Calcular kilómetros de ida
            index1 = equipos.index(equipo1)
            index2 = equipos.index(equipo2)
            total_kilometros += kilometros_matriz[index1][index2]
            total_kilometros += kilometros_matriz[index2][index1]  # Vuelta

        calendario_ida.append(jornada_ida)
        calendario_vuelta.append(jornada_vuelta)

        equipos.insert(1, equipos.pop())  # Rotar equipos para la siguiente jornada

    return calendario_ida, calendario_vuelta, total_kilometros
   
""" 
def calcular_distancias_recorridas(calendario_ida, calendario_vuelta, equipos, kilometros_matriz):
    # Inicializar distancias para cada equipo
    distancias_recorridas = {equipo: 0 for equipo in equipos}

    # Procesar los partidos de ida y vuelta
    for calendario in [calendario_ida, calendario_vuelta]:
        for jornada in calendario:
            for partido in jornada:
                try:
                    # Parsear el formato de partido
                    local = partido.split(" (Local) vs ")[0].split(": ")[1].strip()
                    visitante = partido.split(" (Visitante)")[0].split(" vs ")[1].strip()

                    # Obtener índices de los equipos
                    index_local = equipos.index(local)
                    index_visitante = equipos.index(visitante)

                    # Sumar la distancia recorrida por el visitante
                    distancia = kilometros_matriz[index_visitante][index_local]
                    distancias_recorridas[visitante] += distancia
                except Exception as e:
                    messagebox.showerror("Error", f"Error al calcular distancias: {e}")
                    return {}

    return distancias_recorridas
""" 
def calcular_distancias_recorridas(calendario_ida, calendario_vuelta, equipos, kilometros_matriz):
    # Inicializar distancias para cada equipo
    distancias_recorridas = {equipo: 0 for equipo in equipos}

    # Procesar los partidos de ida y vuelta
    for calendario in [calendario_ida, calendario_vuelta]:
        for jornada in calendario:
            for partido in jornada:
                try:
                    # Parsear el formato de partido
                    local = partido.split(" (Local) vs ")[0].split(": ")[1].strip()
                    visitante = partido.split(" (Visitante)")[0].split(" vs ")[1].strip()

                    # Obtener índices de los equipos
                    index_local = equipos.index(local)
                    index_visitante = equipos.index(visitante)

                    # Sumar la distancia recorrida por el visitante
                    distancia = kilometros_matriz[index_visitante][index_local]
                    distancias_recorridas[visitante] += distancia
                except Exception as e:
                    messagebox.showerror("Error", f"Error al calcular distancias: {e}")
                    return {}

    return distancias_recorridas

def ejecutar():
    try:
        # Generar calendarios
        calendario_ida, calendario_vuelta, _ = generar_calendarios(equipos, kilometros_matriz)
        calendario_text.delete(1.0, tk.END)

        jornada_num = 1
        # Mostrar los partidos de ida
        calendario_text.insert(tk.END, "Calendario de Ida:\n")
        for jornada in calendario_ida:
            calendario_text.insert(tk.END, f"Jornada {jornada_num}:\n")
            for partido in jornada:
                calendario_text.insert(tk.END, f"{partido}\n")
            jornada_num += 1

        # Mostrar los partidos de vuelta
        calendario_text.insert(tk.END, "\nCalendario de Vuelta:\n")
        for jornada in calendario_vuelta:
            calendario_text.insert(tk.END, f"Jornada {jornada_num}:\n")
            for partido in jornada:
                calendario_text.insert(tk.END, f"{partido}\n")
            jornada_num += 1

        # Calcular distancias recorridas
        distancias_recorridas = calcular_distancias_recorridas(calendario_ida, calendario_vuelta, equipos, kilometros_matriz)

        # Mostrar las distancias en un nuevo cuadro de texto
        distancias_text.delete(1.0, tk.END)
        distancias_text.insert(tk.END, "Distancias recorridas por equipo:\n")
        for equipo, distancia in distancias_recorridas.items():
            distancias_text.insert(tk.END, f"{equipo}: {distancia} km\n")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el calendario: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Calendarios")

# Crear frames para organizar la interfaz
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Widgets en la columna izquierda
cargar_btn = tk.Button(left_frame, text="Cargar archivo", command=cargar_archivo)
cargar_btn.grid(row=0, column=0, pady=5)

generar_btn = tk.Button(left_frame, text="Generar Calendarios", state=tk.DISABLED, command=ejecutar)
generar_btn.grid(row=1, column=0, pady=5)

distancias_label = tk.Label(right_frame, text="Distancias Recorridas:")
distancias_label.grid(row=4, column=0, sticky="w")

distancias_text = tk.Text(right_frame, height=10, width=50)
distancias_text.grid(row=5, column=0, pady=5)

equipos_label = tk.Label(left_frame, text="Equipos:")
equipos_label.grid(row=2, column=0, sticky="w")

equipos_lista = tk.Listbox(left_frame, height=10)
equipos_lista.grid(row=3, column=0, pady=5)

minimo_label = tk.Label(left_frame, text="Mínimo Locales:")
minimo_label.grid(row=4, column=0, sticky="w")

minimo_text = tk.Text(left_frame, height=1, width=10)
minimo_text.grid(row=5, column=0, pady=5)

maximo_label = tk.Label(left_frame, text="Máximo Locales:")
maximo_label.grid(row=6, column=0, sticky="w")

maximo_text = tk.Text(left_frame, height=1, width=10)
maximo_text.grid(row=7, column=0, pady=5)

# Widgets en la columna derecha
matriz_label = tk.Label(right_frame, text="Matriz de Distancias:")
matriz_label.grid(row=0, column=0, sticky="w")

matriz_text = tk.Text(right_frame, height=10, width=50)
matriz_text.grid(row=1, column=0, pady=5)

calendario_label = tk.Label(right_frame, text="Calendario:")
calendario_label.grid(row=2, column=0, sticky="w")

calendario_text = tk.Text(right_frame, height=20, width=100)
calendario_text.grid(row=3, column=0, pady=5)

# Ejecutar la interfaz
root.mainloop()