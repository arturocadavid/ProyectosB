import tkinter
from PIL import Image, ImageTk
import random

# Ventana principal del programa
root = tkinter.Tk()
root.geometry('400x400')
root.title('Lanza el dado by Arturo Cadavid')

l0 = tkinter.Label(root, text="")
l0.pack()

# Titulo del juego con diferente fuente y formato
l1 = tkinter.Label(root, text="Dados al azar", fg = "light blue",
        bg = "dark blue",
        font = "Helvetica 16 bold italic")
l1.pack()

# imagenes
dice = ['Dados/die1.png', 'Dados/die2.png', 'Dados/die3.png', 'Dados/die4.png', 'Dados/die5.png', 'Dados/die6.png']
# simulando los dados eligiendo entre 1 a 6 imagenes
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Label para las imagenes
label1 = tkinter.Label(root, image=image1)
label1.image = image1

label1.pack( expand=True)

# Activar la funcion por un boton
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # actualiza imagen
    label1.configure(image=image1)
    # mantiene la referencia
    label1.image = image1


# Agregar botón, y el comando usará la función rolling_dice
button = tkinter.Button(root, text='Lanza el dado', fg='blue', command=rolling_dice)

button.pack( expand=True)

#Abre el programa y lo mantiene abierto
root.mainloop()