import pygame
import pygame_menu


pygame.init()
surface = pygame.display.set_mode((800, 500))

def set_difficulty(value, difficulty):
    #setear la dificultad 
    pass

def start_the_game():
    #Crear el juego
    pass

menu = pygame_menu.Menu('BuscaCovid', 800, 500,
                       theme=pygame_menu.themes.THEME_DARK)

menu.add.selector('Dificultad :', [('Principiante', 1), ('Intermedio', 2), ('Avanzado', 3)], onchange=set_difficulty)
menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)