import pygame
from maze import Maze
from turing_machine import TuringMachine

# --- Configuración ---
# ¡Prueba cambiar este número!
# DEBE SER IMPAR para que el generador funcione bien (ej. 15, 25, 35).
MAZE_SIZE = 15 
FPS = 20 # Sube esto para que el "bichito" vaya más rápido

# --- Inicialización ---
pygame.init()

# --- Crear Objetos ---
# 1. Crear el laberinto primero
maze = Maze(MAZE_SIZE) 

# 2. La TM empieza en (0,0)
bug_tm = TuringMachine(maze, start_row=0, start_col=0)

# --- Configuración de la Ventana (basado en el laberinto) ---
# Leemos el cell_size y el 'n' final del objeto laberinto
# (n podría haber cambiado si MAZE_SIZE era par)
CELL_SIZE = maze.cell_size 
WINDOW_SIZE = maze.n * CELL_SIZE 

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Simulador de Máquina de Turing en Laberinto")
clock = pygame.time.Clock()


# --- Bucle Principal ---
running = True
while running:
    # 1. Manejo de Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Lógica (Actualizar el estado de la TM)
    # Ejecutamos varios pasos por fotograma para acelerar
    # (puedes ajustar el 'range' o ponerlo en 1 para ir paso a paso)
    for _ in range(1): # Cambia el 1 para acelerar la simulación
        if not bug_tm.halted:
            bug_tm.step()

    # 3. Dibujo (Renderizado)
    screen.fill((255, 255, 255)) # Fondo blanco
    
    # Dibuja el estado actual del laberinto (paredes, visitados, etc.)
    maze.draw(screen, pygame)
    
    # Dibuja la posición actual del "bichito"
    bug_tm.draw_bug(screen, pygame, maze.cell_size)

    # 4. Actualizar Pantalla
    pygame.display.flip()
    
    # 5. Controlar FPS (velocidad de la simulación)
    clock.tick(FPS)

pygame.quit()