"""francisco's branch"""

import tkinter as tk
import os
import shutil

app = tk.Tk()
app.geometry("800x600")
app.title("Explorador de archivos")
listbox = tk.Listbox(app)

# pylint: disable=global-statement
# pylint: disable=missing-function-docstring

label = tk.Label(app, text="Explorador de archivos", anchor='center', font=("Arial", 20), justify='center')
label.pack(fill=tk.X, padx=10, pady=10)
actual_path = 'c:\\Users\\franb\\OneDrive\\Documents'

# Comandos de los botones
def crear():
    # Crear una nueva ventana
    create_window = tk.Toplevel(app)
    create_window.title("Crear")
    create_window.geometry("300x250")

    # Crear un campo de entrada para el nombre del nuevo archivo/carpeta
    new_name_entry = tk.Entry(create_window)
    new_name_entry.pack()

    # Crear una función para crear el nuevo archivo o carpeta
    def create_new_folder():
        new_name = new_name_entry.get()
        new_path = os.path.join(actual_path, new_name)
        if not os.path.exists(new_path):
            # Aquí puedes decidir si quieres crear un archivo o una carpeta
            # Para crear una carpeta:
            os.mkdir(new_path)
            # Para crear un archivo:
            # open(new_path, 'a').close()
            # Actualizar el Listbox principal
            listbox.delete(0, 'end')
            files_and_dirs = os.listdir(actual_path)
            for item in files_and_dirs:
                listbox.insert('end', item)
            # Cerrar la ventana de crear
            create_window.destroy()
        else:
            print("El archivo o carpeta ya existe")

    def create_new_file():
        new_name = new_name_entry.get()
        new_path = os.path.join(actual_path, new_name)
        if not os.path.exists(new_path):
            # Aquí puedes decidir si quieres crear un archivo o una carpeta
            # Para crear una carpeta:
            # os.mkdir(new_path)
            # Para crear un archivo:
            open(new_path, 'a').close()
            # Actualizar el Listbox principal
            listbox.delete(0, 'end')
            files_and_dirs = os.listdir(actual_path)
            for item in files_and_dirs:
                listbox.insert('end', item)
            # Cerrar la ventana de crear
            create_window.destroy()
        else:
            print("El archivo o carpeta ya existe")
    # Crear un botón para crear el nuevo archivo o carpeta
    create_folder_button = tk.Button(create_window, text="Crear Carpeta", command=create_new_folder)
    create_folder_button.pack()

    create_file_button = tk.Button(create_window, text="Crear Archivo", command=create_new_file)
    create_file_button.pack()

def renombrar():
    # Crear una nueva ventana
    rename_window = tk.Toplevel(app)
    rename_window.title("Renombrar")
    rename_window.geometry("300x250")


    # Crear un Listbox para mostrar los archivos y carpetas
    rename_listbox = tk.Listbox(rename_window)
    rename_listbox.pack(fill=tk.X, padx=10, pady=10)

    # Rellenar el Listbox con los archivos y carpetas actuales
    files_and_dirs = os.listdir(actual_path)
    for item in files_and_dirs:
        rename_listbox.insert('end', item)

    # Crear un campo de entrada para el nuevo nombre
    new_name_entry = tk.Entry(rename_window)
    new_name_entry.pack()

    # Crear una función para renombrar el archivo o carpeta seleccionado
    def rename_selected():
        selected = rename_listbox.get(rename_listbox.curselection())
        new_name = new_name_entry.get()
        os.rename(os.path.join(actual_path, selected), os.path.join(actual_path, new_name))
        # Actualizar el Listbox principal
        listbox.delete(0, 'end')
        files_and_dirs = os.listdir(actual_path)
        for item in files_and_dirs:
            listbox.insert('end', item)
        # Cerrar la ventana de renombrar
        rename_window.destroy()

    # Crear un botón para renombrar el archivo o carpeta seleccionado
    rename_button = tk.Button(rename_window, text="Renombrar", command=rename_selected)
    rename_button.pack()

