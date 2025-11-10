class Maze:
    
    def __init__(self, static_grid, cell_size, tile_images):
        
        # 1. Copiamos la cuadrícula estática
        self.grid = [row[:] for row in static_grid]
        
        # 2. Obtenemos el tamaño 'n' desde la cuadrícula
        self.n = len(self.grid) 
        
        # 3. Guardamos el cell_size y las imágenes
        self.cell_size = cell_size
        self.tile_images = tile_images # Este es el diccionario de imágenes

    def get_cell(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.n:
            return self.grid[row][col]
        return '0' 

    def set_cell(self, row, col, value):
        if 0 <= row < self.n and 0 <= col < self.n:
            self.grid[row][col] = value


    def draw(self, screen, pygame_instance):
        """
        Dibuja el laberinto usando sprites (imágenes) en lugar de colores.
        """
        
        for r in range(self.n):
            for c in range(self.n):
                # 1. Obtener el carácter de la celda (ej: '0', '1', 'E')
                char_key = self.grid[r][c]
                
                # 2. Buscar la imagen correspondiente en el diccionario
                image_to_draw = self.tile_images.get(char_key)
                
                # 3. Calcular dónde dibujarla
                draw_x = c * self.cell_size
                draw_y = r * self.cell_size
                
                if image_to_draw:
                    # 4. ¡Dibujar la imagen!
                    screen.blit(image_to_draw, (draw_x, draw_y))
                else:
                    # 5. Fallback: Si no encontramos imagen para un carácter
                    # (ej. olvidamos 'V'), dibuja un cuadrado rosa brillante
                    # para que sepamos que hay un error.
                    fallback_rect = (draw_x, draw_y, self.cell_size, self.cell_size)
                    pygame_instance.draw.rect(screen, (255, 255, 255), fallback_rect) # Rosa