class ErrorPrestamo(Exception):
    def __init__(self, mensaje, codigo):
        super().__init__(mensaje)
        self.codigo = codigo

    def mensaje_detallado(self):
        return f"{self} Código: {self.codigo}."
