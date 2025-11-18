class MaquinaTuring:
    # __init__ recibe un diccionario de imágenes
    def __init__(self, camino, fila_inicio, col_inicio): 
        self.camino = camino            
        self.fila = fila_inicio        
        self.col = col_inicio     
        self.detenida = False         
        
        self.direccion = 2 # Abajo
        
        self.dr = [-1, 0, 1, 0]
        self.dc = [0, 1, 0, -1]

    def paso(self):

        if self.detenida:
            return

        celda_actual = self.camino.get_celda(self.fila, self.col)
        if celda_actual == 'E':
            self.detenida = True
            print("¡Éxito! Salida encontrada.")
            return

        if celda_actual == '0':
            self.camino.set_celda(self.fila, self.col, 'V') 
        
        self.direccion = (self.direccion + 1) % 4
        
        for i in range(4):
            sig_fila = self.fila + self.dr[self.direccion]
            sig_col = self.col + self.dc[self.direccion]
            
            sig_celda = self.camino.get_celda(sig_fila, sig_col)
            
            if sig_celda != '1':
                self.fila = sig_fila
                self.col = sig_col
                return
            else:
                self.direccion = (self.direccion - 1) % 4

    def get_cadena_salida(self):

        matriz_camino = [fila.copy() for fila in self.camino.grid]

        matriz_salida = [fila.copy() for fila in matriz_camino]

        for fila in range(len(matriz_camino)):
            for col in range(len(matriz_camino[0])):
                if matriz_camino[fila][col] == 'E':
                    matriz_camino[fila][col] = '0'

        fila_actual = 0
        columna_actual = -1
        for i, celda in enumerate(matriz_camino[0]):
            if celda == '0':
                columna_actual = i
                matriz_salida[0][columna_actual] = 'A'
                break
        
        direccion_actual = 2  # Empezamos mirando hacia abajo
        dr = [-1, 0, 1, 0]    # Arriba, Derecha, Abajo, Izquierda
        dc = [0, 1, 0, -1]
        
        mapa_direcciones = {
            0: 'U',  # Arriba (no se usa!)
            1: 'D',  # Derecha
            2: 'A',  # Abajo  
            3: 'I'   # Izquierda
        }
        
        pasos = 0
        max_pasos = len(matriz_camino) * len(matriz_camino[0]) * 2
        primer_paso = True
        
        while pasos < max_pasos:
            if fila_actual == len(matriz_camino) - 1:
                if matriz_camino[fila_actual][columna_actual] == '0':
                    matriz_salida[fila_actual][columna_actual] = mapa_direcciones.get(direccion_actual, 'A')
                break

            direccion_actual = (direccion_actual + 1) % 4
            
            movimiento_encontrado = False
            for i in range(4):
                siguiente_fila = fila_actual + dr[direccion_actual]
                siguiente_columna = columna_actual + dc[direccion_actual]
                
                if (0 <= siguiente_fila < len(matriz_camino) and 
                    0 <= siguiente_columna < len(matriz_camino[0]) and
                    matriz_camino[siguiente_fila][siguiente_columna] != '1'):
                    
                    if not (fila_actual == 0 and columna_actual == columna_actual):
                        if matriz_camino[fila_actual][columna_actual] == '0':
                            matriz_salida[fila_actual][columna_actual] = mapa_direcciones[direccion_actual]
                    
                    fila_actual, columna_actual = siguiente_fila, siguiente_columna
                    movimiento_encontrado = True
                    break
                else:
                    direccion_actual = (direccion_actual - 1) % 4
            
            if not movimiento_encontrado:
                break
                
            pasos += 1
        
        # Convertir la matriz a cadena
        return self._matriz_a_cadena(matriz_salida)

    def _matriz_a_cadena(self, matriz):
        """Convierte la matriz a cadena con # separando filas"""
        filas_str = []
        for fila in matriz:
            fila_str = ''.join(fila)
            filas_str.append(fila_str)
        return '#'.join(filas_str)