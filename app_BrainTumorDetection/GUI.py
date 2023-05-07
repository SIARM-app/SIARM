from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image


class MyGui:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("900x600")
        # Centra la ventana en la pantalla
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        notebook = ttk.Notebook(self.root, width=900, height=600)
        notebook.pack(side=LEFT, fill=BOTH, expand=True)

        # Crear pestanas
        self.page1 = Frame(notebook)
        notebook.add(self.page1, text="Carga de Imagen")
        self.page2 = Frame(notebook)
        notebook.add(self.page2, text="Resultado")

        # Agregar contenido a las páginas
        label1 = Label(self.page1, text="Cargue una imagen para el estudio. ")
        label1.pack(padx=10, pady=10)
        label2 = Label(self.page2, text="Si tiene cancer :(")
        label2.pack(padx=10, pady=10)

        # Agregar un botón para cargar la imagen
        self.load_button = Button(self.page1, text="Cargar imagen")
        self.load_button.pack(side=BOTTOM, padx=50, pady=20)

        self.img_label = Label(self.page1)
        self.img_label.pack(side=TOP, padx=55, pady=100)



        image = Image.open("./Images/Hugod.jpeg")
        # Escalar la imagen al tamaño deseado
        image = image.resize((400, 400), Image.LANCZOS)
        # Convertir la imagen a un objeto compatible con tkinter
        photo = ImageTk.PhotoImage(image)
        # Mostrar la imagen en la página 2
        label2 = Label(self.page2, image=photo)
        label2.image = photo
        label2.pack(padx=10, pady=10)






