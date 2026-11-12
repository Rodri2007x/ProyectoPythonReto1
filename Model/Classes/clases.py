class Libro:
    def __init__ (self, codigo, titulo, autor, año, categoría, codsocio):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.categoría = categoría
        self.codsocio = codsocio # puede ser none (pone en el ej)

    def esta_disponible(self):
        return self.codsocio is None


class Socio:
    def __init__ (self, codsocio, nombre, email, codiprestado):
        self.codsocio = codsocio
        self.nombre = nombre
        self.email = email
        self.codiprestado = codiprestado

    def tiene_libro_prestado(self):
        return self.codiprestado is not None
