#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    if n3>n2 and n3>n1:
        return n3
    if n2>n1 and n2>n3:
        return n2
    
    
def main():
    n1=float(input('Ingrese un numero: '))
    n2=float(input('Ingrese un numero: '))
    n3=float(input('Ingrese un numero: '))
    print(max_de_tres(n1,n2,n3))
    
main()
