import tkinter as tk

window = tk.Tk()
window.title("Finestra di prova")
window.geometry("600x600")
window.resizable(True, True)
window.configure(background="purple")
bg_color = "lightblue"
font = ("Helvetica", 30)


# label = tk.Label(window, text="CALCOLATRICE")
# label.pack(pady=10)
def risultato(ris):
    output_ris = tk.Label(
        window, text="00000000000000000000000", fg="#000000", font=font)
    output_ris.grid(row=2, column=0, columnspan=4, sticky="N")
    output_ris = tk.Label(window, text=ris, fg="#0000FF", font=font)
    output_ris.grid(row=2, column=0, columnspan=4, sticky="N")


def somma():
    num1 = int(input_num1.get())
    num2 = int(input_num2.get())
    ris = num1+num2
    risultato(ris)


def sottrazione():
    num1 = int(input_num1.get())
    num2 = int(input_num2.get())
    ris = num1-num2
    risultato(ris)


def moltiplicazione():
    num1 = int(input_num1.get())
    num2 = int(input_num2.get())
    ris = num1*num2
    risultato(ris)


def divisione():
    num1 = int(input_num1.get())
    num2 = int(input_num2.get())
    if num2 == 0:
        if num1 == 0:
            ris = "INDEFINITO"
        else:
            ris = "IMPOSSIBILE"
    else:
        ris = round((num1/num2), 2)
    risultato(ris)


input_num1 = tk.Entry(window)
input_num1.grid(row=0, column=0, columnspan=2, sticky="N")

input_num2 = tk.Entry(window)
input_num2.grid(row=0, column=2, columnspan=2, sticky="N")

pulsante1 = tk.Button(text="+", command=somma)
pulsante1.grid(row=1, column=0, sticky="NSEW")
pulsante2 = tk.Button(text="-", command=sottrazione)
pulsante2.grid(row=1, column=1, sticky="NSEW")
pulsante3 = tk.Button(text="x", command=moltiplicazione)
pulsante3.grid(row=1, column=2, sticky="NSEW")
pulsante4 = tk.Button(text=":", command=divisione)
pulsante4.grid(row=1, column=3, sticky="NSEW")


if __name__ == "__main__":
    window.mainloop()
