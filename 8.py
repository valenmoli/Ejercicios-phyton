#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o
#devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(l_1,l_2):
    retorno=''
    for i in l_1:
        for j in l_2:
            if j==i:
                retorno= True
    if retorno != True:
        return False
def main():
    l_1=[]
    l_2=[]
    i=1
    while i !='0':
        i=input(('Ingrese "1" para agregar valores a la lista 1\nIngrese "2" para agregar valores a la lista 2\nIngrese 0 para terminar de agregar numeros a listas: '))
        j=1
        k=1
        if i=='1':
            while j!='0':
                j=input()
                l_1.append(j)
        if i=='2':
            while k!='0':
                k=input()
                l_1.append(k)        
    print('\nLa funcion retorna: {}'.format(superposicion(l_1,l_2)))
main()