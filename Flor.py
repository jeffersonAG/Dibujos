from turtle import *

# Configuración inicial
color("greenyellow", "black")  # Establece los colores de la pluma y el relleno
title("Arte con Turtle")  # Título de la ventana
speed(-5)  # Establece la velocidad de dibujo
bgcolor("black")  # Establece el color de fondo
r, g, b = 200, 0, 0  # Inicializa los valores de color (rojo, verde, azul)

# Función para dibujar una flor
def fleur():
    for i in range(300):
        begin_fill()
        circle(190 - i, 90)  # Dibuja un cuarto de círculo
        left(90)
        circle(190 - i, 90)  # Dibuja el otro cuarto de círculo
        left(18)
        end_fill()

fleur()  # Llama a la función para dibujar la flor

mainloop()  # Mantén la ventana abierta
