def creartxt():
	archi=open('datos.txt','w')
	archi.close

def grabartxt():
        archi=open('datos.txt','a')
        archi.write('Este es el primer ejemplo de manejo de archivos\n')
        archi.write('Geovany')
        archi.write('Lizeth')
        archi.write('David')
        archi.close()

def leertxt():
    archi=open('datos.txt','r')
    linea=arch.readline()
    while linea!="":
        print (linea)
        linea=archi.readline()
        arch.close()

def leertxtenlista():
        archivo=open('datos.txt','r')
        lineas=archi.readlines()
        print lineas
archi.close()
        

