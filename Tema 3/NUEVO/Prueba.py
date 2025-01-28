import tkinter as tk 

#Crear la ventana
ventana = tk.Tk()

#Configurar la ventana
ventana.title("Mi primera app")
ventana.geometry("900x700")

#añadir la entrada de texto del usuario
entrada = tk.Entry(ventana)
entrada.pack()

#Funcion para mostrar la entrada
def mostrar_texto():
    texto = entrada.get()
    label.config(text=f"Escribiste: {texto}")

#Crear una etiqueta
label = tk.Label(ventana, text="Hola, mundo")
label.pack() #Empaqueta el texto

#Función para cambiar el texto
def cambiar_texto():
    label.config(text="Texto cambiado")

#Crear un botón
boton = tk.Button(ventana, text="Presióname",command=cambiar_texto)
boton.pack()

#Boton de entrada de texto
boton2 = tk.Button(ventana, text="Mostrar texto escrito", command=mostrar_texto)
boton2.pack()
#Mostrar la ventana hasta que el usuario la cierra
ventana.mainloop()