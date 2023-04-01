#EXERCICIO 1
def maximo(*valor:int):
    n1 = valor[0]
    n2 = valor[1]

    valor = n2 
    if(n1 > n2):
       valor = n1   

    return valor

#DETECTAR QUAL NUMERO É MAIOR, EXEMPLO(10 e 15)
print("O numero maior é:", maximo(10, 15))


#EXERCICIO 2
def mult(*valor:int):
    n1 = valor[0]
    n2 = valor[1]

    n3 = False
    if  n1 % n2 == 0:
        n3 = True  

    return n3
#DETECTAR SE O NUMERO É MULTIPLO, EXEMPLO(35 e 7)
print(mult(35,7))


#EXERCICIO 3
def quad(n1:int):
    area = n1*n1
    return area
#DETECTAR A AREA DE UM QUADRADO, EXEMPLO (3.25)
print(f'{quad(3.25):.2f}')
