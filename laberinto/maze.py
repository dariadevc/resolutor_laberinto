import random
import pygame # Necesitamos pygame para el método de dibujado

# Un '1' es un camino, '0' es una pared, 'E' es la salida
class Maze:
    def __init__(self, n):
        self.n = n
        
        # --- INICIO: Generación Aleatoria (DFS Backtracker) ---
        
        # Asegurarse de que n es impar. Es crucial para este algoritmo.
        if self.n % 2 == 0:
            self.n += 1
        
        # 1. Empezar con una cuadrícula de todas las paredes ('0')
        self.grid = [['0' for _ in range(self.n)] for _ in range(self.n)]
        
        stack = []
        
        # 2. Elegir un inicio DENTRO del marco (en 1,1) y hacerlo camino ('1')
        start_r, start_c = 1, 1 
        self.grid[start_r][start_c] = '1'
        stack.append((start_r, start_c))
        
        # (Ya no necesitamos guardar 'end_of_path')

        # Deltas para moverse 2 celdas (a los vecinos de las "celdas")
        dr = [-2, 2, 0, 0]
        dc = [0, 0, -2, 2]

        while stack:
            r, c = stack[-1]
            
            # 3. Encontrar vecinos no visitados (que sean '0')
            neighbors = []
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                # Asegurarse de que los vecinos estén DENTRO del marco
                if 1 <= nr < self.n - 1 and 1 <= nc < self.n - 1 and self.grid[nr][nc] == '0':
                    neighbors.append(i) # Guardar el índice de la dirección
            
            if neighbors:
                # 4. Elegir un vecino al azar
                choice_index = random.choice(neighbors)
                nr, nc = r + dr[choice_index], c + dc[choice_index]
                
                # 5. "Romper" la pared entre la celda actual y el vecino
                wall_r = r + dr[choice_index] // 2
                wall_c = c + dc[choice_index] // 2
                
                self.grid[nr][nc] = '1'
                self.grid[wall_r][wall_c] = '1'
                
                # 6. Moverse al vecino
                stack.append((nr, nc))
            
            else:
                # 7. No hay vecinos, retroceder (backtrack)
                # ¡AQUÍ ESTÁ EL CAMBIO!
                # En lugar de 'break', usamos 'stack.pop()'.
                # Esto permite al algoritmo crear bifurcaciones
                # y explorar TODA la cuadrícula.
                stack.pop()
        
        # --- FIN: Generación Aleatoria ---

        # --- Crear la abertura de INICIO y FIN ---
        
        # 8. Poner la SALIDA 'E' SIEMPRE en la esquina inferior derecha
        self.grid[self.n - 2][self.n - 2] = 'E'
        
        # 9. Poner el INICIO '1' en la esquina (0,0) (la abertura)
        self.grid[0][0] = '1'
        # Conectar la abertura al laberinto
        self.grid[1][0] = '1' 

        # El 'main.py' leerá esto para ajustar el tamaño de la ventana
        self.cell_size = 20 # Reducimos el tamaño para laberintos más grandes

    def get_cell(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.n:
            return self.grid[row][col]
        return '0' # Trata fuera de los límites como una pared

    def set_cell(self, row, col, value):
        # Para marcar el camino como visitado
        if 0 <= row < self.n and 0 <= col < self.n:
            self.grid[row][col] = value

    def draw(self, screen, pygame_instance):
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
                pygame_instance.draw.rect(screen, color, rect)