#EJERCICIOS DE PRACTICA 2

# 1.
salario_minimo = 1300000

def verificar_salario():
    empleados = []
    num_empleados = int(input("¿Cuántos empleados desea ingresar? "))

    for _ in range(num_empleados):
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        documento = input("Ingrese el documento de identidad del empleado: ")
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        if sueldo > salario_minimo:
            gana_mas_que_minimo = True
        else:
            gana_mas_que_minimo = False
        empleado = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Documento": documento,
            "Sueldo": sueldo,
            "Gana más que el salario mínimo": gana_mas_que_minimo
        }

        empleados.append(empleado)

    for empleado in empleados:
        print("\nDatos del empleado:")
        print(f"Nombre: {empleado['Nombre']}")
        print(f"Apellido: {empleado['Apellido']}")
        print(f"Documento: {empleado['Documento']}")
        print(f"Sueldo: {empleado['Sueldo']}")
        if empleado["Gana más que el salario mínimo"]:
            print("Este empleado gana más que el salario mínimo.")
        else:
            print("Este empleado no gana más que el salario mínimo.")

verificar_salario()

#2
import math

a = float(input('Introduce el coeficiente a: '))
b = float(input('Introduce el coeficiente b: '))
c = float(input('Introduce el coeficiente c: '))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f'Existen dos raíces reales distintas: {raiz1} y {raiz2}')

elif discriminante == 0:
    raiz = -b / (2*a)
    print(f'Existen dos raíces reales iguales: {raiz}')

else:
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(-discriminante) / (2*a)
    print(f'Existen dos raíces complejas: {parte_real} + {parte_imaginaria}i y {parte_real} - {parte_imaginaria}i')

#3
letra = input('Introduce una letra: ')

if len(letra) != 1:
    print('No se puede procesar el dato. Debes ingresar solo un carácter.')
else:
    letra = letra.lower()
    
    if letra in 'aeiou':
        print('Es vocal')
    else:
        print('No es vocal')

#4
import math

def mostrar_menu():
    opciones = {
        1: "Suma",
        2: "Resta",
        3: "Multiplicación",
        4: "División",
        5: "Comparar si un número es par o impar",
        6: "Calcular porcentaje",
        7: "Calcular valores de razones trigonométricas (seno, coseno, tangente)",
        8: "Salir"}
    
    print("\n--- Menú de la Calculadora ---")
    for clave, valor in opciones.items():
        print(f"{clave}. {valor}")
mostrar_menu()

def es_par_o_impar(num):
    if num % 2 == 0:
        return f"El número {num} es par."
    else:
        return f"El número {num} es impar."

def calcular_porcentaje(total, porcentaje):
    return (total * porcentaje) / 100

def menu_trigonometria():
    angulo = float(input("Introduce el ángulo en grados: "))
    # Convertir grados a radianes
    radianes = math.radians(angulo)
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    tangente = math.tan(radianes)
    print(f"Seno({angulo}) = {seno}")
    print(f"Coseno({angulo}) = {coseno}")
    print(f"Tangente({angulo}) = {tangente}")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':  
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado de la suma es: {num1 + num2}")
        
        elif opcion == '2': 
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado de la resta es: {num1 - num2}")
        
        elif opcion == '3': 
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado de la multiplicación es: {num1 * num2}")
        
        elif opcion == '4': 
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            if num2 != 0:
                print(f"El resultado de la división es: {num1 / num2}")
            else:
                print("No se puede dividir entre 0.")
        
        elif opcion == '5': 
            num = int(input("Introduce un número entero: "))
            print(es_par_o_impar(num))
        
        elif opcion == '6': 
            total = float(input("Introduce el valor total: "))
            porcentaje = float(input("Introduce el porcentaje a calcular: "))
            print(f"El {porcentaje}% de {total} es: {calcular_porcentaje(total, porcentaje)}")
        
        elif opcion == '7':
            menu_trigonometria()
        
        elif opcion == '8':  
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor elija una opción del menú.")

calculadora()

#5

def convertir_unidad(valor, de_unidad, a_unidad):
    
    if de_unidad == "metros":
        valor_cm = valor * 100
    elif de_unidad == "kilometros":
        valor_cm = valor * 100000
    elif de_unidad == "centimetros":
        valor_cm = valor
    elif de_unidad == "millas":
        valor_cm = valor * 160934
    elif de_unidad == "yardas":
        valor_cm = valor * 91.44
    elif de_unidad == "pies":
        valor_cm = valor * 30.48
    elif de_unidad == "pulgadas":
        valor_cm = valor * 2.54
    else:
        raise ValueError("Unidad de entrada no válida")

    if a_unidad == "metros":
        return valor_cm / 100
    elif a_unidad == "kilometros":
        return valor_cm / 100000
    elif a_unidad == "centimetros":
        return valor_cm
    elif a_unidad == "millas":
        return valor_cm / 160934
    elif a_unidad == "yardas":
        return valor_cm / 91.44
    elif a_unidad == "pies":
        return valor_cm / 30.48
    elif a_unidad == "pulgadas":
        return valor_cm / 2.54
    else:
        raise ValueError("Unidad de salida no válida")

def main():
    print("Opciones de unidades: metros, kilometros, centimetros, millas, yardas, pies, pulgadas")
    
    de_unidad = input("Ingrese la unidad de entrada: ").strip().lower()
    a_unidad = input("Ingrese la unidad de salida: ").strip().lower()
    valor = float(input(f"Ingrese la distancia en {de_unidad}: "))
    
    resultado = convertir_unidad(valor, de_unidad, a_unidad)
    print(f"{valor} {de_unidad} son {resultado} {a_unidad}")

if __name__ == "__main__":
    main()

