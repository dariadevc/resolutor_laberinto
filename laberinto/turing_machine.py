class TuringMachine:
    def __init__(self, maze, start_row, start_col):
        self.maze = maze
        self.n = maze.n
        
        # Posición actual del "bichito" (cabeza de la TM)
        self.row = start_row
        self.col = start_col
        
        # Estado = Orientación: 0=Norte, 1=Este, 2=Sur, 3=Oeste
        self.state = 1 # Empezamos mirando al Este
        
        self.halted = False

    def get_tape_index(self, r, c):
        return r * self.n + c

    def get_coords(self, index):
        return index // self.n, index % self.n

    def step(self):
        if self.halted:
            return

        # 1. Marcar la celda actual como visitada
        current_symbol = self.maze.get_cell(self.row, self.col)
        if current_symbol == 'E':
            print("¡Salida encontrada!")
            self.halted = True
            return
        
        if current_symbol != 'V':
             self.maze.set_cell(self.row, self.col, 'V') # 'V' para visitado

        # 2. Implementar la lógica de estados (Regla de la Mano Derecha)
        # (dx, dy) para [Norte, Este, Sur, Oeste]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Girar a la derecha
        right_state = (self.state + 1) % 4
        dr_right, dc_right = directions[right_state]
        cell_to_right = self.maze.get_cell(self.row + dr_right, self.col + dc_right)

        if cell_to_right != '0': # Si no hay pared a la derecha...
            # Giramos (cambiando de estado) y avanzamos
            self.state = right_state
            self.row += dr_right
            self.col += dc_right
        else: # Hay pared a la derecha, intentamos seguir recto
            dr_fwd, dc_fwd = directions[self.state]
            cell_fwd = self.maze.get_cell(self.row + dr_fwd, self.col + dc_fwd)

            if cell_fwd != '0': # Si no hay pared en frente...
                # Avanzamos (mismo estado)
                self.row += dr_fwd
                self.col += dc_fwd
            else: # Hay pared en frente...
                # Giramos a la izquierda (cambiando de estado)
                self.state = (self.state - 1) % 4
                # No avanzamos en este paso

    def draw_bug(self, screen, pygame, cell_size):
        # Dibuja el "bichito" como un círculo rojo
        center_x = self.col * cell_size + cell_size // 2
        center_y = self.row * cell_size + cell_size // 2
        pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), cell_size // 3)