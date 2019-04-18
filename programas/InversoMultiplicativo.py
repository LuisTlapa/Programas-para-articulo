import random, sys, os, time
def MCD(a, b):
    # Devuelve su MCD  de a y b usando el algoritmo de Euclides extendido
    while a != 0:
        (a, b) =(b % a, a)
    #print(b)
    return b

def Inverso(a, m):
    # Devuelve el inverso modular de a% m, que es
    # el número x tal que a * x% m = 1
    
    if MCD(a, m) != 1:
        print("No son primos relativos")
        return None #si a y m no son primos

    # Calcular utilizando el algoritmo euclidiano extendido:
    
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    
    while v3 != 0:
        D = u3 // v3 # // es el operador de división entera
        v1,u1=(u1 - D * v1),v1
        v2,u2=(u2 - D * v2),v2
        v3,u3=(u3 - D * v3),v3
        
    t=u1%m
    print("\n El inverso multiplicativo de e es: \n",t)
    print("digitos: ",len(str(t)))

if __name__ == '__main__':
    x =int(input("\n Ingresa el número  e para generar su inversa: \n"))
    n =int(input("\n Ingresa un número para el modulo (n): \n "))
    inicio_de_tiempo = time.time()
    Inverso(x,n)
    tiempo_final = time.time()
    tiempo_transcurrido = tiempo_final  - inicio_de_tiempo
    print ("\n Tomó %d segundos." % (tiempo_transcurrido))