#EJERCICIOS DE PRACTICA 2

#  1.
def agregar_contacto(base_datos):
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    documento = input("Introduce el documento de identidad: ")
    direccion = input("Introduce la dirección de residencia: ")
    telefono = input("Introduce el número de teléfono: ")
    contacto = (nombre, apellido, documento, direccion, telefono)
    base_datos.append(contacto)

def mostrar_contactos(base_datos):
    if not base_datos:
        print("No hay contactos en la base de datos.")
    else:
        print("\nLista de contactos:")
        for i, contacto in enumerate(base_datos, 1):
            print(f"{i}. Nombre: {contacto[0]}, Apellido: {contacto[1]}, Documento: {contacto[2]}, Dirección: {contacto[3]}, Teléfono: {contacto[4]}")

def menu():
    base_datos = []
    while True:
        print("\n1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_contacto(base_datos)
        elif opcion == '2':
            mostrar_contactos(base_datos)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()


# 2.
def mostrar_mes():
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    
    while True:
        try:
            numero = int(input("Introduce un número entre 1 y 12 (0 para salir): "))
            
            if numero == 0:
                print("Saliendo del programa.")
                break
            elif 1 <= numero <= 12:
                print(f"El mes en la posición {numero} es: {meses[numero - 1]}")
            else:
                print("Número fuera de rango. Debe ser entre 1 y 12.")
        except ValueError:
            print("Por favor, introduce un número válido.")

mostrar_mes()


# 3. 
def agregar_contacto(base_datos):
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    documento = input("Introduce el documento de identidad: ")
    direccion = input("Introduce la dirección de residencia: ")
    telefono = input("Introduce el número de teléfono: ")
    contacto = [nombre, apellido, documento, direccion, telefono]
    base_datos.append(contacto)

def mostrar_contactos(base_datos):
    if not base_datos:
        print("No hay contactos en la base de datos.")
    else:
        print("\nLista de contactos:")
        for i, contacto in enumerate(base_datos, 1):
            print(f"{i}. Nombre: {contacto[0]}, Apellido: {contacto[1]}, Documento: {contacto[2]}, Dirección: {contacto[3]}, Teléfono: {contacto[4]}")

def editar_contacto(base_datos):
    if not base_datos:
        print("No hay contactos para editar.")
        return
    mostrar_contactos(base_datos)
    try:
        indice = int(input("Introduce el número del contacto que deseas editar: ")) - 1
        if 0 <= indice < len(base_datos):
            nueva_direccion = input("Introduce la nueva dirección: ")
            nuevo_telefono = input("Introduce el nuevo número de teléfono: ")
            base_datos[indice][3] = nueva_direccion
            base_datos[indice][4] = nuevo_telefono
            print("Datos actualizados correctamente.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Opción no válida.")

def menu():
    base_datos = []
    while True:
        print("\n1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Editar contacto")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_contacto(base_datos)
        elif opcion == '2':
            mostrar_contactos(base_datos)
        elif opcion == '3':
            editar_contacto(base_datos)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()


# 4.
def llenar_lista():
    lista = []
    while True:
        try:
            numero = int(input("Introduce un número (0 para terminar): "))
            if numero == 0:
                break
            lista.append(numero)
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    lista.sort()
    return lista

def separar_pares_impares(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares

def main():
    lista = llenar_lista()
    pares, impares = separar_pares_impares(lista)
    
    print(f"Lista ordenada: {lista}")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")

main()

# 5. 
def sumar(lista):
    total = sum(lista)
    return total

def multiplicar(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def ingresar_numeros():
    lista = []
    while True:
        try:
            numero = int(input("Introduce un número (0 para terminar): "))
            if numero == 0:
                break
            lista.append(numero)
        except ValueError:
            print("Por favor, introduce un número válido.")
    return lista

def main():
    numeros = ingresar_numeros()
    print(f"La suma de los números es: {sumar(numeros)}")
    print(f"La multiplicación de los números es: {multiplicar(numeros)}")

main()


# 6. 
def ingresar_nombres():
    lista = []
    n = int(input("¿Cuántos estudiantes deseas ingresar? "))
    for _ in range(n):
        nombre = input("Introduce el nombre del estudiante: ")
        lista.append(nombre)
    return lista

def buscar_nombre(lista):
    nombre_buscado = input("Introduce el nombre a buscar: ")
    if nombre_buscado in lista:
        print(f"{nombre_buscado} está en la lista de estudiantes.")
    else:
        print(f"{nombre_buscado} no está en la lista de estudiantes.")

def main():
    lista_estudiantes = ingresar_nombres()
    buscar_nombre(lista_estudiantes)

main()


# 7.
def ver_traducciones(traductor):
    print("\nDiccionario actual:")
    for espanol, ingles in traductor.items():
        print(f"{espanol} -> {ingles}")

def traducir(traductor):
    palabra = input("\nIntroduce una palabra en español para traducir: ").lower()
    if palabra in traductor:
        print(f"La traducción de '{palabra}' es: {traductor[palabra]}")
    else:
        print(f"La palabra '{palabra}' no está registrada en el diccionario.")
        agregar = input("¿Deseas agregarla? (s/n): ").lower()
        if agregar == 's':
            traduccion = input("Introduce la traducción al inglés: ").lower()
            traductor[palabra] = traduccion
            print(f"Palabra '{palabra}' agregada al diccionario con la traducción '{traduccion}'.")

def eliminar_palabra(traductor):
    palabra = input("\nIntroduce la palabra en español que deseas eliminar: ").lower()
    if palabra in traductor:
        del traductor[palabra]
        print(f"La palabra '{palabra}' ha sido eliminada del diccionario.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en el diccionario.")

def editar_palabra(traductor):
    palabra = input("\nIntroduce la palabra en español que deseas editar: ").lower()
    if palabra in traductor:
        nueva_traduccion = input(f"La traducción actual de '{palabra}' es '{traductor[palabra]}'. Introduce la nueva traducción: ").lower()
        traductor[palabra] = nueva_traduccion
        print(f"Traducción de '{palabra}' actualizada a '{nueva_traduccion}'.")
    else:
        print(f"La palabra '{palabra}' no está en el diccionario.")

def menu():
    traductor = {
        'auto': 'car', 'azul': 'blue', 'red': 'rojo', 'volar': 'fly', 'blanco': 'white',
        'casa': 'house', 'clase': 'class', 'futbol': 'soccer', 'hora': 'hour', 'cama': 'bathroom'
    }

    while True:
        print("\nSeleccione una opción:")
        print("1. Ver traducciones")
        print("2. Traducir palabra")
        print("3. Agregar palabra")
        print("4. Eliminar palabra")
        print("5. Editar palabra")
        print("6. Salir")

        opcion = input("\nIngrese una opción: ")

        if opcion == '1':
            ver_traducciones(traductor)
        elif opcion == '2':
            traducir(traductor)
        elif opcion == '3':
            traducir(traductor) 
        elif opcion == '4':
            eliminar_palabra(traductor)
        elif opcion == '5':
            editar_palabra(traductor)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()

# 8. 
def agregar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ")
    apellido = input("Introduce el apellido del contacto: ")
    telefono = input("Introduce el número de teléfono: ")
    correo = input("Introduce el correo electrónico: ")
    direccion = input("Introduce la dirección de residencia: ")
    cumpleanos = input("Introduce la fecha de cumpleaños (dd/mm/aaaa): ")
    
    agenda[nombre] = {
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
        'direccion': direccion,
        'cumpleanos': cumpleanos
    }
    print(f"Contacto de {nombre} {apellido} agregado con éxito.")

def ver_contactos(agenda):
    if len(agenda) == 0:
        print("No hay contactos registrados.")
    else:
        print("\nContactos registrados:")
        for nombre, datos in agenda.items():
            print(f"{nombre} {datos['apellido']}")
            print(f"  Teléfono: {datos['telefono']}")
            print(f"  Correo: {datos['correo']}")
            print(f"  Dirección: {datos['direccion']}")
            print(f"  Cumpleaños: {datos['cumpleanos']}")
            print("-" * 40)

def editar_contacto(agenda):
    nombre = input("\nIntroduce el nombre del contacto que deseas editar: ")
    if nombre in agenda:
        print(f"Editando contacto de {nombre} {agenda[nombre]['apellido']}")
        agenda[nombre]['telefono'] = input("Nuevo teléfono: ")
        agenda[nombre]['correo'] = input("Nuevo correo: ")
        agenda[nombre]['direccion'] = input("Nueva dirección: ")
        agenda[nombre]['cumpleanos'] = input("Nuevo cumpleaños (dd/mm/aaaa): ")
        print(f"Contacto de {nombre} actualizado.")
    else:
        print("El contacto no existe.")

def eliminar_contacto(agenda):
    nombre = input("\nIntroduce el nombre del contacto que deseas eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto de {nombre} eliminado.")
    else:
        print("El contacto no existe.")

def menu():
    agenda = {}
    
    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            ver_contactos(agenda)
        elif opcion == '3':
            editar_contacto(agenda)
        elif opcion == '4':
            eliminar_contacto(agenda)
        elif opcion == '5':
            print(f"\nAgenda telefónica finalizada. Total de contactos: {len(agenda)}")
            for nombre in agenda:
                print(f"- {nombre}")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()

# 9. 
def agregar_libro(biblioteca):
    print("\nAgregar un nuevo libro")
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    anio = input("Introduce el año de publicación: ")
    referencia = input("Introduce el número de referencia del libro: ")

    biblioteca[titulo] = {
        'autor': autor,
        'anio': anio,
        'referencia': referencia,
        'consultado': 0 
    }
    print(f"Libro '{titulo}' agregado con éxito.")

def registrar_usuario(usuarios):
    print("\nRegistrar nuevo usuario")
    nombre_usuario = input("Introduce el nombre del usuario: ")
    usuarios.append(nombre_usuario)
    print(f"Usuario '{nombre_usuario}' registrado con éxito.")

def consultar_libro(biblioteca):
    print("\nConsultar un libro")
    consulta = input("Introduce el título o autor del libro a consultar: ").lower()

    libros_encontrados = [titulo for titulo, datos in biblioteca.items() if consulta in titulo.lower() or consulta in datos['autor'].lower()]

    if libros_encontrados:
        for titulo in libros_encontrados:
            biblioteca[titulo]['consultado'] += 1 
            print(f"Libro encontrado: {titulo}")
            print(f"  Autor: {biblioteca[titulo]['autor']}")
            print(f"  Año: {biblioteca[titulo]['anio']}")
            print(f"  Número de referencia: {biblioteca[titulo]['referencia']}")
    else:
        print("No se encontraron libros con ese título o autor.")

def menu():
    biblioteca = {
        'Cien años de soledad': {'autor': 'Gabriel García Márquez', 'anio': '1967', 'referencia': '001', 'consultado': 0},
        'Don Quijote de la Mancha': {'autor': 'Miguel de Cervantes', 'anio': '1605', 'referencia': '002', 'consultado': 0},
        'La casa de los espíritus': {'autor': 'Isabel Allende', 'anio': '1982', 'referencia': '003', 'consultado': 0},
        'El amor en los tiempos del cólera': {'autor': 'Gabriel García Márquez', 'anio': '1985', 'referencia': '004', 'consultado': 0},
        '1984': {'autor': 'George Orwell', 'anio': '1949', 'referencia': '005', 'consultado': 0}
    }
    usuarios = []
    consultas_realizadas = 0

    while True:
        print("\nOpciones:")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Consultar libro por título o autor")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_libro(biblioteca)
        elif opcion == '2':
            registrar_usuario(usuarios)
        elif opcion == '3':
            consultar_libro(biblioteca)
            consultas_realizadas += 1
        elif opcion == '4':
            print("\nInforme final:")
            print(f"Total de libros consultados: {consultas_realizadas}")
            print(f"Total de usuarios registrados: {len(usuarios)}")
            print(f"Total de libros en la biblioteca: {len(biblioteca)}")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()

# 10.
import time

vehiculos = {}
dinero_recolectado = 0
motos_entradas = 0
carros_entrados = 0

tarifa_moto = 2000
tarifa_auto = 3000

def registrar_vehiculo():
    global motos_entradas, carros_entrados
    tipo_vehiculo = input("¿El vehículo es una moto o un carro? (moto/carro): ").lower()
    if tipo_vehiculo not in ['moto', 'carro']:
        print("Tipo de vehículo no válido.")
        return

    codigo_usuario = str(time.time()).replace(".", "")[:5]
    hora_entrada = time.time()

    vehiculos[codigo_usuario] = {
        'tipo': tipo_vehiculo,
        'hora_entrada': hora_entrada
    }

    if tipo_vehiculo == 'moto':
        motos_entradas += 1
    else:
        carros_entrados += 1

    print(f"Vehículo registrado con éxito. Código de usuario: {codigo_usuario}")

def cobrar_salida():
    global dinero_recolectado
    codigo_usuario = input("Introduce el código de usuario del vehículo: ")

    if codigo_usuario not in vehiculos:
        print("Código de usuario no encontrado.")
        return

    hora_salida = time.time()
    vehiculo = vehiculos[codigo_usuario]
    tipo = vehiculo['tipo']
    hora_entrada = vehiculo['hora_entrada']
    tiempo_parqueo = (hora_salida - hora_entrada) / 3600
    fracciones = int(tiempo_parqueo) + (1 if tiempo_parqueo % 1 > 0 else 0)

    if tipo == 'moto':
        costo = fracciones * tarifa_moto
    else:
        costo = fracciones * tarifa_auto

    dinero_recolectado += costo
    print(f"El cobro es de {costo} pesos.")

    dinero_recibido = float(input("Introduce el dinero recibido: "))
    if dinero_recibido < costo:
        print("Dinero insuficiente.")
        return

    cambio = dinero_recibido - costo
    print(f"El cambio a devolver es: {cambio} pesos.")
    del vehiculos[codigo_usuario]

def menu():
    while True:
        print("\nOpciones:")
        print("1. Registrar vehículo")
        print("2. Cobrar salida")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registrar_vehiculo()
        elif opcion == '2':
            cobrar_salida()
        elif opcion == '3':
            print(f"Total de dinero recolectado: {dinero_recolectado}")
            print(f"Total de motos entradas: {motos_entradas}")
            print(f"Total de carros entradas: {carros_entrados}")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()


# 11. 
def calcular_media_ponderada(calificaciones, creditos):
    total_pesos = sum(creditos)
    suma_ponderada = sum([calificacion * credito for calificacion, credito in zip(calificaciones, creditos)])
    return suma_ponderada / total_pesos

def calcular_media_aritmetica(calificaciones):
    return sum(calificaciones) / len(calificaciones)

materias = ["Differential Equations", "Physics III", "Computer Programming II", "Electrical Circuits II", "Engineering Drawing"]
creditos = [4, 4, 3, 3, 3]
calificaciones = []

for materia in materias:
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación para {materia}: "))
            if 0 <= calificacion <= 5:
                calificaciones.append(calificacion)
                break
            else:
                print("Por favor ingrese una calificación entre 0 y 5.")
        except ValueError:
            print("Por favor ingrese un número válido.")

media_ponderada = calcular_media_ponderada(calificaciones, creditos)
media_aritmetica = calcular_media_aritmetica(calificaciones)

print("Media ponderada:", media_ponderada)
print("Media aritmética:", media_aritmetica)
