import pygame
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
 
LARGO  = 20
ALTO = 20
 
MARGEN = 5


#SE CREA LA MATRIZ FIJA DE 9X9 LA CUAL SERA MODIFICADA
matriz = []
for fila in range(9):
    matriz.append([])
    for columna in range(9):
        matriz[fila].append(0)
        
 
# Inicializamos pygame
pygame.init()
  
DIMENSION_VENTANA = [800, 500]

pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
 
 
# flag que determina termino del juego
hecho = False
 
#refresco pantalla
reloj = pygame.time.Clock()

#bucle del juego
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            matriz[fila][columna] = 1
 

    pantalla.fill(NEGRO)
 
    # Dibujamos constantemente la matriz
    for fila in range(9):
        for columna in range(9):
            color = BLANCO  #CELDA OCULTA DE MINA
            if matriz[fila][columna] == 1:  #EN CASO DE APRETAR UN BOTON CAMBIA A COLOR VERDE, AUN NO IMPLEMENTADO QUE EXISTA UNA BOMBA
                color = VERDE    #TAREA1-HU006
            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN,
                              (MARGEN+ALTO) * fila + MARGEN,
                              LARGO,
                              ALTO])
     
    # 60 FPS
    reloj.tick(60)
 
    # actualizar pantalla
    pygame.display.flip()
     
pygame.quit()