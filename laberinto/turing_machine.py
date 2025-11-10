# Este archivo es turing_machine.py

class TuringMachine:
    def __init__(self, maze, start_row, start_col):
        self.maze = maze            # Referencia al objeto laberinto
        self.row = start_row        # Posición actual (fila)
        self.col = start_col        # Posición actual (columna)
        self.halted = False         # Bandera para detener la máquina
        
        # Dirección: 0=Arriba, 1=Derecha, 2=Abajo, 3=Izquierda
        self.direction = 2 # Empezamos mirando hacia Abajo (para el laberinto de ejemplo)
        
        # Deltas para el movimiento [Arriba, Derecha, Abajo, Izquierda]
        # dr (delta row), dc (delta col)
        self.dr = [-1, 0, 1, 0]
        self.dc = [0, 1, 0, -1]

    def step(self):
        """
        Ejecuta un paso de la lógica de la Máquina de Turing.
        Implementa el algoritmo de "Seguir la pared de la derecha".
        """
        if self.halted:
            return

        # 1. Comprobar si hemos llegado a la salida
        current_cell = self.maze.get_cell(self.row, self.col)
        if current_cell == 'E':
            self.halted = True
            print("¡Éxito! Salida encontrada.")
            return

        # 2. Marcar la celda actual como visitada (si no es la salida)
        if current_cell == '1':
            self.maze.set_cell(self.row, self.col, 'V') # 'V' de Visitado
        
        # --- Lógica del Seguidor de Pared (Mano Derecha) ---
        
        # 3. Primero, gira a la derecha para "tantear" la pared
        self.direction = (self.direction + 1) % 4
        
        # 4. Bucle para encontrar la próxima dirección válida
        # Intentará 4 veces (derecha, recto, izquierda, atrás)
        for i in range(4):
            # Calcular la celda que está en frente de la dirección actual
            next_r = self.row + self.dr[self.direction]
            next_c = self.col + self.dc[self.direction]
            
            # Comprobar qué hay en esa celda
            next_cell = self.maze.get_cell(next_r, next_c)
            
            # Si la celda NO es una pared ('0')...
            if next_cell != '0':
                # ¡Camino encontrado! Moverse a esa celda
                self.row = next_r
                self.col = next_c
                # Romper el bucle 'for', ya que hemos completado nuestro movimiento
                return
            else:
                # Si hay una pared, gira a la izquierda e inténtalo de nuevo
                self.direction = (self.direction - 1) % 4
                
        # Si el bucle 'for' termina sin un 'return', significa que
        # estamos en un callejón sin salida 1x1 (muy raro).
        # En este caso, la lógica nos hará girar 180 grados y volver.


    def draw_bug(self, screen, pygame_instance, cell_size):
        """ Dibuja el "bichito" (la cabeza de la TM) en la pantalla """
        if self.halted:
            return

        # Calcular el centro de la celda actual
        center_x = self.col * cell_size + cell_size // 2
        center_y = self.row * cell_size + cell_size // 2
        
        # Dibujar un círculo rojo para representar el "bichito"
        radius = cell_size // 3
        pygame_instance.draw.circle(screen, (255, 0, 0), (center_x, center_y), radius)