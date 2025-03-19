class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Libro '{self.titulo}' prestado con éxito."
        else:
            return f"El libro '{self.titulo}' ya está prestado."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"Libro '{self.titulo}' devuelto con éxito."
        else:
            return f"El libro '{self.titulo}' ya estaba disponible."
    
    def mostrar_info(self):
        estado = "Sí" if self.disponible else "No"
        return f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, titulo, autor, isbn):
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
        return "Libro agregado con éxito."
    
    def prestar(self, isbn):
        libro = self.buscar_libro(isbn)
        return libro.prestar() if libro else "No se encontró un libro con ese ISBN."
    
    def devolver(self, isbn):
        libro = self.buscar_libro(isbn)
        return libro.devolver() if libro else "No se encontró un libro con ese ISBN."
    
    def mostrar(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        return "\n".join([libro.mostrar_info() for libro in self.libros])
    
    def buscar(self, isbn):
        libro = self.buscar_libro(isbn)
        return libro.mostrar_info() if libro else "No se encontró un libro con ese ISBN."
    
    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

def ejecutar_comandos(comandos):
    biblioteca = Biblioteca()
    resultados = []
    
    for comando in comandos:
        if comando[0] == "agregar":
            resultados.append(biblioteca.agregar(*comando[1:]))
        elif comando[0] == "prestar":
            resultados.append(biblioteca.prestar(comando[1]))
        elif comando[0] == "devolver":
            resultados.append(biblioteca.devolver(comando[1]))
        elif comando[0] == "mostrar":
            resultados.append(biblioteca.mostrar())
        elif comando[0] == "buscar":
            resultados.append(biblioteca.buscar(comando[1]))
        elif comando[0] == "salir":
            resultados.append("Saliendo del sistema...")
            break
    
    return "\n".join(resultados)

# Ejemplo de uso con comandos predefinidos
ejemplo_comandos = [
    ("agregar", "El Quijote", "Miguel de Cervantes", "12345"),
    ("mostrar",),
    ("prestar", "12345"),
    ("mostrar",),
    ("devolver", "12345"),
    ("mostrar",),
    ("salir",)
]

resultado = ejecutar_comandos(ejemplo_comandos)
print(resultado)
