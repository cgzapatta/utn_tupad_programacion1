#Ejercicio 1
print("Hola mundo")

#Ejercicio 2
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = int(input("Ingrese su edad:"))
residencia = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
pi = 3.14
radio = int(input("Ingrese el radio de un circulo:"))
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"El area es {area}, el perimetro es: {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos:"))
horas = segundos / 3600
print(f"La cantidad de horas es: {horas}")

#Ejercicio 6
numero = int(input("Ingresá un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7
numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("Ingrese otro numero:"))
suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
division = numero1 / numero2
print(f"La suma es: {suma}, la resta es: {resta}, la multiplicacion es: {multi}, la division es: {division}")

#Ejercicio 8
altura = float(input("Ingrese su altura:"))
peso = float(input("Ingrese su peso:"))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")

#Ejercicio 9
celsius = int(input("Ingrese temperatura en grados celsius:"))
faren = ((9/5) * celsius) + 32
print(f"La temperatura en grados fahrenheit es: {faren}")

#Ejercicio 10
n1 = int(input("Ingrese un numero:"))
n2 = int(input("Ingrese otro numero:"))
n3 = int(input("Ingrese otro numero:"))
promedio = (n1+n2+n3) / 3
print(f"El promedio es: {promedio}")