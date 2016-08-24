import pygame

pygame.init()

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
PI = 3.141592653

dimensiones = (700, 500)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption('Super juego del profesor Craven')

# Itera hasta que cierre la ventana
hecho = False

# Se usa para gestionar el refrescado de la pantalla
reloj = pygame.time.Clock()


# -------- Bucle principal del juego -----
while not hecho:
    # Procesado de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # han pulsado la x
            hecho = True
    # fin procesado de eventos

    # Logica del juego

    # fin logica del juego

    # codigo de dibujado

    # fin codigo de dibujado

    # limita a 20 fotogramas por segundo
    reloj.tick(20)
