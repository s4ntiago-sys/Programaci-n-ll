#EJERCICIOS DE PRACTICA 2

#  1.
def area_perimetro_rectangulo(base, altura):
    perimetro = 2*altura + 2*base
    area = base * altura
    return perimetro, area

base = float(input("ingrese la base del rectangulo "))
altura = float(input("ingrese la altura del rectangulo "))
perimetro, area = area_perimetro_rectangulo(base, altura)
print("perimetro: ", perimetro, "area: ", area)

# 2.

import math

def area_perimetro_circulo():
    while True:
        try:
            radio = float(input("Introduce el radio del círculo (o escribe 'salir' para terminar): "))
            if radio < 0:
                print("El radio no puede ser negativo. Intenta de nuevo.")
                continue
            
            area = math.pi * radio**2
            perimetro = 2 * math.pi * radio
            
            print(f"Radio: {radio}")
            print(f"Perímetro: {perimetro:.2f}")
            print(f"Área: {area:.2f}")
        except ValueError:
            print("Saliendo del programa.")
            break

area_perimetro_circulo()


# 3.
def hallar_mayor_menor():
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        
        if a > b:
            mayor = a
            menor = b
        else:
            mayor = b
            menor = a
        
        print(f"Mayor: {mayor}")
        print(f"Menor: {menor}")
    except ValueError:
        print("Por favor, introduce números válidos.")

hallar_mayor_menor()


# 4.
def palabra_inversa():
    cadena = input("Introduce una palabra o frase: ")
    cadena_invertida = cadena[::-1]
    print(f"Cadena invertida: {cadena_invertida}")

palabra_inversa()

# 5.
import math

def suma():
    print("Suma: Introduce los números separados por espacio")
    numeros = list(map(float, input().split()))
    print(f"Resultado: {sum(numeros)}")

def resta():
    print("Resta: Introduce los números separados por espacio (restará en orden)")
    numeros = list(map(float, input().split()))
    resultado = numeros[0] - sum(numeros[1:])
    print(f"Resultado: {resultado}")

def multiplicacion():
    print("Multiplicación: Introduce los números separados por espacio")
    numeros = list(map(float, input().split()))
    resultado = 1
    for num in numeros:
        resultado *= num
    print(f"Resultado: {resultado}")

def division():
    print("División: Introduce los números separados por espacio (dividirá en orden)")
    numeros = list(map(float, input().split()))
    resultado = numeros[0]
    try:
        for num in numeros[1:]:
            resultado /= num
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

def potencia():
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    print(f"Resultado: {math.pow(base, exponente)}")

def porcentaje():
    total = float(input("Introduce el total: "))
    porcentaje = float(input("Introduce el porcentaje a calcular: "))
    print(f"Resultado: {total * (porcentaje / 100)}")

def raiz():
    numero = float(input("Introduce el número: "))
    indice = float(input("Introduce el índice de la raíz (ejemplo: 2 para raíz cuadrada): "))
    try:
        resultado = numero ** (1 / indice)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error: El índice de la raíz no puede ser cero.")

def menu():
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Porcentaje")
        print("7. Raíz")
        print("8. Salir")
        
        opcion = input("Elige una opción (1-8): ")
        
        if opcion == '1':
            suma()
        elif opcion == '2':
            resta()
        elif opcion == '3':
            multiplicacion()
        elif opcion == '4':
            division()
        elif opcion == '5':
            potencia()
        elif opcion == '6':
            porcentaje()
        elif opcion == '7':
            raiz()
        elif opcion == '8':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

menu()

# 6. 
def relacion(a, b):
    if a > b:
        return "True"
    elif a < b:
        return "False"
    else:
        return "Empate"
def main():
    while True:
        try:
            print("\nEstablecer relación entre dos números")
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            
            resultado = relacion(a, b)
            print(f"Resultado: {resultado}")
            
            continuar = input("¿Quieres comparar otros números? (sí/no): ").lower()
            if continuar != 'sí':
                print("Saliendo del programa. ¡Adiós!")
                break
        except ValueError:
            print("Por favor, introduce valores numéricos válidos.")

main()


# 7.

def Separar(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    pares.sort()
    impares.sort()
    return pares, impares

def main():
    try:
        numeros = list(map(int, input("Introduce una lista de números enteros separados por espacio: ").split()))
        
        pares, impares = Separar(numeros)
        
        print(f"Números pares ordenados: {pares}")
        print(f"Números impares ordenados: {impares}")
    except ValueError:
        print("Por favor, introduce solo números enteros.")

main()