def eliminar():
    # Crear una nueva ventana
    delete_window = tk.Toplevel(app)
    delete_window.title("Eliminar")
    delete_window.geometry("300x250")

    # Crear un Listbox para mostrar los archivos y carpetas
    delete_listbox = tk.Listbox(delete_window)
    delete_listbox.pack(fill=tk.X, padx=10, pady=10)

    # Rellenar el Listbox con los archivos y carpetas actuales
    files_and_dirs = os.listdir(actual_path)
    for item in files_and_dirs:
        delete_listbox.insert('end', item)

    # Crear una función para eliminar el archivo o carpeta seleccionado
    def delete_selected():
        selected = delete_listbox.get(delete_listbox.curselection())
        if os.path.isfile(os.path.join(actual_path, selected)):
            os.remove(os.path.join(actual_path, selected))
        else:
            shutil.rmtree(os.path.join(actual_path, selected))
        # Actualizar el Listbox principal
        listbox.delete(0, 'end')
        files_and_dirs = os.listdir(actual_path)
        for item in files_and_dirs:
            listbox.insert('end', item)
        # Cerrar la ventana de eliminar
        delete_window.destroy()

    # Crear un botón para eliminar el archivo o carpeta seleccionado
    delete_button = tk.Button(delete_window, text="Eliminar", command=delete_selected)
    delete_button.pack()


def mover():
    print("Mover")

def abrir_archivos(event):
    global actual_path
    seleccionado = listbox.get(listbox.curselection())
    ruta_completa = os.path.join(actual_path, seleccionado)
    if os.path.isfile(ruta_completa):
        os.startfile(ruta_completa)
    elif os.path.isdir(ruta_completa):
        actual_path = ruta_completa
        path_label.config(text="Ruta: " + actual_path)
        files_and_dirs = os.listdir(actual_path)
        listbox.delete(0, 'end')
        for item in files_and_dirs:
            listbox.insert('end', item)

listbox.bind('<Double-Button-1>', abrir_archivos)

def cambiar_ruta():
    global actual_path
    global files_and_dirs
    nueva_ruta = cambiar_ruta_input.get()
    if os.path.exists(nueva_ruta):
        actual_path = nueva_ruta
        path_label.config(text="Ruta: " + actual_path)
        files_and_dirs = os.listdir(actual_path)
        listbox.delete(0, 'end')
        for files in files_and_dirs:
            listbox.insert('end', files)
    else:
        print("La ruta no existe")

def abrir_archivos_manual():
    global actual_path
    seleccionado = file_path.get()
    ruta_completa = os.path.join(actual_path, seleccionado)
    if os.path.isfile(ruta_completa):
        os.startfile(ruta_completa)
    elif os.path.isdir(ruta_completa):
        actual_path = ruta_completa
        path_label.config(text="Ruta: " + actual_path)
        files_and_dirs = os.listdir(actual_path)
        listbox.delete(0, 'end')
        for item in files_and_dirs:
            listbox.insert('end', item)

def ir_atras():
    global actual_path
    global files_and_dirs
    ultimo_slash = actual_path.rfind('\\')
    if ultimo_slash != -1:
        actual_path = actual_path[:ultimo_slash]
        path_label.config(text="Ruta: " + actual_path)
        files_and_dirs = os.listdir(actual_path)
        listbox.delete(0, 'end')
        for item in files_and_dirs:
            listbox.insert('end', item)
    else:
        print("Ya estás en la raíz")

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
# OJO debe ser la ruta de la carpeta que se va a explorar, esta ruta cambia en cada PC

path_label = tk.Label(app, text="Ruta: " + actual_path , anchor='center', font=("Arial", 10), justify='center')
path_label.pack(fill=tk.X, padx=10, pady=10)

cambiar_ruta_frame = tk.Frame(app)
cambiar_ruta_frame.pack(fill=tk.X, padx=10, pady=10)
cambiar_ruta_label = tk.Label(cambiar_ruta_frame, text="Nueva Ruta:", font=("Arial", 10))
cambiar_ruta_label.pack(side='left')
cambiar_ruta_input = tk.Entry(cambiar_ruta_frame, width=50, font=("Arial", 10))
cambiar_ruta_input.pack(side='left', padx=10)

cambiar_ruta_button = tk.Button(cambiar_ruta_frame, text="Cambiar Ruta", command=cambiar_ruta)
cambiar_ruta_button.pack(side='left', padx=10)

ir_atras_button = tk.Button(path_label, text="Ir Atras", command=ir_atras)
ir_atras_button.pack(side='left', padx=10)

# Lista de los archivos

listbox.pack(fill='both', expand=True, padx=10)

# Donde toma los archivos
files_and_dirs = os.listdir('c:/Users/franb/OneDrive/Documents')

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
