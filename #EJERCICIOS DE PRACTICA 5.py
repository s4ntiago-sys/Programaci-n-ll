#EJERCICIOS DE PRACTICA 2

#  1.
# class Contacto:
#     def __init__(self, nombre, apellido, telefono, correo, direccion, cumpleaños):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.telefono = telefono
#         self.correo = correo
#         self.direccion = direccion
#         self.cumpleaños = cumpleaños

#     def __str__(self):
#         return f"{self.nombre} {self.apellido} - Tel: {self.telefono} - Email: {self.correo} - Dir: {self.direccion} - Cumpleaños: {self.cumpleaños}"

# class Agenda:
#     def __init__(self):
#         self.contactos = {}

#     def agregar_contacto(self, contacto):
#         self.contactos[contacto.telefono] = contacto
#         print(f"Contacto {contacto.nombre} {contacto.apellido} agregado con éxito.")

#     def buscar_contacto(self, telefono):
#         if telefono in self.contactos:
#             return self.contactos[telefono]
#         else:
#             return "Contacto no encontrado."

#     def eliminar_contacto(self, telefono):
#         if telefono in self.contactos:
#             del self.contactos[telefono]
#             print(f"Contacto con teléfono {telefono} eliminado.")
#         else:
#             print("Contacto no encontrado.")

#     def actualizar_contacto(self, telefono, nuevo_contacto):
#         if telefono in self.contactos:
#             self.contactos[telefono] = nuevo_contacto
#             print(f"Contacto con teléfono {telefono} actualizado.")
#         else:
#             print("Contacto no encontrado.")

#     def mostrar_agenda(self):
#         if not self.contactos:
#             print("No hay contactos en la agenda.")
#         else:
#             for contacto in self.contactos.values():
#                 print(contacto)

# def menu():
#     agenda = Agenda()
    
#     while True:
#         print("\nOpciones:")
#         print("1. Agregar contacto")
#         print("2. Buscar contacto")
#         print("3. Eliminar contacto")
#         print("4. Actualizar contacto")
#         print("5. Mostrar agenda")
#         print("6. Salir")
        
#         opcion = input("Selecciona una opción: ")

#         if opcion == '1':
#             nombre = input("Nombre: ")
#             apellido = input("Apellido: ")
#             telefono = input("Teléfono: ")
#             correo = input("Correo: ")
#             direccion = input("Dirección: ")
#             cumpleaños = input("Cumpleaños: ")
#             nuevo_contacto = Contacto(nombre, apellido, telefono, correo, direccion, cumpleaños)
#             agenda.agregar_contacto(nuevo_contacto)
#         elif opcion == '2':
#             telefono = input("Ingresa el teléfono del contacto a buscar: ")
#             contacto = agenda.buscar_contacto(telefono)
#             print(contacto)
#         elif opcion == '3':
#             telefono = input("Ingresa el teléfono del contacto a eliminar: ")
#             agenda.eliminar_contacto(telefono)
#         elif opcion == '4':
#             telefono = input("Ingresa el teléfono del contacto a actualizar: ")
#             nombre = input("Nuevo nombre: ")
#             apellido = input("Nuevo apellido: ")
#             correo = input("Nuevo correo: ")
#             direccion = input("Nueva dirección: ")
#             cumpleaños = input("Nuevo cumpleaños: ")
#             nuevo_contacto = Contacto(nombre, apellido, telefono, correo, direccion, cumpleaños)
#             agenda.actualizar_contacto(telefono, nuevo_contacto)
#         elif opcion == '5':
#             agenda.mostrar_agenda()
#         elif opcion == '6':
#             print("Gracias por usar la agenda.")
#             break
#         else:
#             print("Opción no válida. Intenta de nuevo.")

# menu()

# 2.
# class ConversorEnteroARomano:
#     def __init__(self, numero):
#         self.numero = numero
#         self.romano = ""
    
#     def convertir(self):
#         valors_romanos = [
#             (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
#             (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
#         ]
        
#         num = self.numero
#         for valor, simbolo in valors_romanos:
#             while num >= valor:
#                 self.romano += simbolo
#                 num -= valor
#         return self.romano


# class ConversorRomanoAEntero:
#     def __init__(self, romano):
#         self.romano = romano
#         self.numero = 0
#         self.romanos = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
#             'D': 500, 'M': 1000
#         }
    
