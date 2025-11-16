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

    # verifica si la celda es una pared
    def es_pared(self, fila, col):
        if 0 <= fila < self.n and 0 <= col < self.n:
            return self.grid[fila][col] == '1'
        return False

    # verifica si la celda es un camino
    def es_camino(self, fila, col):
        if 0 <= fila < self.n and 0 <= col < self.n:
            return self.grid[fila][col] in ['0', 'V', 'E']
        return False

    def obtener_tipo_tile(self, fila, col):

        # si no es una pared, usa la tile camino.png
        if not self.es_pared(fila, col):
            return self.get_celda(fila, col)

        # Verificar los 8 vecinos, B2 representa la celda actual

        # A1 | A2 | A3
        # B1 | B2 | B3
        # C1| C2 | C3

        # Y una celda extra por debajo de C2 para las paredes

        # D2

        # primer fila
        a1 = self.es_pared(fila - 1, col - 1) if 0 <= fila-1 < self.n and 0 <= col-1 < self.n else True
        a2 = self.es_pared(fila - 1, col) if 0 <= fila-1 < self.n and 0 <= col < self.n else True
        a3 = self.es_pared(fila - 1, col + 1) if 0 <= fila-1 < self.n and 0 <= col+1 < self.n else True

        #segunda fila
        b1 = self.es_pared(fila, col - 1) if 0 <= fila < self.n and 0 <= col-1 < self.n else True
        b2 = self.es_pared(fila, col) if 0 <= fila < self.n and 0 <= col < self.n else True
        b3 = self.es_pared(fila, col + 1) if 0 <= fila < self.n and 0 <= col+1 < self.n else True

        #tercer fila
        c1 = self.es_pared(fila + 1, col - 1) if 0 <= fila+1 < self.n and 0 <= col-1 < self.n else True
        c2 = self.es_pared(fila + 1, col) if 0 <= fila+1 < self.n and 0 <= col < self.n else True
        c3 = self.es_pared(fila + 1, col + 1) if 0 <= fila+1 < self.n and 0 <= col+1 < self.n else True

        #cuarta fila
        d2 = self.es_pared(fila + 2, col) if 0 <= fila+2 < self.n and 0 <= col < self.n else True

        # ==== Determinar el tipo de tile basado en los vecinos ====

        # --- CELDAS CENTRALES ---

        # Costado izquierdo
        if a2 and a3 and b3 and c2 and c3 and ((not b1 and d2)or (b1 and not c1 and d2)):
            return 'CIZ'

        # Centro
        if a1 and a2 and a3 and b1 and b3 and c1 and c2 and c3 and d2:
            return 'CEN'
        
        # Costado derecho
        if a1 and a2 and b1 and c1 and c2 and ((not b3 and d2) or (b3 and not c3 and d2)):
            return 'CDE'
        
        # --- CELDAS SUPERIORES ---

        # Esquina superior izquierda
        if not a1 and not a2 and not b1 and b3 and c2 and c3 and d2:
            return 'ESI'
    
        # Centro superior
        if not a2 and b1 and b3 and c1 and c2 and c3 and d2:
            return 'CSU'
        
        # Esquina superior derecha
        if not a2 and not a3 and not b3 and b1 and c1 and c2 and d2:
            return 'ESD'
        
        # -- CELDAS INFERIORES ---

        # Esquina inferior izquierda
        if a2 and a3 and b3 and c2 and c3 and ((a1 and b1) or (not a1 and not b1) or (a1 and not b1)) and not c1 and not d2:
            return 'EII'
        
        # Centro inferior
        if a2 and b1 and b3 and c2 and c3 and not d2:
            return 'CIN'
        
        # Esquina inferior derecha
        if a1 and a2 and b1 and c1 and c2 and ((a3 and b3) or (not a3 and not b3) or (a3 and not b3)) and not c3 and not d2:
            return 'EID'

        # -- CELDAS SUP E INF ---

        # Esquina superior e inferior izquierda
        if not a1 and not a2 and not b1 and not c1 and not d2 and b3 and c2 and c3:
            return 'ESII'

        # Centro superior e inferior
        if not a2 and b1 and b3 and c1 and c2 and c3 and not d2:
            return 'CSI'
        
        # Esquina superior e inferior derecha
        if not a2 and not a3 and not b3 and not c3 and not d2 and b1 and c1 and c2:
            return 'ESDI'
        
        # -- PAREDES ---

        # Pared izquierda
        if a2 and a3 and b3 and not b1 and not c1 and not c2:
            return 'PI'
        
        # Pared central
        if a1 and a2 and a3 and b1 and b3 and not c2:
            return 'PC'
        
        # Pared derecha
        if a1 and a2 and b1 and not b3 and not c2 and not c3:
            return 'PD'
        
        return 'CEN'  # Valor por defecto si no coincide con ningún patrón


    def dibujar(self, pantalla, pygame_instance, offset_x=0, offset_y=0):
        for fila in range(self.n):
            for col in range(self.n):
                tipo_tile = self.obtener_tipo_tile(fila, col)
                imagen_a_dibujar = self.tile_images.get(tipo_tile)

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