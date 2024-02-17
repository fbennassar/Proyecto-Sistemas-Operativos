"""francisco's branch"""

import tkinter as tk
import os

app = tk.Tk()
app.geometry("800x600")
app.title("Explorador de archivos")

label = tk.Label(app, text="Explorador de archivos", anchor='center', font=("Arial", 20), justify='center')
label.pack(fill=tk.X, padx=10, pady=10)

# Comandos de los botones
def crear():
    print("Crear")

def renombrar():
    print("Renombrar")

def eliminar():
    print("Eliminar")

def mover():
    print("Mover")

def abrir_archivos(event):
    print("Abrir Archivos")

def cambiar_ruta():
    print("Cambiar Ruta")

def abrir_archivos_manual():
    print("Abrir Archivos")

# Frame es algo asi como un div en html
button_frame = tk.Frame(app)
button_frame.pack()

# Crear Botones
crear_button = tk.Button(button_frame, text="Crear", command=crear)
crear_button.pack(side='left', padx=10)

renombrar_button = tk.Button(button_frame, text="Renombrar", command=renombrar)
renombrar_button.pack(side='left', padx=10)

eliminar_button = tk.Button(button_frame, text="Eliminar", command=eliminar)
eliminar_button.pack(side='left', padx=10)

mover_button = tk.Button(button_frame, text="Mover", command=mover)
mover_button.pack(side='left', padx=10)

cambiar_ruta_button = tk.Button(button_frame, text="Cambiar Ruta", command=cambiar_ruta)
cambiar_ruta_button.pack(side='left', padx=10)

# Etiqueta de la ruta
# OJO debe ser la ruta de la carpeta que se va a explorar, esta ruta cambia en cada PC
INITIALPATH = 'c:/Users/PC/Documents'
path_label = tk.Label(app, text="Ruta: " + INITIALPATH , anchor='center', font=("Arial", 10), justify='center')
path_label.pack(fill=tk.X, padx=10, pady=10)
cambiar_ruta = tk.Entry(app)
cambiar_ruta.pack(fill=tk.X, padx=10, pady=10)

# Lista de los archivos
listbox = tk.Listbox(app)
listbox.pack(fill='both', expand=True, padx=10)

# Donde toma los archivos
files_and_dirs = os.listdir('c:/Users/PC/Documents')

# Recorre todo el directorio y lo muestra en la lista
for item in files_and_dirs:
    listbox.insert('end', item)

# Scrollbar
scrollbar = tk.Scrollbar(listbox)
scrollbar.pack(side='right', fill='y')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Evento doble click
listbox.bind('<Double-Button-1>', abrir_archivos)

# Crear otro frame para los botones de abrir archivo
bottom_frame = tk.Frame(app)
bottom_frame.pack(side='bottom', fill='x', pady=40 )

# Etiqueta para el archivo seleccionado
abrir_archivos_label = tk.Label(bottom_frame, text="Archivo seleccionado:", padx=10)
abrir_archivos_label.pack(side='left')

# Donde se ingresa manualmente el archivo
file_path = tk.Entry(bottom_frame, width=50)
file_path.pack(side='left')

# Boton para abrir el archivo
open_button = tk.Button(bottom_frame, text="Abrir archivo", command=abrir_archivos_manual)
open_button.pack(side='left', padx=10)

# Create a Label to display the file path
file_path_label = tk.Label(bottom_frame, textvariable=file_path)
file_path_label.pack(side='left')


app.mainloop()
