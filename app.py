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

# Etiqueta de la ruta
INITIALPATH = 'C:/Users/franb/OneDrive/Documents'
path_label = tk.Label(app, text="Ruta: " + INITIALPATH , anchor='center', font=("Arial", 10), justify='center')
path_label.pack(fill=tk.X, padx=10, pady=10)


# Lista de los archivos
listbox = tk.Listbox(app)
listbox.pack(fill='both', expand=True)


# Donde toma los archivos
files_and_dirs = os.listdir('C:/Users/franb/OneDrive/Documents')

# Recorre todo el directorio y lo muestra en la lista
for item in files_and_dirs:
    listbox.insert('end', item)

listbox.bind('<Double-Button-1>', abrir_archivos)


app.mainloop()
