from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from Gui import *
from Model import *



gui = MyGui()
image_path = None


def open_file():
    global image_path
    if image_path:
        result = messagebox.askyesno("Cambiar imagen", "¿Desea cambiar la imagen actual?")
        if not result:
            return
    image_path = filedialog.askopenfilename()
    if image_path:
        try:
            img = Image.open(image_path)
            #img = img.resize((500, 350), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            gui.img_label.configure(image=photo)
            gui.img_label.image = photo
            gui.root.state('zoomed')
            #gui.notebook.imagen_tk = photo
            #gui.img_label.config(image=photo)
            #gui.img_label.image = photo


        except:
            messagebox.showerror("Error", "No se pudo abrir la imagen.")

def check_Image():
    AreaT, AreaC, brainPercen, marked_image_path_TUMOR = modelfunction(image_path)
    markedImg = Image.open(marked_image_path_TUMOR)
    # img = img.resize((500, 350), Image.LANCZOS)
    markedPhoto = ImageTk.PhotoImage(markedImg)
    gui.marked_img_label.configure(image=markedPhoto)
    gui.marked_img_label.image = markedPhoto
    gui.notebook.select(gui.page2)

    gui.AreaT_result.config(text="Area del tumor: " + str(AreaT))
    gui.AreaC_result.config(text="Area del cerebro: " + str(AreaC))
    gui.brainPercen_result.config(text= "El porcentaje del cerebro que se dectó como tumor es: " + str(brainPercen) + "%")

    if brainPercen >= 0 and brainPercen <= 10:
        gui.brainPercen_result_scale.config(text= "Estado del Cerebro: Leve")
    elif brainPercen > 10 and brainPercen <= 20:
        gui.brainPercen_result_scale.config(text= "Estado del Cerebro: Moderado")
    else:
        gui.brainPercen_result_scale.config(text= "Estado del Cerebro: Grave")


gui.load_button.config(command=open_file)
gui.check_button.config(command=check_Image)
gui.root.mainloop()
