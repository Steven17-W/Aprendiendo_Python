#----------- Clase 3 de Python -------------------


#----------- Ejercicio 1 ------------------- Mayor de edad

"""Edad =int(input("¿Cual es tu edad?"))
if Edad >= 18:
    print("Eres mayor de edad")
else:
    print("Menor de edad")"""


#----------- Ejercicio 2 ------------------- Resultado de 2 numeros +-*/

"""Num1 = int(input("Ingresa el primer numero"))
Num2 = int(input("Ingresa el Segundo numero"))

Suma= (Num1+Num2)
print(Suma)
Resta= (Num1-Num2)
print(Resta)
Multi= (Num1*Num2)
print(Multi)
Division= (Num1/Num2)
print(Division)"""

#----------- Ejercicio 3 ------------------- Cuadrado de un numero "Potenciacion y pidiendo el numeor por consola"

"""Numero=int(input("Ingresa un numero a elevar al cuadrado: "))
Resultado=Numero**2
print(Resultado)"""

#----------- Ejercicio 5 ------------------- Condicional para identificar si una persona tiene 13 y 18 años, si es mayor de edad tambien que me diga si es hombre o mujer

"""Genero=str(input("Eres hombre o Mujer"))
edad=int(input("Cuantos años tienes?"))

if edad>=18:
    print("Eres mayor de edad")
elif edad>=13:
    print("Eres mas grande, pero aun no mayor de edad")
elif edad>=0:
    print("Eres un niño")
else:
    print("Resultado no viable")"""


#----------- Ejercicio 6 ----------------- Diccionarion con Genero, edad, descripcion

"""Diccionario_datos={"Genero":"Masculino",'Edad':24,"Descripcion":"Me gusta jugar futbol"}
print(Diccionario_datos)"""

#----------- Ejercicio 7 ----------------- Nombre de usuario y poner letras mayusculas
"""NombreUsuario=input("Ingresa tu nombre")
print(NombreUsuario.title())"""

#----------- Ejercicio 8 ----------------- Nombre de usuario y cambiar primera letra

"""NombreUsuario=("Steven")
print(NombreUsuario.replace("S","W"))"""

#----------- Ejercicio 9 ----------------- Cuente una letra especifica

"""Parrafo=str(input("ingresa parrafo"))
print(Parrafo.count("a"))"""

#----------- Ejercicio 10 --------------------- Numero par o inpar

"""numero=int(input("Ingresa un numero, y verifica si es par o inpar"))
if numero/2 == 0:
    print("Tu numero es par")
else:
    print("Tu numero es inpar")"""

#----------- Ejercicio 11 --------------------- Recibir dos cadenas del usuario, concatene y muestre

"""Espacio=" "
Cadena1=str(input("Ingresa tu primer cadena "))
Cadena2=str(input("Ingresa tu segunda cadena "))

Cadena_Completa = Cadena1+Espacio+Cadena2

print(Cadena_Completa)"""


#---------------- Ciclos y bucles --------------

#Son estructuras de codigo que me permiten iterar, sobre una estructura o rango, existen 2 tipos de ciclos mas usados los FOR que significa (para) o los WHILE que significa (Mientras que)

# Estructura de los ciclos for

"""for <Variable>int<lista>:
    <Ejecutable>"""

Paises = ["Rusia","Francia", "Paraguay","Colombia","Venezuela","Chile"]

#Imprimir cada pais
"""for i in Paises:
    print(i)"""

#Busqueda de dato en una lista
"""for i in Paises:
    if i == "Chile":
        print(i,"Este pais es infiltrado")"""


#Numeracion de items de la lista
"""for numero , i in enumerate(Paises):
    print(numero)
    print(i)"""

#-----------------FUNCIONES-------------------

#len me da la longitud de un arreglo

"""print(len(Paises))

#Funsion max me muestra el numero mas grande

max([1,2,3,,4,5])

#Funsion min me muestra el numero mas bajo

min([1,2,3,,4,5])

#Funsion type tipo de dato

type(Paises)

#round me permite redondear decimales
round(3.1416,2)"""

#range me sirve para crear secuencia de numeros, tiene 3 argumentos, el inicio, el final, el paso
"""contando = range(0,200,5)


for i in contando:
    print(contando)


#Las funciones propias, son las que yo creo y me sirven para reutilizar codigo
def suma(a,b):
    resultado=a*b
    return resultado""" 

"""def Precio_pan(cantidad,Precio):
    resultado=cantidad*Precio
    return resultado

Pregunta=int(input("Buenos dias, cuantos panes quiere"))
Valor=int(input("Precio del pan"))
print(Precio_pan(Pregunta,Valor))"""

"""def divicion(b,c):
    resultado_divicion=b/c
    return resultado_divicion

print()"""


"""Calcule el total de compra de un supermercado, 
 el usurio debe ingresar el precio de 2 productos 
 y las cantidades que quiere comprar de cada uno, 
 luego el programa debera permitir al usuario sumar 
 el precio de ambos productos. multiplicar por las 
 cantidaes de productos para obtener el precio total, 
 restar un descuento del precio total si el usuariario tiene un cupon, 
 dividir el valor total en 2 personas"""

# M - S - R - D

def M(valor1,valor2):
    resultadoM=valor1*valor2
    return resultadoM

def S(valor1,valor2):
    resultadoS=valor1+valor2
    return resultadoS
    
def R(valor1,valor2):
    resultadoR=valor1-valor2
    return resultadoR

def D(valor1,valor2):
    if valor2 != 0:
        return valor1/valor2
    else:
        return print("No se puede dividir entre 0")
 

print("Bienvenido a Supermarket")
Producto_1=float(input( "Ingrese el valor del producto1: "))
Cantidad_1=int(input("Ingrese la cantidad que quiere llevar del 1r producto: "))

Producto_2=float(input( "Ingrese el valor del producto2: "))
Cantidad_2=int(input("Ingrese la cantidad que quiere llevar del 2do producto: "))

operacion=("""Bienvenido como estas dime que quieres hacer
1. Sumar los precios de ambos productos
2. calcular el costo total multiplicando precio por cantidad
3. Aplicar un descuento al total 
4. Dividir el total en 2 personas
No olvides que solo tienes las opciones 1,2,3,4: """)

if operacion=="1":
    total_precio=S(Producto_1,Producto_2)
    print(total_precio)

if operacion=="2":
    Costo_total=M(Producto_1,Producto_2)
    print(Costo_total)

if operacion=="3":
    Costo_total=M(Producto_1,Producto_2)
    Descuento = input("De cuanto es tu descuento")
    Total_Con_Descuento = R(Costo_total,Descuento)
    print(Total_Con_Descuento)

if operacion=="4":
    total_precio=S(Producto_1,Producto_2)
    PrecioPorPersona=D(total_precio,2)
    print(PrecioPorPersona)
    


