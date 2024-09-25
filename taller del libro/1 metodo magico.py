class libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"El título del libro es: {self.titulo}, y su autor es: {self.autor}"
    def __repr__(self):
        return f"Libro(Titulo: {self.titulo}, autor: {self.autor}, paginas: {self.paginas}"
libro1= libro("habitos atomicos","james clear",300)
libro2= libro("romeo y julieta","William Shakespeare",224)
print(libro1)
print(libro2)