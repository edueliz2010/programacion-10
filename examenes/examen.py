class Contenido:
    def __init__(self, titulo, calificacion):
        self.titulo = titulo
        self.calificacion = calificacion

    @property
    def calificacion(self):
        return self.__calificacion

    @calificacion.setter
    def calificacion(self, valor):
        if valor < 0:
            self.__calificacion = 0
        else:
            self.__calificacion = valor

    def __str__(self):
        return f"{self.titulo} (calificacion: {self.calificacion})"

    def __lt__(self, otro):
        return self.calificacion < otro.calificacion


class Pelicula(Contenido):
    def __init__(self, titulo, calificacion, duracion_minutos):
        super().__init__(titulo, calificacion)
        self.duracion_minutos = duracion_minutos

    def __str__(self):
        return (
            f"pelicula: {self.titulo}, "
            f"{self.duracion_minutos} min, "
            f"calificacion: {self.calificacion}"
        )


class Serie(Contenido):
    def __init__(self, titulo, calificacion, temporadas):
        super().__init__(titulo, calificacion)
        self.temporadas = temporadas

    def __str__(self):
        return (
            f"serie: {self.titulo}, "
            f"{self.temporadas}, "
            f"calificacion: {self.calificacion}"
        )

    @classmethod
    def desde_cadena(cls, texto):
        titulo, temporadas, calificacion = texto.split(",")

        return cls(
            titulo,
            float(calificacion),
            int(temporadas)
        )


class Playlist:
    def __init__(self):
        self.contenido = []

    def agregar_contenido(self, contenido):
        self.contenido.append(contenido)

    def vaciar_playlist(self):
        self.contenido.clear()

    def mostrar_playlist(self):
        for obj in self.contenido:
            print(obj)

    def ordenar_por_clacificacion(self):
        return sorted(self.contenido, reverse=True)

    def calcular_calificacion_promedio(self):
        if len(self.contenido) == 0:
            return 0

        suma = 0

        for obj in self.contenido:
            suma += obj.calificacion

        return suma / len(self.contenido)


def main():
    contenido1 = Contenido("Contenido generico", 7.5)

    pelicula1 = Pelicula(
        "Interestelar",
        9.0,
        169
    )

    serie1 = Serie(
        "Breaking Bad",
        9.5,
        5
    )

    serie2 = Serie.desde_cadena(
        "Stranger Things,4,8.7"
    )

    playlist = Playlist()

    playlist.agregar_contenido(contenido1)
    playlist.agregar_contenido(pelicula1)
    playlist.agregar_contenido(serie1)
    playlist.agregar_contenido(serie2)

    print("=== PLAYLIST ORIGINAL ===")
    playlist.mostrar_playlist()

    print("\n=== CAMBIANDO CALIFICACION ===")

    contenido1.calificacion = -5

    print(contenido1)

    print("\n=== PLAYLIST ORDENADA POR CALIFICACION ===")

    playlist_ordenada = playlist.ordenar_por_clacificacion()

    for obj in playlist_ordenada:
        print(obj)

    print("\n=== PLAYLIST ORIGINAL SIN MODIFICAR ===")
    playlist.mostrar_playlist()

    promedio = playlist.calcular_calificacion_promedio()

    print(f"\n=== CALIFICACION PROMEDIO ===")
    print(f"Promedio: {promedio:.2f}")

    playlist.vaciar_playlist()

    print("\n=== PLAYLIST DESPUES DE VACIAR ===")
    playlist.mostrar_playlist()

    print(f"Cantidad de contenidos: {len(playlist.contenido)}")


if __name__ == "__main__":
    main()