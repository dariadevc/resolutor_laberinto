class Camino:
    
    def __init__(self, static_grid, tamanio_celda, tile_images):
        
        self.grid = [fila[:] for fila in static_grid]
        self.n = len(self.grid) 
        self.tamanio_celda = tamanio_celda
        self.tile_images = tile_images

    def get_celda(self, fila, col):
        if 0 <= fila < self.n and 0 <= col < self.n:
            return self.grid[fila][col]
        return '1' 

    def set_celda(self, fila, col, value):
        if 0 <= fila < self.n and 0 <= col < self.n:
            self.grid[fila][col] = value

    # La idea es que se reconozca qué tile poner según ls vecinos que tiene!!
    # def get_tile_type(self, fila, col):
    #     """Determina el tipo de tile basado en los vecinos"""
    #     if self.grid[fila][col] != '1':  # No es pared
    #         return self.grid[fila][col]
        
    #     # Sistema de bits para determinar el tipo de pared
    #     bitmask = 0
        
    #     # Verificar los 8 vecinos (solo nos interesan las paredes '1')
    #     # Arriba-izquierda (1)
    #     if fila > 0 and col > 0 and self.grid[fila-1][col-1] == '1':
    #         bitmask |= 1
    #     # Arriba (2)
    #     if fila > 0 and self.grid[fila-1][col] == '1':
    #         bitmask |= 2
    #     # Arriba-derecha (4)
    #     if fila > 0 and col < self.n-1 and self.grid[fila-1][col+1] == '1':
    #         bitmask |= 4
    #     # Izquierda (8)
    #     if col > 0 and self.grid[fila][col-1] == '1':
    #         bitmask |= 8
    #     # Derecha (16)
    #     if col < self.n-1 and self.grid[fila][col+1] == '1':
    #         bitmask |= 16
    #     # Abajo-izquierda (32)
    #     if fila < self.n-1 and col > 0 and self.grid[fila+1][col-1] == '1':
    #         bitmask |= 32
    #     # Abajo (64)
    #     if fila < self.n-1 and self.grid[fila+1][col] == '1':
    #         bitmask |= 64
    #     # Abajo-derecha (128)
    #     if fila < self.n-1 and col < self.n-1 and self.grid[fila+1][col+1] == '1':
    #         bitmask |= 128
            
    #     return self.bitmask_to_tile_type(bitmask)
    
    # def bitmask_to_tile_type(self, bitmask):
    #     """Convierte la máscara de bits a un tipo de tile específico"""
    #     # Definir los tipos básicos según la conectividad
    #     top = (bitmask & 2) != 0
    #     bottom = (bitmask & 64) != 0
    #     left = (bitmask & 8) != 0
    #     right = (bitmask & 16) != 0
        
    #     # Paredes simples
    #     if top and bottom and left and right:
    #         return 'wall_center'  # Pared completamente rodeada
        
    #     # Esquinas
    #     if top and right and not left and not bottom:
    #         return 'wall_corner_top_left'
    #     if top and left and not right and not bottom:
    #         return 'wall_corner_top_right'
    #     if bottom and right and not left and not top:
    #         return 'wall_corner_bottom_left'
    #     if bottom and left and not right and not top:
    #         return 'wall_corner_bottom_right'
            
    #     # # Paredes verticales
    #     # if top and bottom and not left and not right:
    #     #     return 'wall_vertical'
            
    #     # Paredes horizontales
    #     if left and right and not top and not bottom:
    #         return 'wall_horizontal'
            
    #     # # T-connections
    #     # if top and left and right and not bottom:
    #     #     return 'wall_t_down'
    #     # if bottom and left and right and not top:
    #     #     return 'wall_t_up'
    #     # if left and top and bottom and not right:
    #     #     return 'wall_t_right'
    #     # if right and top and bottom and not left:
    #     #     return 'wall_t_left'
            
    #     # Paredes con extremos
    #     if top and not bottom and not left and not right:
    #         return 'wall_end_bottom'
    #     if bottom and not top and not left and not right:
    #         return 'wall_end_top'
    #     if left and not right and not top and not bottom:
    #         return 'wall_end_right'
    #     if right and not left and not top and not bottom:
    #         return 'wall_end_left'
            
    #     return 'wall_single'  # Pared aislada


    # def dibujar(self, pantalla, pygame_instance, offset_x=0, offset_y=0):
    #     for fila in range(self.n):
    #         for col in range(self.n):
    #             # Obtener el tipo de tile basado en los vecinos
    #             tile_type = self.get_tile_type(fila, col)
    #             imagen_a_dibujar = self.tile_images.get(tile_type)
                
    #             pos_x = col * self.tamanio_celda + offset_x
    #             pos_y = fila * self.tamanio_celda + offset_y
                
    #             if imagen_a_dibujar:
    #                 pantalla.blit(imagen_a_dibujar, (pos_x, pos_y))


    def dibujar(self, pantalla, pygame_instance, offset_x=0, offset_y=0):
        for fila in range(self.n):
            for col in range(self.n):
                char_key = self.grid[fila][col]
                imagen_a_dibujar = self.tile_images.get(char_key)
                
                pos_x = col * self.tamanio_celda + offset_x
                pos_y = fila * self.tamanio_celda + offset_y
                
                if imagen_a_dibujar:
                    pantalla.blit(imagen_a_dibujar, (pos_x, pos_y))

    def get_cadena_camino(self):
        filas_transformadas = []
        for fila in self.grid:
            # Convertir fila a string y reemplazar 'E' por '0'
            fila_str = ''.join(fila).replace('E', '0')
            filas_transformadas.append(fila_str)
        
        # Unir todas las filas con '#' entre ellas
        return '#'.join(filas_transformadas)