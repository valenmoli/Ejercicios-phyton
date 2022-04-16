#Definir una función es_palindromo() que reconoce palíndromos
#(es decir, palabras que tienen el mismo aspecto escritas invertidas),
#ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(p):
    palin=''
    i=1
    while i <= len(p):
        palin+=p[len(p)-i]
        i+=1
    if palin==p:
        return True
    else:
        return False
    
def main():
    p=input('Ingrese palabra para ver si es palindromo: ')
    print(es_palindromo(p))
    
main()