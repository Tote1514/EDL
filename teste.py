def ffilter (funcao, lista):
    lista_nova = []
    if len(lista) == 0:
        return []
    else:
        if funcao(lista[0]):
            lista_nova += lista[:1]
    return lista_nova + ffilter(funcao, lista[1:])

def maior (x):
    return x > 2
def menor (x):
    return x <= 2

lista1 = [1,2,3,4,5]
lista2 = []
lista2 = ffilter(maior,lista1)
lista3 = ffilter(menor,lista1)
print("Teste da função ffilter")
print("Lista original:",lista1)
print("Lista 2 com os elementos maiores do que 2:", lista2)
print("Lista 3 com os elementos menores ou iguais a 2:", lista3)
