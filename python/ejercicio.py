class Libro:
    """
    Clase que representa un libro dentro de la biblioteca.
    Contiene información sobre el título, autor, ISBN y si está disponible.
    """
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        """
        Método para prestar un libro. Cambia el estado a 'No disponible'.
        """
        if self.disponible:
            self.disponible = False
            return f"Libro '{self.titulo}' prestado con éxito."
        else:
            return f"El libro '{self.titulo}' ya está prestado."

    def devolver(self):
        """
        Método para devolver un libro prestado. Cambia el estado a 'Disponible'.
        """
        if not self.disponible:
            self.disponible = True
            return f"Libro '{self.titulo}' devuelto con éxito."
        else:
            return f"El libro '{self.titulo}' ya estaba disponible."
    
    def mostrar_info(self):
        """
        Método para mostrar la información del libro.
        Indica si el libro está disponible o no.
        """
        estado = "Sí" if self.disponible else "No"
        return f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"

class Biblioteca:
    """
    Clase que representa la biblioteca.
    Gestiona una lista de libros y las operaciones sobre ellos.
    """
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

def ejecutar_sin_interaccion():
    """
    Función para ejecutar pruebas sin necesidad de input(), evitando errores de I/O.
    """
    biblioteca = Biblioteca()
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    
    acciones = [
        biblioteca.agregar("El Quijote", "Cervantes", "12345"),
        biblioteca.mostrar(),
        biblioteca.prestar("12345"),
        biblioteca.mostrar(),
        biblioteca.devolver("12345"),
        biblioteca.mostrar()
    ]
    
    print("\n1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro")
    print("6. Salir")
    
    for resultado in acciones:
        print(resultado)
    
    print("Saliendo del sistema...")

# Ejecutar pruebas sin interacción
ejecutar_sin_interaccion()
