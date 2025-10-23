import random
from PIL import Image
from mazelib import Maze
from mazelib.generate.HuntAndKill import HuntAndKill


class Laberinto:
    def __init__(self, ancho=16, alto=16, semilla=9000):
        self.columnas = ancho
        self.filas = alto
        #cuando querramos usar laberintos random, tenemos que sacar la semilla!!
        self.lab = Maze(semilla)
        self.inicializar_laberinto()

    def get_laberinto(self):
        """Me permite obtener el laberinto como un objeto Maze!!! no como una matriz (importante)"""
        return self.lab

    def inicializar_laberinto(self):
        """
        Genera un laberinto a partir del algoritmo HuntAndKill, el cual...
        Además le agrega una entrada y una salida en algunos de los bordes del laberinto.
        """
        # Voy a estar usando el algoritmo HuntAndKill de la libería con orden random.
        self.lab.generator = HuntAndKill(self.columnas, self.filas, "random")
        self.lab.generate()
        self.agregar_entrada_salida()

    def agregar_entrada_salida(self):
        """
        Para agregar una entrada y una salida al laberinto ya generado
        """
        posibles = self.bordes_disponibles(self.lab.grid)
        self.lab.start, self.lab.end = random.sample(posibles, 2)
        self.lab.grid[self.lab.start[0]][self.lab.start[1]] = 0
        self.lab.grid[self.lab.end[0]][self.lab.end[1]] = 0

    def bordes_disponibles(self, matriz):
        """
        Genera un arreglo de las celdas en los bordes que se encuentran al lado de una celda
        libre, es decir, del camino.
        """
        disponibles = []

        # Borde superior
        for y in range(1, self.columnas-1):
            if matriz[1][y] == 0:
                disponibles.append((0, y))

        # Borde inferior
        for y in range(1, self.columnas-1):
            if matriz[self.filas-2][y] == 0:
                disponibles.append((self.filas-1, y))

        # Borde izquierdo
        for x in range(1, self.filas-1):
            if matriz[x][1] == 0:
                disponibles.append((x, 0))

        # Borde derecho
        for x in range(1, self.filas-1):
            if matriz[x][self.columnas-2] == 0:
                disponibles.append((x, self.columnas-1))

        return disponibles

    def generar_imagen(self):
        
        TAMANIO_CELDA = 20
        
        # Crear imagen
        h, w = len(self.lab.grid), len(self.lab.grid[0])
        img = Image.new("RGB", (w*TAMANIO_CELDA, h*TAMANIO_CELDA), "white")
        
        # Colores
        wall_color = (0,0,0)       # negro
        path_color = (255,255,255) # blanco
        start_color = (0,255,0)    # verde
        end_color = (255,0,0)      # rojo

        for i in range(h):
            for j in range(w):
                color = wall_color if laberinto_objeto.grid[i][j]==1 else path_color
                for y in range(TAMANIO_CELDA):
                    for x in range(TAMANIO_CELDA):
                        img.putpixel((j*TAMANIO_CELDA + x, i*TAMANIO_CELDA + y), color)
        
        # Colorear entrada y salida
        si, sj = laberinto_objeto.start
        ei, ej = laberinto_objeto.end
        for y in range(TAMANIO_CELDA):
            for x in range(TAMANIO_CELDA):
                img.putpixel((sj*TAMANIO_CELDA + x, si*TAMANIO_CELDA + y), start_color)
                img.putpixel((ej*TAMANIO_CELDA + x, ei*TAMANIO_CELDA + y), end_color)

        # Mostrar
        img.show()




laberinto = Laberinto()
laberinto_objeto = laberinto.get_laberinto()
print(laberinto_objeto)

laberinto.generar_imagen()
