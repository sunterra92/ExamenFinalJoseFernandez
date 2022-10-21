import random
def GenerateRandom():
    Lista10 = []
    for i in range(0,10):
        Lista10.append(random.randint(0, 15))

    return Lista10

def DeleteRepetiveValues(x):
    ListaNoRepetida = []
    for i in x:
        if i not in ListaNoRepetida:
            ListaNoRepetida.append(i)

    return ListaNoRepetida

def OrderList(x):
    x.sort()
    print('Lista Ordenada Asc          : ', x)
    x.reverse()
    print('Lista Ordenada Desc         : ', x)
    return x

def GetMaxValue(x):
    return x[0]

x = GenerateRandom()
print('Primera Lista Generada      : ', x)
x = DeleteRepetiveValues(x)
print('Segunda Lista Sin repetidos : ', x)
x = OrderList(x)
print('Valor mayor de la Lista:    : ', GetMaxValue(x))