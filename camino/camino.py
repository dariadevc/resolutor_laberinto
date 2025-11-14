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