import argparse
import math
import os
import sys

parser = argparse.ArgumentParser(description='Calcula la raíz cuadrada positiva y negativa de un número mayor o igual a cero utilizando fork.')
parser.add_argument('numero', type=float, help='El número del que se calculará la raíz cuadrada.')
parser.add_argument('-f', action='store_true', help='Realiza un fork para calcular la raíz negativa en un proceso hijo.')
args = parser.parse_args()

if args.numero < 0:
    sys.stdout.write('Error: el número debe ser mayor o igual a cero.\n')
    sys.exit(1)

if args.numero == 0:
    sys.stdout.write('La raíz cuadrada de 0 es 0.\n')
    sys.exit(0)

raiz_positiva = math.sqrt(args.numero)
sys.stdout.write(f'La raíz cuadrada positiva de {args.numero} es {raiz_positiva}.\n')

if args.f:
    pid = os.fork()
    if pid == 0:
        # Proceso hijo
        raiz_negativa = -math.sqrt(args.numero)
        sys.stdout.write(f'La raíz cuadrada negativa de {args.numero} es {raiz_negativa}.\n')
    else:
        # Proceso padre
        os.wait()

