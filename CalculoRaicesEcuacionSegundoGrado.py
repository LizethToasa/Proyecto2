## Ecuacion de segundo grado 
print ('Modelo de la ecuacion  a*x^2 + b*x + c = 0')

def creartxt():
	archi=open('Ecuacion cuadratica.txt','w')
	archi.close

def grabartxt():
    a = float(input('Valor de a: '))
    b = float(input('Valor de b: '))
    c = float(input('Valor de c: '))
    disc = float(b**2-4*a*c)
    if disc < 0:
        print('No hay solucion')
    elif disc ==0:
        soluc == float(-b/2*a)
        print ('Solucion unica: ',soluc)
    else:
        x1 = float((-b+((b**2 - 4*a*c))**0.5)/(2*a))
        x2 = float((-b-((b**2 - 4*a*c))**0.5)/(2*a))
        print('Los valores de las raices son:')
        print('X1: ',x1)
        print('X2: ',x2)
        archi=open('Ecuacion cuadratica.txt','a')
        archi.write('Los valores de las raices son:')
        archi.write('\nX1:'+str(x1))
        archi.write('\nX2:'+str(x2))
        archi.close()

creartxt()
grabartxt()

