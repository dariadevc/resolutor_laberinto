import pygame
from maze import Maze
from turing_machine import TuringMachine

# --- Configuración ---
MAZE_SIZE = 5 # El 'n' de tu laberinto
CELL_SIZE = 40 # Tamaño en píxeles de cada celda
WINDOW_SIZE = MAZE_SIZE * CELL_SIZE
FPS = 5 # Controla la velocidad del "bichito"

# --- Inicialización ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Simulador de Máquina de Turing en Laberinto")
clock = pygame.time.Clock()

# --- Crear Objetos ---
maze = Maze(MAZE_SIZE)
# Asignamos el laberinto a la TM y le damos una posición inicial
bug_tm = TuringMachine(maze, start_row=0, start_col=0)


# --- Bucle Principal ---
running = True
while running:
    # 1. Manejo de Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Lógica (Actualizar el estado de la TM)
    if not bug_tm.halted:
        bug_tm.step()

    # 3. Dibujo (Renderizado)
    screen.fill((255, 255, 255)) # Fondo blanco por si acaso
    
    # Dibuja el estado actual del laberinto (paredes, visitados, etc.)
    maze.draw(screen, pygame)
    
    # Dibuja la posición actual del "bichito"
    bug_tm.draw_bug(screen, pygame, maze.cell_size)

    # 4. Actualizar Pantalla
    pygame.display.flip()
    
    # 5. Controlar FPS (velocidad de la simulación)
    clock.tick(FPS)

pygame.quit()