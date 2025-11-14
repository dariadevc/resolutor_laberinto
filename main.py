import pygame
import random
from camino.camino import Camino 
from camino.maquina_turing import MaquinaTuring
from camino.controlador_animacion import ControladorAnimacion

# CONSTANTES
PARED = '1'
CAMINO = '0'
VISITADO = 'V'
SALIDA = 'E'
TAMANIO_CELDA = 40
FPS = 7

# Laberintos estáticos
# ========== LABERINTOS 7x7 ==========
maze_7x7_1 = [
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '1', '1'],
    ['1', '1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', 'E', '1']
]

maze_7x7_2 = [
    ['1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '0', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', 'E', '1', '1', '1', '1', '1']
]

maze_7x7_3 = [
    ['1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '1', '1'],
    ['1', '1', '1', '0', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '1', '1'],
    ['1', 'E', '1', '1', '1', '1', '1']
]

maze_7x7_4 = [
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', 'E', '1']
]

# ========== LABERINTOS 9x9 ==========
maze_9x9_1 = [
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

maze_9x9_2 = [
    ['1', '1', '1', '1', '0', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '0', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

maze_9x9_3 = [
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '0', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '0', '0', '0', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1', 'E', '1', '1']
]

maze_9x9_4 = [
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

# ========== LABERINTOS 11x11 ==========
maze_11x11_1 = [
    ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', 'E', '1', '1', '1']
]

maze_11x11_2 = [
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

maze_11x11_3 = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1'],
    ['1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1'],
    ['1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', 'E', '1', '1', '1', '1', '1', '1', '1', '1']
]

maze_11x11_4 = [
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

# ========== LABERINTOS 15x15 CORREGIDOS ==========
maze_15x15_1 = [
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

maze_15x15_2 = [
    ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

maze_15x15_3 = [
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]

maze_15x15_4 = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
]


caminos_posibles = [
    maze_7x7_1, 
    maze_7x7_2, 
    maze_7x7_3,
    maze_7x7_4,
    maze_9x9_1, 
    maze_9x9_2, 
    maze_9x9_3,
    maze_9x9_4,
    maze_11x11_1,
    maze_11x11_2,
    maze_11x11_3,
    maze_11x11_4,
    maze_15x15_1,
    maze_15x15_2,
    maze_15x15_3,
    maze_15x15_4
]

# --- Variables globales ---
CAMINO_ELEGIDO = None
camino = None
maquina_turing = None
controlador_animacion = None
pantalla = None
TAMANIO_VENTANA_ACTUAL = None
MARGEN_X = 0
MARGEN_Y = 0

# --- Funciones auxiliares ---
def crear_ventana(n_ventana):
    global pantalla, TAMANIO_VENTANA_ACTUAL
    
    TAMANIO_VENTANA_ACTUAL = n_ventana * TAMANIO_CELDA
    ALTURA_EXTRA = 100
    
    # Crear nueva ventana
    nueva_pantalla = pygame.display.set_mode((TAMANIO_VENTANA_ACTUAL, TAMANIO_VENTANA_ACTUAL + ALTURA_EXTRA))
    pygame.display.set_caption("Simulador de Máquina de Turing")
    
    return nueva_pantalla, TAMANIO_VENTANA_ACTUAL

def calcular_margenes(n_ventana):
    global TAMANIO_VENTANA_ACTUAL
    if TAMANIO_VENTANA_ACTUAL is None:
        return 0, 0
    
    tamaño_laberinto = n_ventana * TAMANIO_CELDA
    margen_x = (TAMANIO_VENTANA_ACTUAL - tamaño_laberinto) // 2
    margen_y = 0
    
    return margen_x, margen_y

def reiniciar_simulacion():
    global CAMINO_ELEGIDO, camino, maquina_turing, controlador_animacion, pantalla, TAMANIO_VENTANA_ACTUAL, MARGEN_X, MARGEN_Y
    
    # Selecciona nuevo camino aleatorio
    CAMINO_ELEGIDO = random.choice(caminos_posibles)
    N_VENTANA = len(CAMINO_ELEGIDO)

    # ACTUALIZAR VENTANA Y MÁRGENES
    pantalla, TAMANIO_VENTANA_ACTUAL = crear_ventana(N_VENTANA)
    MARGEN_X, MARGEN_Y = calcular_margenes(N_VENTANA)
    
    # Recrea los objetos
    camino = Camino(
        static_grid=CAMINO_ELEGIDO,
        tamanio_celda=TAMANIO_CELDA,
        tile_images=imagenes_tiles_cargadas
    )
    
    fila_inicio = 0
    col_inicio = -1 
    for indice_col, val_celda in enumerate(CAMINO_ELEGIDO[fila_inicio]):
        if val_celda == CAMINO:
            col_inicio = indice_col
            break
    
    maquina_turing = MaquinaTuring(
        camino=camino, 
        fila_inicio=fila_inicio, 
        col_inicio=col_inicio
    )

    controlador_animacion = ControladorAnimacion(imagenes_personaje_cargadas)
    
    print("\n=== NUEVA SIMULACIÓN ===")
    cadena_entrada = camino.get_cadena_camino()
    cadena_salida = maquina_turing.get_cadena_salida()
    print("Cadena de entrada:", cadena_entrada, "\n")
    print("Cadena de salida:", cadena_salida, "\n")

    return cadena_entrada, cadena_salida

# def dibujar_texto(surface, texto, posicion, color=(255, 255, 255), tamanio=24):
#     """Dibuja texto en la superficie"""
#     fuente = pygame.font.Font(None, tamanio)

#     ancho_maximo = surface.get_width() - 20
#     palabras = texto.split(' ')
#     lineas = []
#     linea_actual = ""

#     for palabra in palabras:
#         # Probar si la palabra cabe en la línea actual
#         texto_prueba = linea_actual + " " + palabra if linea_actual else palabra
#         ancho_texto = fuente.size(texto_prueba)[0]
        
#         if ancho_texto <= ancho_maximo:
#             linea_actual = texto_prueba
#         else:
#             # Si no cabe, guardar la línea actual y empezar nueva línea
#             if linea_actual:
#                 lineas.append(linea_actual)
#             linea_actual = palabra
    
#     # Añadir la última línea
#     if linea_actual:
#         lineas.append(linea_actual)
    
#     # Dibujar cada línea
#     x, y = posicion
#     for linea in lineas:
#         texto_surface = fuente.render(linea, True, color)
#         surface.blit(texto_surface, (x, y))
#         y += fuente.get_linesize()  # Mover a la siguiente línea

def dibujar_boton(surface, rect, texto, color_normal, color_hover, mouse_pos):
    """Dibuja un botón interactivo"""
    color = color_hover if rect.collidepoint(mouse_pos) else color_normal
    pygame.draw.rect(surface, color, rect, border_radius=8)
    pygame.draw.rect(surface, (200, 200, 200), rect, 2, border_radius=8)
    
    fuente = pygame.font.Font(None, 28)
    texto_surface = fuente.render(texto, True, (255, 255, 255))
    texto_rect = texto_surface.get_rect(center=rect.center)
    surface.blit(texto_surface, texto_rect)
    
    return rect

# --- Inicialización ---
pygame.init() 

# --- Selección del Camino ---
CAMINO_ELEGIDO = random.choice(caminos_posibles)

# --- Configuración de la Ventana ---
N_VENTANA = len(CAMINO_ELEGIDO) 
TAMANIO_VENTANA = N_VENTANA * TAMANIO_CELDA
ALTURA_EXTRA = 100

pantalla = pygame.display.set_mode((TAMANIO_VENTANA, TAMANIO_VENTANA+ALTURA_EXTRA)) 
pygame.display.set_caption("Simulador de Máquina de Turing")
reloj = pygame.time.Clock()

# --- Encontrar el punto de inicio---
fila_inicio = 0
col_inicio = -1 
for indice_col, val_celda in enumerate(CAMINO_ELEGIDO[fila_inicio]):
    if val_celda == CAMINO:
        col_inicio = indice_col
        break


# --- Carga de Sprites---

imagenes_personaje_cargadas = {}
rutas_imagenes_personaje = {
    # Animación Abajo
    1: "./img/1.png",
    2: "./img/2.png",
    3: "./img/3.png",
    4: "./img/4.png",
    # Animación Izquierda
    9: "./img/9.png",
    10: "./img/10.png",
    11: "./img/11.png",
    12: "./img/12.png",
    # Animación Derecha
    13: "./img/13.png",
    14: "./img/14.png",
    15: "./img/15.png", 16: "./img/16.png"
}
print("\nCargando sprites del personaje...")
for dir_key, ruta in rutas_imagenes_personaje.items():
    try:
        img_original = pygame.image.load(ruta).convert_alpha()
        imagenes_personaje_cargadas[dir_key] = pygame.transform.scale(img_original, (TAMANIO_CELDA, TAMANIO_CELDA))
        print(f" - '{ruta}' (Personaje) cargado.")
    except Exception as e:
        print(f" - ¡ERROR cargando '{ruta}': {e}")
        imagenes_personaje_cargadas[dir_key] = None

imagenes_tiles_cargadas = {}
rutas_imagenes_tiles = {
    PARED: "./img/pared2.png",     # Paredes
    CAMINO: "./img/pasillo3.png",    # Pasillo
    VISITADO: "./img/pasillo3.png",   # Pasillo visitado
    SALIDA: "./img/tilesFin.png"    # Salida
}
print("\nCargando sprites del nivel...")
for char_key, ruta in rutas_imagenes_tiles.items():
    try:
        img_original = pygame.image.load(ruta).convert_alpha()
        imagenes_tiles_cargadas[char_key] = pygame.transform.scale(img_original, (TAMANIO_CELDA, TAMANIO_CELDA))
        print(f" - '{ruta}' (Nivel) cargado.")
    except Exception as e:
        print(f" - ¡ERROR cargando '{ruta}': {e}")
        imagenes_tiles_cargadas[char_key] = None
print("Carga de sprites finalizada.\n")


# --- Inicializar primera simulación ---
cadena_entrada, cadena_salida = reiniciar_simulacion()
simulacion_completada = False

# --- Bucle Principal ---
ejecutando = True
simulacion_completada = False

# Definir área del botón
boton_reiniciar = pygame.Rect(
    TAMANIO_VENTANA // 2 - 80,
    TAMANIO_VENTANA + 80,
    160, 35
)

while ejecutando:
    mouse_pos = pygame.mouse.get_pos()
    N_VENTANA = len(CAMINO_ELEGIDO)

    # Manejo de Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                boton_ancho = 190
                boton_alto = 35
                boton_x = (TAMANIO_VENTANA_ACTUAL - boton_ancho) // 2
                boton_y = TAMANIO_VENTANA_ACTUAL + (100 - boton_alto) // 2
                boton_reiniciar = pygame.Rect(boton_x, boton_y, boton_ancho, boton_alto)
                if boton_reiniciar.collidepoint(mouse_pos):
                    reiniciar_simulacion()
                    simulacion_completada = False

    # --- Renderizado ---
    pantalla.fill((255, 255, 255)) 

    area_juego = pygame.Rect(MARGEN_X, MARGEN_Y, N_VENTANA * TAMANIO_CELDA, N_VENTANA * TAMANIO_CELDA)
    pygame.draw.rect(pantalla, (255, 255, 255), area_juego)
    
    camino.dibujar(pantalla, pygame, offset_x=MARGEN_X, offset_y=MARGEN_Y)

    if not maquina_turing.detenida:
        sprite_actual = controlador_animacion.obtener_sprite_actual(maquina_turing.direccion)
        if sprite_actual:
            posicion_x = maquina_turing.col * TAMANIO_CELDA + MARGEN_X
            posicion_y = maquina_turing.fila * TAMANIO_CELDA + MARGEN_Y
            pantalla.blit(sprite_actual, (posicion_x, posicion_y))

    # --- ÁREA DE INFORMACIÓN (debajo del juego) ---
    area_info = pygame.Rect(0, TAMANIO_VENTANA_ACTUAL, TAMANIO_VENTANA_ACTUAL, 100)
    pygame.draw.rect(pantalla, (60, 60, 60), area_info)
    
    
    # dibujar_texto(pantalla, f"Entrada: {cadena_entrada}", (10, TAMANIO_VENTANA_ACTUAL + 10), (220, 220, 220), 22)
    # dibujar_texto(pantalla, f"Salida:  {cadena_salida}", (10, TAMANIO_VENTANA_ACTUAL + 35), (220, 220, 220), 22)
    
    # # Mostrar estado de la simulación
    # estado = "Completado" if maquina_turing.detenida else "En progreso..."
    # color_estado = (100, 255, 100) if maquina_turing.detenida else (255, 255, 100)
    # dibujar_texto(pantalla, f"Estado: {estado}", (10, TAMANIO_VENTANA + 60), color_estado, 24)
    
    # Dibujar botón de reinicio
    boton_ancho = 190
    boton_alto = 35
    boton_x = (TAMANIO_VENTANA_ACTUAL - boton_ancho) // 2
    boton_y = TAMANIO_VENTANA_ACTUAL + (100 - boton_alto) // 2
    boton_rect = dibujar_boton(
        pantalla, 
        pygame.Rect(boton_x, boton_y, boton_ancho, boton_alto),
        "Nueva Simulación", 
        (70, 130, 200),
        (100, 160, 230), # hover
        mouse_pos
    )

    # Lógica
    if not maquina_turing.detenida:
        maquina_turing.paso()
        controlador_animacion.actualizar_animacion()
    
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()