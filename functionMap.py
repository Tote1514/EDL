def fmap(function, lista):
    for i in range(len(lista)):
        novo = function(lista[i])
        lista[i] = novo
        
def metade (x):
    return x / 2

def show(x):
    return str(x)

def multiplou(x):
    return x%4 == 0

lista1 = [ 10, 4, 8 , 12]
lista2 = [ 7, 10, 12, 16, 18, 20]

print("Lista 1 original:", lista1)

fmap(metade, lista1)
print("lista 1 com seus elementos divididos por 2:" ,lista1)

fmap(show, lista1)
print("Lista 1 com seus elementos convertidos para string:", lista1)

print("Lista 2 original:", lista2)

fmap(multiplou, lista2)
print("Lista 2 testando se seus elementos são multiplos de 4",lista2)