#     def convertir(self):
#         romano = self.romano.upper()
#         for i in range(len(romano)):
#             if i + 1 < len(romano) and self.romanos[romano[i]] < self.romanos[romano[i + 1]]:
#                 self.numero -= self.romanos[romano[i]]
#             else:
#                 self.numero += self.romanos[romano[i]]
#         return self.numero


# def menu():
#     while True:
#         print("\nOpciones:")
#         print("1. Convertir número entero a romano")
#         print("2. Convertir número romano a entero")
#         print("3. Salir")
        
#         opcion = input("Selecciona una opción: ")
        
#         if opcion == '1':
#             numero = int(input("Ingresa un número entero: "))
#             conversor = ConversorEnteroARomano(numero)
#             print(f"El número {numero} en romano es: {conversor.convertir()}")
#         elif opcion == '2':
#             romano = input("Ingresa un número romano: ")
#             conversor = ConversorRomanoAEntero(romano)
#             print(f"El número romano {romano} es: {conversor.convertir()}")
#         elif opcion == '3':
#             print("Gracias por usar el conversor.")
#             break
#         else:
#             print("Opción no válida. Intenta de nuevo.")

# menu()


# 3.
# class Animal:
#     def __init__(self, nombre, edad, habitat):
#         self.nombre = nombre
#         self.edad = edad
#         self.habitat = habitat

#     def mostrar_informacion(self):
#         return f"Nombre: {self.nombre}\nEdad: {self.edad}\nHábitat: {self.habitat}"

# class Terrestre(Animal):
#     def __init__(self, nombre, edad, habitat, velocidad, dieta):
#         super().__init__(nombre, edad, habitat)
#         self.velocidad = velocidad
#         self.dieta = dieta

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\nVelocidad: {self.velocidad} km/h\nDieta: {self.dieta}"

# class Aereo(Animal):
#     def __init__(self, nombre, edad, habitat, envergadura, tipo_de_plumas):
#         super().__init__(nombre, edad, habitat)
#         self.envergadura = envergadura
#         self.tipo_de_plumas = tipo_de_plumas

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\nEnvergadura: {self.envergadura} metros\nTipo de Plumas: {self.tipo_de_plumas}"

# class Acuatico(Animal):
#     def __init__(self, nombre, edad, habitat, tipo_de_agua, velocidad_de_nado):
#         super().__init__(nombre, edad, habitat)
#         self.tipo_de_agua = tipo_de_agua
#         self.velocidad_de_nado = velocidad_de_nado

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\nTipo de agua: {self.tipo_de_agua}\nVelocidad de nado: {self.velocidad_de_nado} km/h"

# def ingresar_datos():
#     print("Selecciona la especie del animal:")
#     print("1. Terrestre")
#     print("2. Aéreo")
#     print("3. Acuático")
    
#     opcion = input("Opción: ")
    
#     if opcion == '1':
#         nombre = input("Nombre del animal: ")
#         edad = int(input("Edad del animal: "))
#         habitat = input("Hábitat del animal: ")
#         velocidad = int(input("Velocidad máxima (km/h): "))
#         dieta = input("Dieta del animal: ")
#         animal = Terrestre(nombre, edad, habitat, velocidad, dieta)
#     elif opcion == '2':
#         nombre = input("Nombre del animal: ")
#         edad = int(input("Edad del animal: "))
#         habitat = input("Hábitat del animal: ")
#         envergadura = float(input("Envergadura de las alas (metros): "))
#         tipo_de_plumas = input("Tipo de plumas: ")
#         animal = Aereo(nombre, edad, habitat, envergadura, tipo_de_plumas)
#     elif opcion == '3':
#         nombre = input("Nombre del animal: ")
#         edad = int(input("Edad del animal: "))
#         habitat = input("Hábitat del animal: ")
#         tipo_de_agua = input("Tipo de agua (dulce/salado): ")
#         velocidad_de_nado = int(input("Velocidad de nado (km/h): "))
#         animal = Acuatico(nombre, edad, habitat, tipo_de_agua, velocidad_de_nado)
#     else:
#         print("Opción no válida.")
#         return None
    
