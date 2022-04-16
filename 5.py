#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def suma(lst):
    sumatoria=0
    for i in lst:
        sumatoria+=i
    return sumatoria

def multip(lst):
    multiplicacion=0
    for i in lst:
        if multiplicacion==0:
            multiplicacion+=i
        else:    
            multiplicacion*=i
    return multiplicacion
    
def main():
    lst=[1,2,3,4]
    print(suma(lst))
    print(multip(lst))
main()