import calculadoraC as c

def test_suma():
    assert c.suma([-3,2],[4,1])==[1,3], 'Debe ser 1+3i'
    
def test_resta():
    assert c.resta([5,2],[7,1])==[-2,1], 'Debe ser -2-1i'
    
def test_producto():
    assert c.producto([-7,3],[-2,3]) == [5,-27], 'Debe ser 5-27i'
    
def test_division():
    assert c.division([-3,-2],[5,4]) == [-0.5609756097560976,0.04878048780487805], 'Debe ser 7/41 -22/41 i'
    
def test_conjugado():
    assert c.conjugado([-3,7]) == [-3,-7], 'Debe ser -3-7i'
    
def test_modulo():
    assert c.modulo([-3,7]) == [(58)**(1/2)], 'Debe ser (58)^(1/2) '
    

if __name__== "__main__":
    
    test_suma()
    test_resta()
    test_producto()
    test_conjugado()
    test_modulo()
    
    print('prueba exitosa')