#     print("\nInformación del animal registrado:")
#     print(animal.mostrar_informacion())
#     return animal

# def menu():
#     animales = []
#     while True:
#         print("\n1. Ingresar un nuevo animal")
#         print("2. Salir")
#         opcion = input("Selecciona una opción: ")
        
#         if opcion == '1':
#             animal = ingresar_datos()
#             if animal:
#                 animales.append(animal)
#         elif opcion == '2':
#             print("\nAnimales registrados:")
#             for animal in animales:
#                 print("\n" + animal.mostrar_informacion())
#             break
#         else:
#             print("Opción no válida. Intenta de nuevo.")

# menu()


# 4. 
# import math
# from abc import ABC, abstractmethod

# class FiguraGeometrica(ABC):
#     def __init__(self):
#         self.area = 0
#         self.perimetro = 0

#     @abstractmethod
#     def calcular_area(self):
#         pass

#     @abstractmethod
#     def calcular_perimetro(self):
#         pass

# class Triangulo(FiguraGeometrica):
#     def __init__(self, base, altura, lado1, lado2, lado3):
#         super().__init__()
#         self.base = base
#         self.altura = altura
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3

#     def calcular_area(self):
#         self.area = (self.base * self.altura) / 2
#         return self.area

#     def calcular_perimetro(self):
#         self.perimetro = self.lado1 + self.lado2 + self.lado3
#         return self.perimetro

# class Circunferencia(FiguraGeometrica):
#     def __init__(self, radio):
#         super().__init__()
#         self.radio = radio

#     def calcular_area(self):
#         self.area = math.pi * (self.radio ** 2)
#         return self.area

#     def calcular_perimetro(self):
#         self.perimetro = 2 * math.pi * self.radio
#         return self.perimetro

# class Cuadrado(FiguraGeometrica):
#     def __init__(self, lado):
#         super().__init__()
#         self.lado = lado

#     def calcular_area(self):
#         self.area = self.lado ** 2
#         return self.area

#     def calcular_perimetro(self):
#         self.perimetro = 4 * self.lado
#         return self.perimetro

# class Rectangulo(FiguraGeometrica):
#     def __init__(self, largo, ancho):
#         super().__init__()
#         self.largo = largo
#         self.ancho = ancho

#     def calcular_area(self):
#         self.area = self.largo * self.ancho
#         return self.area

#     def calcular_perimetro(self):
#         self.perimetro = 2 * (self.largo + self.ancho)
#         return self.perimetro

# class Paralelogramo(FiguraGeometrica):
#     def __init__(self, base, altura):
#         super().__init__()
#         self.base = base
#         self.altura = altura

#     def calcular_area(self):
#         self.area = self.base * self.altura
#         return self.area

#     def calcular_perimetro(self):
#         self.perimetro = 2 * (self.base + self.altura)
#         return self.perimetro

# class Trapecio(FiguraGeometrica):
#     def __init__(self, base1, base2, altura, lado1, lado2):
#         super().__init__()
#         self.base1 = base1
#         self.base2 = base2
#         self.altura = altura
#         self.lado1 = lado1
#         self.lado2 = lado2

#     def calcular_area(self):
#         self.area = ((self.base1 + self.base2) * self.altura) / 2
#         return self.area

#     def calcular_perimetro(self):
#         self.perimetro = self.lado1 + self.lado2 + self.base1 + self.base2
#         return self.perimetro

# class Rombo(FiguraGeometrica):
#     def __init__(self, diagonal1, diagonal2, lado):
#         super().__init__()
#         self.diagonal1 = diagonal1
#         self.diagonal2 = diagonal2
#         self.lado = lado

#     def calcular_area(self):
#         self.area = (self.diagonal1 * self.diagonal2) / 2
#         return self.area

#     def calcular_perimetro(self):
#         self.perimetro = 4 * self.lado
#         return self.perimetro

# def main():
#     figuras = []
#     while True:
#         print("\nSeleccione la figura:")
#         print("1. Triángulo")
#         print("2. Circunferencia")
#         print("3. Cuadrado")
#         print("4. Rectángulo")
#         print("5. Paralelogramo")
#         print("6. Trapecio")
#         print("7. Rombo")
#         print("8. Salir")
        
#         opcion = int(input("Ingrese una opción: "))
        
#         if opcion == 8:
#             break

