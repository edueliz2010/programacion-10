class libro:

    def __init__ (self, titulo, autor, pag_tot):
        self.autor = autor
        self.titulo = titulo
        self.pag_tot = pag_tot
        self.pag_act = 0
    
    def leer(self, cant):
        self.pag_act += cant
        if self.pag_act > self.pag_tot:
            self.pag_act = self.pag_tot
        print(f"{self.titulo}: página {self.pag_act} de {self.pag_tot}")
    
    def progreso(self):
        porcentaje = (self.pag_act / self.pag_tot) * 100
        print(f"progreso de ' {self.titulo}': {porcentaje:.1f}%")

libro = libro("titulo", "autor", "paginas")
libro.leer("x")
libro.progreso()
