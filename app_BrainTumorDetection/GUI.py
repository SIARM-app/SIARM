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
        self.root.geometry("500x300")
        self.root.title("Aplicacion de deteccion de tumores cerebrales")

        # Centra la ventana en la pantalla
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # Crear contenedor de pestanas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(side=LEFT, fill=BOTH, expand=True)

        # Crear pestanas
        self.page1 = Frame(self.notebook)
        self.notebook.add(self.page1, text="Carga de Imagen")

        self.page2 = Frame(self.notebook)
        self.notebook.add(self.page2, text="Resultado")

        # Agregar contenido a Page 1 "Carga de Imagen"

        self.img_label = ttk.Label(self.page1)
        self.img_label.pack(padx=55, pady=40)

        # Crear el marco page1
        self.marco = tk.Frame(self.page1)
        self.marco.pack(side=tk.BOTTOM, padx=50, pady=20)

        label1 = ttk.Label(self.marco, text="Cargue una imagen para el estudio." , font=("Arial", 10, "bold"))
        label1.pack(side=TOP, pady=20)
        # Crear los botones
        self.load_button = tk.Button(self.marco, text="Cargar Imagen")
        self.check_button = tk.Button(self.marco, text="Comprobar")

        # Ubicar los botones uno al lado del otro
        self.load_button.pack(side=tk.LEFT, padx=20)
        self.check_button.pack(side=tk.LEFT, padx=20)

        # Agregar contenido a Page 2 "Resultados"

        self.marked_img_label = ttk.Label(self.page2)
        self.marked_img_label.pack(padx=55, pady=40)

        # Crear el marco page2
        self.contenedor_principal = tk.Frame(self.page2)
        self.contenedor_principal.pack(side=tk.BOTTOM, pady=20)

        self.marco2 = tk.Frame(self.contenedor_principal)
        self.marco2.pack(side=tk.LEFT, padx=30)

        self.marco3 = tk.Frame(self.contenedor_principal)
        self.marco3.pack(side=tk.LEFT, padx=30)

        label_page2 = ttk.Label(self.marco2, text="Los resultados son los siguientes: ", font=("Arial", 12))
        label_page2.pack(side=TOP)

        label_status = ttk.Label(self.marco3, text="Según el porcentaje del tumor con respecto al cerebro puede identificarse como: \nLeve, Moderado, Grave", font=("Arial", 10))
        label_status.pack(side=TOP)

        self.AreaT_result = ttk.Label(self.marco2, font=("Arial", 10, "bold"))
        self.AreaT_result.pack(side=BOTTOM)

        self.AreaC_result = ttk.Label(self.marco2, font=("Arial", 10, "bold"))
        self.AreaC_result.pack(side=BOTTOM)

        self.brainPercen_result = ttk.Label(self.marco2, font=("Arial", 10, "bold"))
        self.brainPercen_result.pack(side=BOTTOM)

        self.brainPercen_result_scale = ttk.Label(self.marco3, font=("Arial", 10, "bold"))
        self.brainPercen_result_scale.pack(side=BOTTOM)




