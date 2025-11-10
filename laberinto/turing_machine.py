# En turing_machine.py

import pygame

class TuringMachine:
    # ¡MODIFICADO! Ahora el __init__ recibe un diccionario de imágenes
    def __init__(self, maze, start_row, start_col, bug_images): 
        self.maze = maze            
        self.row = start_row        
        self.col = start_col        
        self.halted = False         
        
        self.direction = 2 # Empezamos mirando hacia Abajo
        
        self.dr = [-1, 0, 1, 0]
        self.dc = [0, 1, 0, -1]

        # --- ¡MUY MODIFICADO! ---
        # Ya no cargamos imágenes aquí. 
        # Simplemente asignamos las que recibimos de main.py
        self.bug_images = bug_images 

    def step(self):
        # ... (Tu lógica del método step sigue igual) ...
        # (No es necesario pegarla de nuevo, la tuya funciona)
        if self.halted:
            return

        current_cell = self.maze.get_cell(self.row, self.col)
        if current_cell == 'E':
            self.halted = True
            print("¡Éxito! Salida encontrada.")
            return

        if current_cell == '1':
            self.maze.set_cell(self.row, self.col, 'V') 
        
        self.direction = (self.direction + 1) % 4
        
        for i in range(4):
            next_r = self.row + self.dr[self.direction]
            next_c = self.col + self.dc[self.direction]
            
            next_cell = self.maze.get_cell(next_r, next_c)
            
            if next_cell != '0':
                self.row = next_r
                self.col = next_c
                return
            else:
                self.direction = (self.direction - 1) % 4


    # --- ¡MODIFICADO! Para manejar tus 3 imágenes ---
    def draw_bug(self, screen, pygame_instance, cell_size):
        """ 
        Dibuja el "bichito" en la pantalla.
        Si no hay sprite para "Arriba", usa el de "Abajo".
        """
        if self.halted:
            return

        # 1. Intentar obtener la imagen de la dirección actual
        current_bug_image = self.bug_images.get(self.direction)
        
        # 2. ¡NUEVO! Si no existe (ej. dirección 0)
        if current_bug_image is None:
            # Usar la imagen de "Abajo" (key 2) como default
            current_bug_image = self.bug_images.get(2) 

        # 3. Si existe (la original o la default), dibujarla
        if current_bug_image: 
            draw_x = self.col * cell_size
            draw_y = self.row * cell_size
            screen.blit(current_bug_image, (draw_x, draw_y))
        else:
            # 4. Si NINGUNA existe (ni '1.png'), dibujar el cuadrado rojo
            draw_x = self.col * cell_size
            draw_y = self.row * cell_size
            fallback_rect = (draw_x, draw_y, cell_size, cell_size)
            pygame_instance.draw.rect(screen, (255, 0, 0), fallback_rect)