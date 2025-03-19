class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def agregar(self):
        print(f"Libro agregado con éxito: {self.titulo} ({self.autor}) - ISBN: {self.isbn}")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro prestado con éxito: {self.titulo} ({self.autor}) - ISBN: {self.isbn}")
        else:
            print(f"El libro {self.titulo} ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro devuelto con éxito: {self.titulo} ({self.autor}) - ISBN: {self.isbn}")
        else:
            print(f"El libro {self.titulo} ya está disponible.")

    def mostrar(self):
        disponibilidad = "Sí" if self.disponible else "No"
        print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {disponibilidad}")

    def buscar(self, isbn):
        if self.isbn == isbn:
            self.mostrar()
            return True
        return False

def menu():
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")

def main():
    inventario = []

    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, isbn)
            libro.agregar()
            inventario.append(libro)

        elif opcion == "2":
            isbn = input("Ingresa el ISBN: ")
            encontrado = False
            for libro in inventario:
                if libro.buscar(isbn):
                    encontrado = True
                    libro.prestar()
                    break
            if not encontrado:
                print("Libro no encontrado.")

        elif opcion == "3":
            isbn = input("Ingresa el ISBN: ")
            encontrado = False
            for libro in inventario:
                if libro.buscar(isbn):
                    encontrado = True
                    libro.devolver()
                    break
            if not encontrado:
                print("Libro no encontrado.")

        elif opcion == "4":
            if not inventario:
                print("No hay libros en el inventario.")
            else:
                for libro in inventario:
                    libro.mostrar()

        elif opcion == "5":
            isbn = input("Ingresa el ISBN: ")
            encontrado = False
            for libro in inventario:
                if libro.buscar(isbn):
                    encontrado = True
                    break
            if not encontrado:
                print("Libro no encontrado.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()