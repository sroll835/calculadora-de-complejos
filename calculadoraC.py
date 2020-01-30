import math

""" Libreria que realiza operaciones entre numeros complejos.

    La libreria soporta por lo menos las siguientes operaciones:
    
        1. Suma
        2. Producto
        3. Resta
        4. Division
        5. Modulo
        6. Conjugado
        7. Conversion entre representacion polar
        8. Retornar la fase de un número complejo
        9. Imprimir de forma a+bi - Forma complejo
        10. [a,b], n entrada y retorna (a+bi)^n
"""

def suma(a,b):
    
    """ Esta funcion retorna la suma de dos numeros complejos """
    
    suma = []
    suma.append((a[0]+b[0]))
    suma.append((a[1]+b[1]))
    return suma
    
    
def producto(a,b):

    """ Esta funcion retorna el producto de dos numeros complejos """

    producto = []
    producto.append((a[0]*b[0]-a[1]*b[1]))
    producto.append((a[0]*b[1]+a[1]*b[0]))
    return producto

def resta(a,b):

    """ Esta funcion retorna la resta de dos numeros complejos """

    resta = []
    resta.append((a[0]-b[0]))
    resta.append((a[1]-b[1]))
    return resta

def division(a,b):

    """ Esta funcion retorna la division de dos numeros complejos """

    division = []
    division.append(((a[0]*b[0]+a[1]*b[1])/(b[0]*b[0]+b[1]*b[1])))
    division.append(((a[1]*b[0]-a[0]*b[1])/(b[0]*b[0]+b[1]*b[1])))
    return division

def modulo(a):

    """ Esta funcion retorna el modulo de un numero complejo """

    modulo = []
    modulo.append(math.sqrt(a[0]**2+a[1]**2))
    return modulo

def conjugado(a):

    """ Esta funcion retorna el conjugado de un numero complejo """

    conjugado = []
    conjugado.append(a[0])
    conjugado.append(-1*a[1])
    return conjugado

def complejoAPolar(a):

    """ Esta funcion convierte un numero complejo a polar """

    aPolar = []
    aPolar.append(modulo(a))
    aPolar.append(math.atan(a[1]/a[0]))
    return aPolar

def polarAComplejo(c):

    """Esta funcion convierte un numero polar a complejo """

    complejo = []
    a = c[0]*math.cos(math.radians(c[1]))
    b = c[0]*math.sin(math.radians(c[1]))
    complejo.append(round(a,2))
    complejo.append(round(b,2))
    return complejo
    

def fase(a):

    """ Esta funcion calcula la fase de un numero complejo """

    fase = []
    fase.append(math.atan((a[1]/a[0]))*(180/math.pi))
    return fase

def imprimir(c):

    """ Esta funcion imprime un numero complejo de la forma a+bi """

    print("El numero es:",str(c[0]),"+",str(c[1])+"i")

def potencia(c,n):
    
    """ Esta funcion calcula c**n, siendo c un numero complejo """
    potencia = []
    polar = complejoAPolar(c)
    complejo = polarAComplejo([round(polar[0]**n,2),round(polar[1]*n,2)])
    return complejo

    



    
    
    
