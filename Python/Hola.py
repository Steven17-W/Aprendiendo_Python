print ("Hola mundo")


nombre = "Steven"
Edad = 24

#/////////////  Ciclo FOR /////////////////////
for i in range(0, 11):
    print(i)

#/////////// Numero mayor - entre dos numeros con If ////////////////
num1 = float (input(" Ingrese el primer numero"))
num2 = float (input(" Ingrese el segundo numero"))

if num1 > num2:
    print("El numero {num1} es mayor que el {num2}.")
elif num2 > num1:
    print("El numero {num2} es mayor que el {num1}.")
else: 
    print("Ambos numeros son iguales")
