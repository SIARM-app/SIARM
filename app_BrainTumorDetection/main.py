from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from GUI import *

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
            img = img.resize((500, 500), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            gui.img_label.config(image=photo)
            gui.img_label.image = photo
        except:
            messagebox.showerror("Error", "No se pudo abrir la imagen.")


# def open_file():
#     file_path = filedialog.askopenfilename()
#     img = Image.open(file_path)
#     img = img.resize((500, 500), Image.LANCZOS)
#     photo = ImageTk.PhotoImage(img)
#     img_Label = Label(gui.page1, image=photo)
#     img_Label.image = photo
#     img_Label.pack(side=TOP, padx=55, pady=100)
# img_label = Label(gui.root, width=500, height=500)
# img_label.pack()

gui.load_button.config(command=open_file)

gui.root.mainloop()
