#Declaracion de variables
nombre="Steven"
apellido="Garzón"
edad=38
cedula= 1007389590
estado_civil="Union Libre"
estatura = 1,75

#////// Lista //////////

datos = []

datos.append(nombre)
datos.append(apellido)
datos.append(edad)
datos.append(cedula)
datos.append(estado_civil)
datos.append(estatura)

#print(datos)

familiares = []

familiares.append("Natalia")
familiares.append("Leidy")
familiares.append("Alicia")
familiares.append("Felipe")
familiares.append("Samuel")

print(familiares)

familiares.insert(1,23)
familiares.insert(3,43)
familiares.insert(5,63)
familiares.insert(7,43)
familiares.insert(9,63)

print(familiares)

#edad_1=input("Hola, que te parece si antes de apostar tu casa vemos si eres mayor de edad, ingresa tu edad: ")

#nombre_1=input("Ingresa tu nombre: ")
#print("Mucho gusto", nombre_1)

paises = ["Venezuela","Mexico","Francia","China","Paraguay","Rusia","Ecuador","Colombia"]

#Para remover datos de las listas utilizo el metodo remove
paises.remove("Rusia")

#Otro metodo para eliminar es el método pop, este me permite eliminar por posicion
paises.pop(4)

#Para eliminar definitivamente se usa del
del paises[5]

#Ordenar las listas, las puedo ordenar de menor a mayor o alfabeticamente, con el metodo sort
paises.sort()
print(paises)


digitos=[2,9,3,8,3,6,4]
digitos.sort()
print(digitos)

digitos.sort(reverse=True)
print(digitos)

#Copia de BD
paises_copia=paises.copy()
print(paises_copia)

#Corta la lista de principio a fin
paises_copia2=paises[:]
print(paises_copia2)

#Diccionarios son tipos de datos que tienen una llave y un valor, a la combinacion de llave con valor
#se le conoce como items, en los diccionarios puedo usar metodos parecidos a los de las listas

diccionario_ing_esp={"casa":"house","entender":"understand","sediento":"thirty","rojo":"red","ocupado":"bussy"}
print(diccionario_ing_esp)


#Para ver un valor de una llave determinada, lo hago de la siguiente manera
diccionario_ing_esp['casa']

#Para traer todas las llaves de un diccionario, puedo usar el metodo keys
diccionario_ing_esp.keys()

#Para trer los valores de los diccionarios
diccionario_ing_esp.values()

#para traer todo el diccionario nombre del diccionario o items
diccionario_ing_esp.items()

#Tipo de dato
type(diccionario_ing_esp)

#Agregar elemento a diccionario
diccionario_ing_esp["azul"]="blue"

print(diccionario_ing_esp)

#Actualizar dato de diccionario UPDATE
diccionario_ing_esp.update({"negro":"black"})

#agregar lista dentro de un diccionario
diccionario_ing_esp.update({"gris":"grey","pronombres":["he","she","it"]})
print(diccionario_ing_esp)

#Borrar datos del diccionario => pop
diccionario_ing_esp.pop("gris")

#para eliminar del diccionario uso => del
del diccionario_ing_esp ["pronombres"]

#---------------------------------- OPERADORES LOGICOS -------------------------------------------------------------

#OPERADORES LOGICOS - Se usan para comprobar condiciones y devolver True o False, dependiendo de cual sea el caso 

#El primero es AND

print("Operador AND (que significa y)")
print("Para que sea verdadero todas las condiciones deben ser verdaderas")
5>3 and 5<10

5<3 and 5<10

#Para usar o, se usa la palabra reservada OR, que en or por lo menos 1na de las condiciones debe ser verdadera
5<3 or 5<10

#operador logico NOT
print("operador NOT (negacion logica)")
print(not 5>3)

#----------------------------------- OPERACIONES MATEMATICAS --------------------------------------

#suma, se representa con el simbolo + y me sirve tambien para concatenar
print(6+5)

#Resta de representa con el -
print(6-5)

#Multiplicacion, se representa con el asterisco *
print(7*8)

#Divicion, uso el / y me da resultado con decimales
print(37/3)

#Potenciación se usa el doble asterisco **, primero la base y luego el exponente
print(5**5)

#Modulo.. con el simbolo %
print(23%4)

#----------------------------------- OPERADORES DE COMPARACION --------------------------------------
#Para comparar si dos valores son iguales
print((3+29)==21)

#diferente de: !=
print((3+29)!=21)

#mayor que 
print((3+29)>21)

#menor que 
print((3+29)<21)

#menor o mayor igual que 
print((3+29)<=21)

#----------------------------------- CONDICIONALES --------------------------------------

#Me permite ejecutar un bloque de codigo si la condicion es verdadera o falta, las condicionales en python son IF,ELIF,ELSE

#if condición:
    #(codigo que quiero ejecutar)
#else:
    #(codigo a ejecutar)

edad_mafe=17
if edad_mafe >= 18:
    print("Bienvenido, pero no deberias estar aca")
else:
    print("Mafe por que estas aca???")

edad_usuario=int(input("Hola para ingresar por favor comprueba tu edad"))
if edad_usuario >= 18:
    print("Bienvenido, pero no deberias estar aca")
else:
    print("Mafe por que estas aca???")


edad_usuario=int(input("Hola para ingresar por favor comprueba tu edad"))
if edad_usuario >= 18:
    print("Bienvenido, pero no deberias estar aca")
elif edad_usuario >= 13:
    print("Eres un adolecente")
else:
    print("Mafe por que estas aca???")

if "Francia" in paises:
    print("Esta no es una lista latinoamericana")
else:
    print("Los sudacas")