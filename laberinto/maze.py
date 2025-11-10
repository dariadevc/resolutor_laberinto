# Un '1' es un camino, '0' es una pared, 'E' es la salida
class Maze:
    def __init__(self, n):
        self.n = n
        # Crea un laberinto de n x n (aquí puedes generarlo aleatoriamente)
        # Por ahora, usamos uno simple:
        self.grid = [
            ['1', '0', '1', '1', '1'],
            ['1', '0', '0', '0', '0'],
            ['1', '1', '1', '1', '0'],
            ['0', '0', '0', '1', '0'],
            ['1', '1', '0', '1', 'E']
        ]
        self.cell_size = 40 # Tamaño en píxeles de cada celda

    def get_cell(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.n:
            return self.grid[row][col]
        return '0' # Trata fuera de los límites como una pared

    def set_cell(self, row, col, value):
        # Para marcar el camino como visitado
        if 0 <= row < self.n and 0 <= col < self.n:
            self.grid[row][col] = value

    def draw(self, screen, pygame):
        # Dibuja la cuadrícula
        colors = {
            '0': (0, 0, 0),       # Pared (Negro)
            '1': (255, 255, 255), # Camino (Blanco)
            'E': (0, 255, 0),     # Salida (Verde)
            'V': (0, 0, 255)      # Visitado (Azul)
        }
        for r in range(self.n):
            for c in range(self.n):
                color = colors.get(self.grid[r][c], (255, 0, 0)) # Rojo si hay error
                rect = (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, color, rect)