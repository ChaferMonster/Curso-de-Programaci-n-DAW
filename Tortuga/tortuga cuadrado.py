import turtle

#Lo primero es añadir la pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("white")

#Añadir el pincel tortuga

tortuga = turtle.Turtle()
tortuga.pensize(2)

#Dibujo
for i in range(4):
    tortuga.forward(100)
    tortuga.left(90)

pantalla.mainloop()