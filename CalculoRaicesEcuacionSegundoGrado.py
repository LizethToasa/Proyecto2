## Ecuacion de segundo grado 
print ('Modelo de la ecuacion  a*x^2 + b*x + c = 0')
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))
#calcular el discrminante
disc = float(b**2-4*a*c)
if disc < 0:
    print('No hay solucion')
elif disc ==0:
    soluc == float(-b/2*a)
    print ('Solucion unica: ',soluc)
