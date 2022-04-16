#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def verif(l):
    
    if l =='a' or l =='e' or l =='i' or l =='o' or l =='u':
        return True
    else:
        return False
    
def main():
    l=input('Ingrese un caracter: ')
    print(verif(l))
    
main()