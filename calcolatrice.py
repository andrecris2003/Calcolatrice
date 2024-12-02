from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Calcolatrice")
window.geometry("600x600")
window.resizable(False, False)
window.configure(background="purple")
bg_color = "lightblue"
font = ("Helvetica", 30)
font2 = ("Helvetica", 20)

background_image = tk.PhotoImage(
    file="/home/its/Desktop/PYTHON/Python2/Calcolatrice/image.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# label = tk.Label(window, text="CALCOLATRICE")
# label.pack(pady=10)


def risultato(ris):
    output_ris = tk.Label(
        window, text="00000000000000001", background="#FFFFFF", fg="#FFFFFF", font=font)
    output_ris.grid(row=3, column=0, columnspan=4, sticky="NWE", padx=(100, 0))
    output_ris = tk.Label(window, text=ris, fg="#0000FF",
                          background="#FFFFFF", font=font)
    output_ris.grid(row=3, column=0, columnspan=4, sticky="N", padx=(100, 0))


def somma():
    try:
        num1 = int(input_num1.get())
    except ValueError:
        num1 = 0
    try:
        num2 = int(input_num2.get())
    except ValueError:
        num2 = 0
    ris = num1+num2
    risultato(ris)


def sottrazione():
    try:
        num1 = int(input_num1.get())
    except ValueError:
        num1 = 0
    try:
        num2 = int(input_num2.get())
    except ValueError:
        num2 = 0
    ris = num1-num2
    risultato(ris)


def moltiplicazione():
    try:
        num1 = int(input_num1.get())
    except ValueError:
        num1 = 0
    try:
        num2 = int(input_num2.get())
    except ValueError:
        num2 = 0
    ris = num1*num2
    risultato(ris)


def divisione():
    try:
        num1 = int(input_num1.get())
    except ValueError:
        num1 = 0
    try:
        num2 = int(input_num2.get())
    except ValueError:
        num2 = 0
    if num2 == 0:
        if num1 == 0:
            ris = "INDEFINITO"
        else:
            ris = "IMPOSSIBILE"
    else:
        ris = round((num1/num2), 2)
    risultato(ris)


titolo = tk.Label(window, text="CALCOLATRICE",
                  background="white", fg="blue", font=font)
titolo.grid(row=0, column=0, columnspan=4,
            sticky="NWE", pady=(30, 0), padx=(100, 0))
output_ris = tk.Label(
    window, text="100000andrea000001", background="#FFFFFF", fg="#FFFFFF", font=font)
output_ris.grid(row=3, column=0, columnspan=4, sticky="NWE", padx=(100, 0))
output_ris = tk.Label(
    window, text="risultato", background="#FFFFFF", fg="#0000FF", font=font2)
output_ris.grid(row=3, column=0, columnspan=4, sticky="NS", padx=(100, 0))

input_num1 = tk.Entry(window)
input_num1.grid(row=1, column=0, columnspan=2, sticky="NWE", padx=(100, 0))

input_num2 = tk.Entry(window)
input_num2.grid(row=1, column=2, columnspan=2, sticky="NWE")

pulsante1 = tk.Button(text="+", command=somma)
pulsante1.grid(row=2, column=0, sticky="NWE", padx=(100, 0))
pulsante2 = tk.Button(text="-", command=sottrazione)
pulsante2.grid(row=2, column=1, sticky="NWE")
pulsante3 = tk.Button(text="x", command=moltiplicazione)
pulsante3.grid(row=2, column=2, sticky="NWE")
pulsante4 = tk.Button(text=":", command=divisione)
pulsante4.grid(row=2, column=3, sticky="NWE")

if __name__ == "__main__":
    window.mainloop()
