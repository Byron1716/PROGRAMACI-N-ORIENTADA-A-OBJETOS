#EJEMPLO 1 de POO
class Vehiculo:
    #Definimos el metodo constructor con sus atributos
    def __init__(self, color, marca, modelo, anio):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0

#Haremos una descripción del vehículo
    def describir_vehiculo(self):
        descripcion = f"El vehículo {self.marca} {self.modelo} {self.anio} color {self.color} está yendo a {self.velocidad}km/h."
        return descripcion

#Ponemos el metodo conducir
    def conduicir(self, km):
        if km > 0:
            self.velocidad += km
        else:
            print("El kilometraje debe ser positivo")

#Implementamos el metodo aumentar velocidad
    def aumentar_velocidad(self, aumento_velocidad):
        self.velocidad += aumento_velocidad
        aumento = f"El vehículo {self.marca} {self.modelo} {self.anio} de color {self.color} aumentó su veloicidad y ahora está yendo a {self.velocidad}km/h"
        return aumento

# Implementamos el metodo reducir velocidad
    def reducir_velocidad(self, reduciccion_velocidad):
        self.velocidad -= reduciccion_velocidad
        disminucion = f"El vehículo {self.marca} {self.modelo} {self.anio} de color {self.color} disminuyó su veloicidad y ahora está yendo a {self.velocidad}km/h"
        return disminucion

    def pintar_vehiculo(self, nuevo_color):
        self.color = nuevo_color

#Crear una nueva instancia de la clase vehículo
mi_vehiculo = Vehiculo("Azul", "KIA", "C3", 2022)

#Describir Vehículo
print(mi_vehiculo.describir_vehiculo())

#Conducir el vehículo a 80km/h
mi_vehiculo.conduicir(80)
print(mi_vehiculo.describir_vehiculo())

#Aumentar la velocidad a 100km/h
mi_vehiculo.aumentar_velocidad(20)
print(mi_vehiculo.aumentar_velocidad(0))

#Reducir la velocidad a 70 km/h
mi_vehiculo.reducir_velocidad(30)
print(mi_vehiculo.reducir_velocidad(0))

#Pintar el vehículo de rojo
mi_vehiculo.pintar_vehiculo("rojo")
print(mi_vehiculo.describir_vehiculo())







#EJEMPLO 2 de POO

# Clase para representar un Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} ISBN: {self.isbn} - {estado}"


# Clase para representar un Miembro de la Biblioteca
class Miembro:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha prestado '{libro.titulo}'")
        else:
            print(f"'{libro.titulo}' no está disponible para préstamo.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto '{libro.titulo}'")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' prestado.")


# Clase para representar la Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")


    def registrar_miembro(self, miembro):
        self.miembros.append(miembro)
        print(f"Miembro '{miembro.nombre}' registrado en la biblioteca.")


    def mostrar_libros_disponibles(self):
        print("Libros disponibles en la biblioteca:")
        for libro in self.libros:
            if libro.disponible:
                print(libro)


# Función principal para demostrar el uso de las clases
def main():
    # Crear la biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # Crear y agregar libros a la biblioteca
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "1234567890")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "0987654321")
    libro3 = Libro("El viaje mas largo", "Nicholas Sparks", "03125661233")
    libro4 = Libro("El cuaderno de Noah", "Nicholas Sparks", "0451735234")
    libro5 = Libro("Solo Amigos", "Ana Álvarez", "9786075294032")
    libro6 = Libro("La Divina Comedia", "Dhante Alighieri", "639219859")
    libro7 = Libro("El principito", "Antoine De Saint-Exupéry", "745831011")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.agregar_libro(libro4)
    biblioteca.agregar_libro(libro5)
    biblioteca.agregar_libro(libro6)
    biblioteca.agregar_libro(libro7)

    # Registrar miembros
    miembro1 = Miembro("Juan Pérez", "001")
    miembro2 = Miembro("Ana Gómez", "002")
    miembro3 = Miembro("Byron Rosado", "003")
    miembro4 = Miembro("Ana Fernández", "004")
    miembro5 = Miembro("Ben Carson", "005")
    biblioteca.registrar_miembro(miembro1)
    biblioteca.registrar_miembro(miembro2)
    biblioteca.registrar_miembro(miembro3)
    biblioteca.registrar_miembro(miembro4)
    biblioteca.registrar_miembro(miembro5)

    # Mostrar libros disponibles
    biblioteca.mostrar_libros_disponibles()

    # Prestar y devolver libros
    miembro1.prestar_libro(libro1)
    miembro1.devolver_libro(libro1)
    miembro2.prestar_libro(libro4)
    miembro2.prestar_libro(libro7)
    miembro1.prestar_libro(libro3)
    miembro3.prestar_libro(libro3)
    miembro5.prestar_libro(libro7)
    miembro2.devolver_libro(libro4)
    miembro3.devolver_libro(libro3)


    # Mostrar libros disponibles después de los préstamos
    biblioteca.mostrar_libros_disponibles()

if __name__ == "__main__":
    main()
