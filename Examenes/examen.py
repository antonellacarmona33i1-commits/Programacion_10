class Contenido:
    def __init__(self, titulo, calificacion):
        self.titulo = titulo
        self.calificacion = calificacion
    @property
    def calificacion(self):
        return self._calificacion
    @calificacion.setter
    def calificacion(self, valor):
        if valor < 0:
            self._calificacion = 0
        else:
            self._calificacion = valor

    def __str__(self):
        return f"<{self.titulo}> (Calificacion: <{self.calificacion}>)"
    
    def __lt__(self, otro):
        return self.calificacion < otro.calificacion
    
class Pelicula(Contenido):
    def __init__(self, titulo, calificacion, duracion_minutos):
        super().__init__(titulo, calificacion)
        self.duracion_minutos = duracion_minutos
    def __str__(self):
        return f"Pelicula: <{self.titulo}>, Duracion: <{self.duracion_minutos}> min,Calificacion: <{self.calificacion}>"
    
class Serie(Contenido):
    def __init__(self, titulo, calificacion,temporadas):
        super().__init__(titulo, calificacion)
        self.temporadas = temporadas
    
    def __str__(self):
        return f"Serie: <{self.titulo}>, Temporadas: <{self.temporadas}>, Calificacion: <{self.calificacion}>"
    @classmethod
    def desde_cadena(cls, texto):
        partes = texto.split(",")
        titulo = partes[0].strip()
        temporadas = int(partes[1].strip())
        calificacion = float(partes[2].strip())
        return cls(titulo, calificacion, temporadas)

class Playlist:
    def __init__(self):
        self.contenidos = []
    
    def agregar_contenido(self, contenido):
        self.contenidos.append(contenido)
    
    def vaciar_playlist(self):
        self.contenidos.clear()
    
    def mostrar_playlist(self):
        for contenido in self.contenidos:
            print(contenido)
            
    def ordenar_por_calificacion(self):
        contenidos_ordenados = sorted(self.contenidos, reverse=True)
        return contenidos_ordenados
    
    def calcular_promedio_calificacion(self):
        if not self.contenidos:
            return 0
        else:
            calificaciones = []
            for contenido in self.contenidos:
                calificaciones.append(contenido.calificacion)
            return sum(calificaciones) / len(calificaciones) 
        
def main ():
        playlist = Playlist()
        contenido = Contenido("Contenido generico", 1.3)
        pelicula1 = Pelicula("Shrek 1", 9.0, 94)
        serie1 = Serie("The Disastrous Life of Saiki K", 9.9, 3)
        serie2 = Serie.desde_cadena("Nose, 2, 8.5")
        
        playlist.agregar_contenido(contenido)
        playlist.agregar_contenido(pelicula1)
        playlist.agregar_contenido(serie1)
        playlist.agregar_contenido(serie2)
        
        print("Playlist")
        playlist.mostrar_playlist()
        
        
        print("Sin calificaciones negativas")
        pelicula1.calificacion = -100000000
        print(f"{pelicula1.calificacion}")
        
        
        print("Contenidos ordenados por calificacion")
        playlist_ordenado = playlist.ordenar_por_calificacion() 
        print(f"{playlist_ordenado}")

        
        promedio_calificacion = playlist.calcular_promedio_calificacion()
        print(f"Promedio de calificacion: {promedio_calificacion}")
        
        print("Playlist vaciada")
        playlist.vaciar_playlist()
        playlist.mostrar_playlist()

main()