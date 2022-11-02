import tkinter
from tkinter import ttk



window = tkinter.Tk()
window.title("Lista desplegable")
window.geometry('300x190')


#Geometria mediante grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

def obtener_info():
    print(lista_desplegable.current())



username_label = ttk.Label(window, text="Seleccione una opción:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

lista_desplegable = ttk.Combobox(window, width=17)
lista_desplegable.grid(column=2, row=0, sticky=tkinter.W, padx=5, pady=5)

opciones = ["opcion1", "opcion2","opcion3","opcion4"]

lista_desplegable['values'] = opciones

boton_get = ttk.Button(window,text="Obtener", command=obtener_info)
boton_get.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

window.mainloop()