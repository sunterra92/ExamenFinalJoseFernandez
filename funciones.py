import random
import math


def GenerateLista():
    file = open("tabla.txt", "w")
    totalItem = int(input('Ingrese tamaño de Lista: '))
    for i in range(0, totalItem):
        file.writelines("{}\n".format(random.randint(0, 20)))
    file.close()
    return None

def GenerateRaizCuadrada():
    file_notas = open("notas.txt", "w")
    file = open("tabla.txt", "r")

    for newLine in file:
        newLine = int(newLine)
        file_notas.writelines("Raiz Cuadrada de {} --> {}\n".format(newLine, math.sqrt(newLine)))

    file_notas.close()
    file.close()
    return None