#         if opcion == 1:
#             base = float(input("Ingrese la base del triángulo: "))
#             altura = float(input("Ingrese la altura del triángulo: "))
#             lado1 = float(input("Ingrese el primer lado del triángulo: "))
#             lado2 = float(input("Ingrese el segundo lado del triángulo: "))
#             lado3 = float(input("Ingrese el tercer lado del triángulo: "))
#             figura = Triangulo(base, altura, lado1, lado2, lado3)
        
#         elif opcion == 2:
#             radio = float(input("Ingrese el radio de la circunferencia: "))
#             figura = Circunferencia(radio)
        
#         elif opcion == 3:
#             lado = float(input("Ingrese el lado del cuadrado: "))
#             figura = Cuadrado(lado)
        
#         elif opcion == 4:
#             largo = float(input("Ingrese el largo del rectángulo: "))
#             ancho = float(input("Ingrese el ancho del rectángulo: "))
#             figura = Rectangulo(largo, ancho)
        
#         elif opcion == 5:
#             base = float(input("Ingrese la base del paralelogramo: "))
#             altura = float(input("Ingrese la altura del paralelogramo: "))
#             figura = Paralelogramo(base, altura)
        
#         elif opcion == 6:
#             base1 = float(input("Ingrese la primera base del trapecio: "))
#             base2 = float(input("Ingrese la segunda base del trapecio: "))
#             altura = float(input("Ingrese la altura del trapecio: "))
#             lado1 = float(input("Ingrese el primer lado del trapecio: "))
#             lado2 = float(input("Ingrese el segundo lado del trapecio: "))
#             figura = Trapecio(base1, base2, altura, lado1, lado2)
        
#         elif opcion == 7:
#             diagonal1 = float(input("Ingrese la primera diagonal del rombo: "))
#             diagonal2 = float(input("Ingrese la segunda diagonal del rombo: "))
#             lado = float(input("Ingrese el lado del rombo: "))
#             figura = Rombo(diagonal1, diagonal2, lado)
        
#         figura.calcular_area()
#         figura.calcular_perimetro()
        
#         print(f"Área: {figura.area}")
#         print(f"Perímetro: {figura.perimetro}")

# if __name__ == "__main__":
#     main()


# 5.
# class Vehiculo:
#     def __init__(self, modelo, tipo_pintura, unidades_inventario):
#         self.modelo = modelo
#         self.tipo_pintura = tipo_pintura
#         self.unidades_inventario = unidades_inventario

#     def mostrar_informacion(self):
#         return f"Modelo: {self.modelo}\nTipo de pintura: {self.tipo_pintura}\nUnidades en inventario: {self.unidades_inventario}"

#     def actualizar_inventario(self, cantidad):
#         self.unidades_inventario += cantidad

# class Automovil(Vehiculo):
#     def __init__(self, modelo, tipo_pintura, unidades_inventario, tipo_motor, cantidad_puertas):
#         super().__init__(modelo, tipo_pintura, unidades_inventario)
#         self.tipo_motor = tipo_motor
#         self.cantidad_puertas = cantidad_puertas

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\nTipo de motor: {self.tipo_motor}\nCantidad de puertas: {self.cantidad_puertas}"

# class Camioneta(Vehiculo):
#     def __init__(self, modelo, tipo_pintura, unidades_inventario, capacidad_carga, traccion):
#         super().__init__(modelo, tipo_pintura, unidades_inventario)
#         self.capacidad_carga = capacidad_carga
#         self.traccion = traccion

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\nCapacidad de carga: {self.capacidad_carga} kg\nTipo de tracción: {self.traccion}"

# class Camion(Vehiculo):
#     def __init__(self, modelo, tipo_pintura, unidades_inventario, capacidad_carga, numero_ejes):
#         super().__init__(modelo, tipo_pintura, unidades_inventario)
#         self.capacidad_carga = capacidad_carga
#         self.numero_ejes = numero_ejes

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\nCapacidad de carga: {self.capacidad_carga} kg\nNúmero de ejes: {self.numero_ejes}"

