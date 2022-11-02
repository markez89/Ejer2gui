from functools import reduce
from random import randrange

#Ejercicios.

'''
1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
'''

def max(a, b):
    return a if a > b else b

#print(max(4,7))

'''
 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
'''

def max_de_tres(numeros):
    mayor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero

    return mayor

#print(max_de_tres([2,5,7,1,9,3]))

resultadoMaximo = reduce(lambda x, y: x if x > y else y, [2,5,7,1,9,3])
resultadoMinimo = reduce(lambda x, y: x if x < y else y, [2,5,7,1,9,3])

#print(resultadoMaximo)
#print(resultadoMinimo)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(reduce(lambda x,y : x+y, matrix ))

'''
3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

'''

def calculaLongitud(cadena):
    
    longitud = 0
    for c in cadena:
        longitud += 1
    
    return longitud


#print(calculaLongitud(["hola", "adios"]))

'''
 4-Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
'''

def compruebaCaracter(x):
    return True if x in 'aeiou' else False


#print(compruebaCaracter('a'))

'''
5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
'''

def sum(a ,b ):
    return a + b

def multip(a ,b ):
    return a * b

resultadoSuma = reduce(sum, [1,2,3,4])
resultadoMulti = reduce(multip, [1,2,3,4] )
#print(resultadoSuma)
#print(resultadoMulti)


'''
6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
'''

def devuelveInversa(cadena):
    cadena_inversa = ""
    for c in cadena:
        cadena_inversa = c + cadena_inversa
    return cadena_inversa        

#print(devuelveInversa("estoy probando"))       


'''
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
'''

def es_palindromo(cadena):
    cadena_alreves = cadena[::-1]
    return True if cadena == cadena_alreves else False

#print(es_palindromo("saravaras"))

'''
8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
'''

def devuelveComun(lista1, lista2): 
    estado = False

    for valor in lista1:
        if valor in lista2:
            estado = True

    return estado

#print(devuelveComun([1,2,3,4,5], [6,7,8,9,10]))


'''
9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
'''

def generar_n_caracteres(valor, caracter):
    return caracter * valor


#print(generar_n_caracteres(5,'-'))

'''
10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
'''

def procedimiento(datos):
    for valor in datos:
        print('*' * valor)

#procedimiento([4,9,7])


'''
Ejercicios en python
1) Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
'''

cantidad_compras = 0

colores_bolsa = ['BOLA BLANCA', 'BOLA ROJA', 'BOLA AZUL', 'BOLA VERDE', 'BOLA AMARILLA']
descuentos = [0,10,20,25,50]

while(cantidad_compras < 100):
    cantidad_compras = int(input("Introduzca la cantidad total de compras:"))
    if(cantidad_compras < 100):
        print("El cliente no aplica a la promoción")

print('\nSU GASTO ES IGUAL O SUPERIOR A 100$ Y POR TANTO PARTICIPA EN LA PROMOCIÓN\n')
    
print("    " +"COLOR" + "\t" + "DESCUENTO\n")

for index, color in enumerate(colores_bolsa):
    print(color + '\t' + str(descuentos[index]) + ' POR CIENTO') 
  

random = randrange(5)

print("\nALEATORIAMENTE USTED OBTUVO UNA "+ colores_bolsa[random] +  "\n")

match random:
    case 0:
        print('LO SENTIMOS, PERO USTED NO TIENE DESCUENTO')        
    case 1:
        print('FELICIDADES SU DESCUENTA ES DEL ' + str(descuentos[random]) +  ' POR CIENTO\n')        
    case 2:
        print('FELICIDADES SU DESCUENTA ES DEL ' + str(descuentos[random]) + ' POR CIENTO\n')       
    case 3:
        print('FELICIDADES SU DESCUENTA ES DEL ' + str(descuentos[random]) + ' POR CIENTO\n')        
    case 4:
        print('FELICIDADES SU DESCUENTA ES DEL ' + str(descuentos[random]) + ' POR CIENTO\n')


descuento = cantidad_compras * descuentos[random] / 100

print('TOTAL A PAGAR APLICANDO EL DESCUENTA ES: ' + str(cantidad_compras-descuento) + '€')
        

    
    
    

    

    



