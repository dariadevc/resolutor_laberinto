class ControladorAnimacion:
    def __init__(self, imagenes_personaje):
        self.imagenes_personaje = imagenes_personaje
        self.marcos_animacion = {
            1: [13, 14, 15, 16],  # Derecha
            2: [1, 2, 3, 4],      # Abajo  
            3: [9, 10, 11, 12]    # Izquierda
        }
        self.indice_marco_actual = 0
        self.velocidad_animacion = 3
        self.contador_pasos = 0
    
    def actualizar_animacion(self):
        """Actualiza el marco de animación"""
        self.contador_pasos += 1
        if self.contador_pasos >= self.velocidad_animacion:
            self.indice_marco_actual = (self.indice_marco_actual + 1) % 4
            self.contador_pasos = 0
    
    def obtener_sprite_actual(self, direccion):
        """Obtiene el sprite actual para una dirección dada"""
        if direccion in self.marcos_animacion:
            numero_marco = self.marcos_animacion[direccion][self.indice_marco_actual]
            return self.imagenes_personaje.get(numero_marco)
        return self.imagenes_personaje.get(1) 