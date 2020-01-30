import math
import numpy as np
import matplotlib.pyplot as plt
import calculadoraC as C


def funcion_f(z,c):
    return C.suma(C.producto(z,z),c) 

def esta_en_mandelbrot(c):
    z = [0,0]
    cont = 0
    
    for i in range(30):
        cont += 1
        z = funcion_f(z,c)

        if C.modulo(z)[0]>2:
            return False, cont

    return True, 0

def main():
    
    plano = np.zeros((400,700))

    for parte_real in range(700):
        for parte_imaginaria in range(400):

            c = [parte_real/200-2.5, parte_imaginaria/200-1]
            pertenece, color = esta_en_mandelbrot(c)
            
            if pertenece == True:
                plano[parte_imaginaria][parte_real] = color
            else:
                plano[parte_imaginaria][parte_real] = color

    plt.figure(figsize = (10,10))
    plt.imshow(plano, 'twilight_shifted')
    plt.show()
    
main()