#6
def main():
    print("Por favor, elija un candidato para votar:")
    print("A - Candidato A")
    print("B - Candidato B")
    print("C - Candidato C")
    print("V - Voto en blanco")

    voto = input("Ingrese su opción (A, B, C, V): ").strip().upper()

    if voto == "A":
        print("Usted ha votado por el candidato A")
    elif voto == "B":
        print("Usted ha votado por el candidato B")
    elif voto == "C":
        print("Usted ha votado por el candidato C")
    elif voto == "V":
        print("Usted ha votado en blanco")
    else:
        print("Opción errónea")

if __name__ == "__main__":
    main()

#7
def main():
    n = int(input("Ingrese la cantidad de estudiantes: "))
    estudiantes = []

    for i in range(n):
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
        estudiantes.append(nombre)

    while True:
        consulta = input("Ingrese el nombre a buscar (o 'salir' para terminar): ").strip()
        if consulta.lower() == 'salir':
            break
        
        encontrado = False
        for estudiante in estudiantes:
            if estudiante.lower() == consulta.lower():
                encontrado = True
                break

        if encontrado:
            print(f"{consulta} está en la lista de estudiantes.")
        else:
            print(f"{consulta} no se encuentra en la lista de estudiantes.")

if __name__ == "__main__":
    main()

#8

def main():
    numeros = []
    
    for i in range(5):
        while True:
            try:
                numero = int(input(f"Ingrese el número entero {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    suma_negativos = sum(n for n in numeros if n < 0)
    positivos = [n for n in numeros if n > 0]

    if positivos:
        promedio_positivos = sum(positivos) / len(positivos)
    else:
        promedio_positivos = 0 
    print(f"La sumatoria de los números negativos es: {suma_negativos}")
    print(f"El promedio de los números positivos es: {promedio_positivos}")

if __name__ == "__main__":
    main()

#9

def main():
    primer_numero = int(input("Ingrese un número entero: "))
    anterior = primer_numero

    while True:
        # Solicitar un nuevo número
        numero = int(input("Ingrese otro número entero: "))
        
        if numero < anterior:
            print(f"El número {numero} es menor que el anterior ({anterior}). Fin del programa.")
            break
        else:
            anterior = numero  

if __name__ == "__main__":
    main()

#10

def contar_mayusculas(cadena):
    contador = sum(1 for letra in cadena if letra.isupper())
    return contador

def main():
    cadena = input("Ingrese una cadena: ")
    
    cantidad_mayusculas = contar_mayusculas(cadena)
    
    print(f"La cantidad de letras mayúsculas en la cadena es: {cantidad_mayusculas}")

if __name__ == "__main__":
    main()

#11

import random

def jugar_contra_pc():
    opciones = ['piedra', 'papel', 'tijera']
    puntos_jugador = 0
    puntos_pc = 0
    
    while True:
        jugador = input("Elija piedra, papel o tijera (o 'salir' para terminar): ").lower()
        if jugador == 'salir':
            break
        if jugador not in opciones:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        pc = random.choice(opciones)
        print(f"PC eligió: {pc}")
        
        if jugador == pc:
            print("¡Es un empate!")
        elif (jugador == 'piedra' and pc == 'tijera') or \
             (jugador == 'papel' and pc == 'piedra') or \
             (jugador == 'tijera' and pc == 'papel'):
            print("¡Ganaste esta ronda!")
            puntos_jugador += 1
        else:
            print("¡PC ganó esta ronda!")
            puntos_pc += 1
    
    return puntos_jugador, puntos_pc

def jugar_multijugador():
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    
    while True:
        jugador1 = input("Jugador 1, elija piedra, papel o tijera (o 'salir' para terminar): ").lower()
        if jugador1 == 'salir':
            break
        jugador2 = input("Jugador 2, elija piedra, papel o tijera: ").lower()
        
        if jugador1 not in ['piedra', 'papel', 'tijera'] or jugador2 not in ['piedra', 'papel', 'tijera']:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        print(f"Jugador 1 eligió: {jugador1}")
        print(f"Jugador 2 eligió: {jugador2}")
        
        if jugador1 == jugador2:
            print("¡Es un empate!")
        elif (jugador1 == 'piedra' and jugador2 == 'tijera') or \
             (jugador1 == 'papel' and jugador2 == 'piedra') or \
             (jugador1 == 'tijera' and jugador2 == 'papel'):
            print("¡Jugador 1 ganó esta ronda!")
            puntos_jugador1 += 1
        else:
            print("¡Jugador 2 ganó esta ronda!")
            puntos_jugador2 += 1
    
    return puntos_jugador1, puntos_jugador2

def main():
    print("Bienvenido al juego Piedra, Papel y Tijera")
    modo = input("Elija modo de juego: (1) Contra PC (2) Multijugador: ")
    
    if modo == '1':
        puntos_jugador, puntos_pc = jugar_contra_pc()
        print(f"Final del juego: Jugador: {puntos_jugador} - PC: {puntos_pc}")
        if puntos_jugador > puntos_pc:
            print("¡El jugador ganó el juego!")
        elif puntos_jugador < puntos_pc:
            print("¡La PC ganó el juego!")
        else:
            print("¡El juego terminó en empate!")
    elif modo == '2':
        puntos_jugador1, puntos_jugador2 = jugar_multijugador()
        print(f"Final del juego: Jugador 1: {puntos_jugador1} - Jugador 2: {puntos_jugador2}")
        if puntos_jugador1 > puntos_jugador2:
            print("¡Jugador 1 ganó el juego!")
        elif puntos_jugador1 < puntos_jugador2:
            print("¡Jugador 2 ganó el juego!")
        else:
            print("¡El juego terminó en empate!")
    else:
        print("Modo no válido.")

if __name__ == "__main__":
    main()
