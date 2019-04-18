from time import time
from math import floor, ceil, sqrt
from fractions import gcd
import random, time,  sys, os
import math, time
import pandas as pd
import numpy as np

def esPrimoDiv(num):
    # Devuelve True si num es un número primo; de lo contrario, es False.
    # Utiliza el algoritmo de división de prueba para probar la primalidad.
    # Todos los números menores que 2 no son primos:
    if num < 2:
        return False
    # Verifica si num es divisible por cualquier número hasta la raíz cuadrada de num:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        return True
    
def primerTamiz(tamizTamaño):
    # Devuelve una lista de números primos calculados usando el algoritmo del Tamiz de Eratóstenes.
    tamiz = [True] * tamizTamaño
    tamiz[0] = False # Cero y uno no son numeros primos.
    tamiz[1] = False
    
    # Crea el tamiz:
    for i in range(2, int(math.sqrt(tamizTamaño)) + 1):
        apuntador = i * 2
        while apuntador < tamizTamaño:
            tamiz[apuntador] = False
            apuntador += i
            
    # Compilar la lista de primos:
    primes = []
    for i in range(tamizTamaño):
        if tamiz[i] == True:
            primes.append(i)
    return primes
    
def rabinMiller(num):
    # Devuelve verdadero si num es un número primo.
    if num % 2 == 0 or num < 2:
        return False # Rabin-Miller no funciona en enteros pares.
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # Siga dividiendo a la mitad s hasta que sea impar (y use t para contar cuántas veces hemos reducido a la mitad s):
        s = s // 2
        t += 1
        
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # Esta prueba no se aplica si v es 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

# La mayoría de las veces podemos determinar rápidamente si num no es primo
# dividiendo por las primeras docenas de números primos. Esto es más rápido
# que RabinMiller () pero no detecta todos los compuestos.

PRIMOS_BAJOS = primerTamiz(100)
def esPrimo(num):
    # Devuelve True si num es un número primo. Esta función lo hace más rápido
    # verificación del número primo antes de llamar a RabinMiller
    if (num < 2):
        
     #   return False
    # 0, 1 y los números negativos no son primos.
    # Ver si alguno de los números primos bajos puede dividir num:
        for primo in PRIMOS_BAJOS:
            if (num % primo == 0):
                return False
    # Si todo lo demás falla, llame a rabinMiller () para determinar si num es primo:
    return rabinMiller(num)

def generarPrimoLargo(tamañoClave=1024):
    # Devuelve un número primo aleatorio que tiene bits de tamaño de clave en tamaño:
    while True:
        num = random.randrange(2**(tamañoClave-1), 2**(tamañoClave))
        if esPrimo(num):
            return num
        
def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b
        

def f(x):
	""" función para rho de pollard """
	return x**2 + 1


def factorRho(n,x_1):
	""" Factor utilizando el método rho de pollard. """
	x = x_1;
	xp = f(x) % n
	p = gcd(x - xp,n)

	#print ("x_i's: {")
	while p == 1:
		#print (x),
		# en la iteración x = x_i y x' = x_2i
		x = f(x) % n
		xp = f(xp) % n
		xp = f(xp) % n
		p = gcd(x-xp,n)

	#print ("}")

	if p == n: return -1
	else: return p


def testFactorRho(n):
    

    x_1 = 2

    #print ("n= %i, x_1= %i" % (n,x_1))
    
    p = factorRho(n,x_1)
    return p

if __name__ == '__main__':
    #while True:
    #entrada = input("\n Decea generar un número n y factorizarlo: ")
    numeros = int(input("\n Cuantos números desea generar: "))
    Tabla = np.zeros((numeros,5))
    numeros*=2
    #if entrada =="Si":
    T=0
    for tamañoBits in range (4,numeros+4,2):
        #tamañoBits = 0
        #for tamañoBits in range (4,numeros+4):
        #tamañoBits = int(input("Ingrese el tamaño de los números en bits: "))#Tamañoo de claves en bits
        #print(tamañoBits)
        p = 0 #Variable
        q = 0 #Variable
        #print ('\n Generando p & q primos...')
        while p == q:
            p = generarPrimoLargo(tamañoBits)
            #print("p = ", p)
            q = generarPrimoLargo(tamañoBits)
            #print("q = ", q)
        #Calcular n = p*q
        n = p * q
        #print("n = ", n)
        #print("Número de digitos de n: ",len(str(n)))
        inicio_de_tiempo = time.time()
        #print ('\n factorizando ', n)
        testFactorRho(n)
        #print("p: ",p)
        q=n/p
        #print(q)
        tiempo_final = time.time()
        tiempo_transcurrido = tiempo_final  - inicio_de_tiempo
        #print ("Tomó %d segundos." % (tiempo_transcurrido))
        tam=len(str(n))
        v=[]
        v=[int(n),tam,p,q,tiempo_transcurrido]
        #print(T,".-",v)
        #print(T)
        tamañoBits+= 2
        v= np.asarray(v)
        Tabla[T]=v
        T=T+1
    labels=['número','digitos','  p  ','  q  ','tiempo']
    df = pd.DataFrame(Tabla, columns=labels)

df