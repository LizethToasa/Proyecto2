def creartxt():
	archi=open('Texto.txt','w')
	archi.close

def grabartxt():
        archi=open('TEXTO.txt','a')
        archi.write('Poquito a poco te llevo al cielo amor poquito a poco yo te inundare de amor poquito a poco te llevo al cielo amor oh yo te inundare de amor')
        archi.close()

creartxt()
grabartxt()

palabra = raw_input("palabra a buscar ?? ")

repetidas = 0 
f = open('TEXTO.txt','r')
lines = f.readlines()
for line in lines:
    palabras = line.split(' ')
    for p in palabras:
        if p==palabra:
            repetidas = repetidas+1

print "la palabra "+str(palabra)+" se repite "+str(repetidas)+" veces"

f.close()
