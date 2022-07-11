import pygame
import pygame_menu


pygame.init()
surface = pygame.display.set_mode((800, 500))

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

MARGEN=5 #MARGEN ENTRE CELDAS
LARGO=15 #LARGO DE CELDAS
ALTO=15  #ALTO DE LAS CELDAS
 
matriz=[[1,1],[1,1]]

def set_difficulty(value, difficulty):
    #setear la dificultad 
    pass

def start_the_game():
    
        #Crear el juego
        pantalla=pygame.display.set_mode((800,500))
        pantalla.fill(NEGRO)

        for fila in range(2):
            for columna in range(2):
                color = BLANCO
                if matriz[fila][columna] == 1:
                    color = VERDE
                pygame.draw.rect(pantalla,
                                color,
                                [(MARGEN+LARGO) * columna + MARGEN,
                                (MARGEN+ALTO) * fila + MARGEN,
                                LARGO,
                                ALTO])

menu = pygame_menu.Menu('BuscaCovid', 800, 500,
                       theme=pygame_menu.themes.THEME_DARK)

menu.add.selector('Dificultad :', [('Principiante', 1), ('Intermedio', 2), ('Avanzado', 3)], onchange=set_difficulty)
menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)