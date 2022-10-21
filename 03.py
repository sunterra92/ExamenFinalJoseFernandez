import random
import time


def MedirTiempo(funcionB):
    inicio = time.time()
    def funcionC(*args, **kwargs):
        #print("\nLa cantidad de argumentos que tiene la función es")
        resultado = funcionB(*args, **kwargs)
        time.sleep(random.randint(1,2))
        print(resultado)
        print('Tiempo de Ejecución : ', time.time())
        #print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return funcionC


@MedirTiempo
def Division2Numeros(a, b):
    return a/b

Division2Numeros(100, 10)
Division2Numeros(81, 9)
Division2Numeros(36, 6)
