
def pnc(n):
        
        if n > 0: print("El número es positivo")

        if n < 0: print("El número es negativo")

        if n == 0: print("El número es cero")
        
def p_i():

        n = int(input("Digite nuevamente un número: "))

        if n %2 == 0: print("El número es par")

        else: print("El número es impar")

def fibo():

    n= int(input("Digite nuevamente el número: "))

    num1 = 0

    num2 = 1

    while num2 < n:

        sec = num1 + num2

        num1 = num2

        num2 = sec
        
    if num2 == n or n== 0: print("El número es parte de la serie fibonacci")

    else: print("No hace parte de la serie fibonacci")
        
def primo():

    n = int(input("Digite nuevamente el número: "))

    esprimo = True
    
    for rep in range(2, n):

        if n % rep == 0:

            esprimo = False

            break
    if esprimo and n > 1: print("Es primo")

    else: print("No es primo") 

def  sumarinter():

    n1 = int(input("Digite un número: "))
    n2 = int(input("Digite nuevament el número: "))

    inicio = min(n1, n2)
    fin = max(n1, n2)
    
    suma = sum(range(inicio + 1, fin))
    
    print("La suma de los intermedios es:", suma)

def imparelev():

    n = int(input("Digite nuevamente un número: "))
    if n % 2 == 0: resultado = numero ** 3
    else: resultado = n** 2
        
    print("El resultado del nuemro",n,"elevado al cuadro es ",resultado)
        
def main(): 
    n = int(input("Digite un número: "))

    pnc(n)

    p_i()

    fibo()

    primo()

    sumarinter()

    imparelev()
    

    
main()
