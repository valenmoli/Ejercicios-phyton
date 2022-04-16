# Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len()
#incorporada,pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def contar(lst):
    cont=0
    for i in lst:
        cont+=1
        
    return cont
        
def main():
    lst=[0,1,5,4,2,3,3]
    print('La lista tiene un largo de: {}'.format(contar(lst)))

main()