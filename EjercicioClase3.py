nro1 = int (input("Ingrese el primer numero: "))
nro2 = int (input("Ingrese el segundo numero: "))
opcion = int (input("Ingrese el numero 1 para sumar o el numero 2 para restar: "))

def sumar(num1,num2):
    suma = num1 + num2
    return suma 

def restar(num1,num2):
    resta = num1 - num2
    return resta 

if opcion == 1:
    resultado_suma = sumar(nro1,nro2)
    print (f'La suma entre {nro1} y {nro2} es: {resultado_suma}')
elif opcion == 2:
    resultado_resta = restar(nro1,nro2)
    print (f'La resta entre {nro1} y {nro2} es: {resultado_resta}')
else:
    print ("Numero incorrecto")