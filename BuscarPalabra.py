def creartxt():
    archi=open('TEXTO.txt','w')
    archi.close()
    
pal=str(input('Ingrese la palabara a buscar: ',pal)

def leertxt():
    archi=open('TEXTO.txt','r')
    linea=archi.readline()
        
    while linea!="":
        cadena=linea
        cadena.find(pal)
        
        linea=archi.readline()
        archi.close()