# class Tractocamion(Vehiculo):
#     def __init__(self, modelo, tipo_pintura, unidades_inventario, capacidad_carga, numero_ejes, tipo_motor):
#         super().__init__(modelo, tipo_pintura, unidades_inventario)
#         self.capacidad_carga = capacidad_carga
#         self.numero_ejes = numero_ejes
#         self.tipo_motor = tipo_motor

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\nCapacidad de carga: {self.capacidad_carga} kg\nNúmero de ejes: {self.numero_ejes}\nTipo de motor: {self.tipo_motor}"

# def mostrar_menu():
#     print("\nMenu del concesionario:")
#     print("1. Agregar un automóvil")
#     print("2. Agregar una camioneta")
#     print("3. Agregar un camión")
#     print("4. Agregar un tractocamión")
#     print("5. Mostrar todos los vehículos")
#     print("6. Salir")

# def agregar_vehiculo(tipo_vehiculo):
#     modelo = input("Ingrese el modelo del vehículo: ")
#     tipo_pintura = input("Ingrese el tipo de pintura del vehículo: ")
#     unidades_inventario = int(input("Ingrese la cantidad de unidades en inventario: "))

#     if tipo_vehiculo == 'automovil':
#         tipo_motor = input("Ingrese el tipo de motor del automóvil: ")
#         cantidad_puertas = int(input("Ingrese la cantidad de puertas del automóvil: "))
#         return Automovil(modelo, tipo_pintura, unidades_inventario, tipo_motor, cantidad_puertas)
#     elif tipo_vehiculo == 'camioneta':
#         capacidad_carga = int(input("Ingrese la capacidad de carga de la camioneta (kg): "))
#         traccion = input("Ingrese el tipo de tracción de la camioneta: ")
#         return Camioneta(modelo, tipo_pintura, unidades_inventario, capacidad_carga, traccion)
#     elif tipo_vehiculo == 'camion':
#         capacidad_carga = int(input("Ingrese la capacidad de carga del camión (kg): "))
#         numero_ejes = int(input("Ingrese el número de ejes del camión: "))
#         return Camion(modelo, tipo_pintura, unidades_inventario, capacidad_carga, numero_ejes)
#     elif tipo_vehiculo == 'tractocamion':
#         capacidad_carga = int(input("Ingrese la capacidad de carga del tractocamión (kg): "))
#         numero_ejes = int(input("Ingrese el número de ejes del tractocamión: "))
#         tipo_motor = input("Ingrese el tipo de motor del tractocamión: ")
#         return Tractocamion(modelo, tipo_pintura, unidades_inventario, capacidad_carga, numero_ejes, tipo_motor)
#     else:
#         print("Opción no válida.")
#         return None

# def mostrar_vehiculos(vehiculos):
#     if len(vehiculos) == 0:
#         print("No hay vehículos registrados.")
#     else:
#         for vehiculo in vehiculos:
#             print("\n" + vehiculo.mostrar_informacion())

# def main():
#     vehiculos = []
#     while True:
#         mostrar_menu()
#         opcion = input("Seleccione una opción: ")

#         if opcion == '1':
#             vehiculo = agregar_vehiculo('automovil')
#             if vehiculo:
#                 vehiculos.append(vehiculo)
#         elif opcion == '2':
#             vehiculo = agregar_vehiculo('camioneta')
#             if vehiculo:
#                 vehiculos.append(vehiculo)
#         elif opcion == '3':
#             vehiculo = agregar_vehiculo('camion')
#             if vehiculo:
#                 vehiculos.append(vehiculo)
#         elif opcion == '4':
#             vehiculo = agregar_vehiculo('tractocamion')
#             if vehiculo:
#                 vehiculos.append(vehiculo)
#         elif opcion == '5':
#             mostrar_vehiculos(vehiculos)
#         elif opcion == '6':
#             print("Saliendo del programa...")
#             break
#         else:
#             print("Opción no válida, intente de nuevo.")

# if __name__ == "__main__":
#     main()

