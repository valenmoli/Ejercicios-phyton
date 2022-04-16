#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería
#devolver la cadena "odnaborp yotse"

def inversa(cadena):
    i=1
    inv=''
    while i <= len(cadena):
        inv+=cadena[len(cadena)-i]
        i+=1
        
    return inv
    
def main():
    cadena=input('Ingrese una cadena: ')
    print('La cadena inversa es: {}'.format(inversa(cadena)))
    
main()