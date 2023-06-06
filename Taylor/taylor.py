import threading
import math

def calcular_termino(n, x):
    termino = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return termino

def calcular_suma_terminos(n, x, resultados, lock):
    termino = calcular_termino(n, x)
    lock.acquire()
    resultados.append(termino)
    lock.release()

def calcular_suma_total(resultados, lock, suma_total):
    for termino in resultados:
        lock.acquire()
        suma_total[0] += termino
        lock.release()

def main():
    x = float(input("Ingrese el valor de x: "))
    num_terminos = int(input("Ingrese la cantidad de términos a calcular: "))
    referencia = float(input("Ingrese el valor de referencia: "))

    resultados = []
    lock = threading.Lock()
    suma_total = [0]

    hilos_terminos = []
    hilos_suma = []

    # Crea los hilos para calcular los términos
    for n in range(num_terminos):
        hilo_termino = threading.Thread(target=calcular_suma_terminos, args=(n, x, resultados, lock))
        hilos_terminos.append(hilo_termino)
        hilo_termino.start()

    # Crea el hilo para sumar los términos
    hilo_suma = threading.Thread(target=calcular_suma_total, args=(resultados, lock, suma_total))
    hilo_suma.start()

    # Espera a que todos los hilos terminen
    for hilo in hilos_terminos:
        hilo.join()
    hilo_suma.join()

    # Calcula la diferencia con el valor de referencia
    diferencia = suma_total[0] - referencia

    # Imprime los resultados
    print("Suma total de los términos calculados:", suma_total[0])
    print("Diferencia con el valor de referencia:", diferencia)

if __name__ == "__main__":
    main()