# 6. 
class Persona:
    def __init__(self, codigo_empleado, apellidos, nombres, numero_documento, area_trabajo, hora_ingreso, temperatura_ingreso, hora_salida, temperatura_salida):
        self.codigo_empleado = codigo_empleado
        self.apellidos = apellidos
        self.nombres = nombres
        self.numero_documento = numero_documento
        self.area_trabajo = area_trabajo
        self.hora_ingreso = hora_ingreso
        self.temperatura_ingreso = temperatura_ingreso
        self.hora_salida = hora_salida
        self.temperatura_salida = temperatura_salida

    def mostrar_info(self):
        print(f"Código empleado: {self.codigo_empleado}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Nombres: {self.nombres}")
        print(f"Número de Documento: {self.numero_documento}")
        print(f"Área de Trabajo: {self.area_trabajo}")
        print(f"Hora de Ingreso: {self.hora_ingreso}")
        print(f"Temperatura de Ingreso: {self.temperatura_ingreso}°C")
        print(f"Hora de Salida: {self.hora_salida}")
        print(f"Temperatura de Salida: {self.temperatura_salida}°C")

    def editar_info(self):
        print("¿Qué información desea modificar?")
        campo = input("Ingrese el nombre del campo (apellidos, nombres, número_documento, área_trabajo, hora_ingreso, temperatura_ingreso, hora_salida, temperatura_salida): ")
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
        setattr(self, campo, nuevo_valor)
        print("Información actualizada.")

    def eliminar_usuario(self, lista_usuarios):
        lista_usuarios.remove(self)
        print(f"Usuario {self.nombres} eliminado.")

    def buscar_nombre_temp(self, lista_usuarios):
        print("\nUsuarios con temperatura mayor a 37.5°C:")
        for usuario in lista_usuarios:
            if usuario.temperatura_ingreso > 37.5:
                print(f"{usuario.apellidos} {usuario.nombres}")

    def buscar_por_cargo(self, lista_usuarios, cargo):
        print(f"\nUsuarios por cargo ({cargo}):")
        for usuario in lista_usuarios:
            if usuario.area_trabajo == cargo:
                print(f"{usuario.apellidos} {usuario.nombres}")

    def buscar_por_hora_llegada(self, lista_usuarios, hora):
        print(f"\nUsuarios que ingresaron a las {hora}:")
        for usuario in lista_usuarios:
            if usuario.hora_ingreso == hora:
                print(f"{usuario.apellidos} {usuario.nombres}")

    def buscar_por_hora_salida(self, lista_usuarios, hora):
        print(f"\nUsuarios que salieron a las {hora}:")
        for usuario in lista_usuarios:
            if usuario.hora_salida == hora:
                print(f"{usuario.apellidos} {usuario.nombres}")

class Empleado(Persona):
    def __init__(self, codigo_empleado, apellidos, nombres, numero_documento, area_trabajo, hora_ingreso, temperatura_ingreso, hora_salida, temperatura_salida, cargo, salario):
        super().__init__(codigo_empleado, apellidos, nombres, numero_documento, area_trabajo, hora_ingreso, temperatura_ingreso, hora_salida, temperatura_salida)
        self.cargo = cargo
        self.salario = salario

    def calcular_salario(self):
        print(f"El salario de {self.nombres} {self.apellidos} es {self.salario} USD.")
        return self.salario

class Visitante(Persona):
    def __init__(self, codigo_empleado, apellidos, nombres, numero_documento, hora_ingreso, temperatura_ingreso, hora_salida, temperatura_salida):
        super().__init__(codigo_empleado, apellidos, nombres, numero_documento, 'Visitante', hora_ingreso, temperatura_ingreso, hora_salida, temperatura_salida)

    def calcular_pago(self, horas_esperadas=2): 
        pago = horas_esperadas * 10 
        print(f"El pago para el visitante {self.nombres} {self.apellidos} es {pago} USD.")
        return pago

usuarios = []

empleado1 = Empleado(101, 'Gonzalez', 'Carlos', '12345678', 'Administrativo', '08:00', 36.8, '16:00', 37.1, 'Administrativo', 3000)
visitante1 = Visitante(102, 'Perez', 'Maria', '87654321', '08:15', 38.0, '12:00', 36.5)

usuarios.append(empleado1)
usuarios.append(visitante1)

empleado1.mostrar_info()
visitante1.mostrar_info()

empleado1.buscar_nombre_temp(usuarios)

empleado1.calcular_salario()

visitante1.calcular_pago()

empleado1.buscar_por_cargo(usuarios, 'Administrativo')

empleado1.buscar_por_hora_llegada(usuarios, '08:00')

empleado1.buscar_por_hora_salida(usuarios, '16:00')
