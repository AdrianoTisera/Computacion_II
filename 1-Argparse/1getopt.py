import getopt
import sys

class NotValidNumberError(Exception):
    pass

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["number="])
    except getopt.GetoptError:
        print('Uso: 1getopt.py -n <numero>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-n", "--number"):
            try:
                n = int(arg)
            except ValueError:
                print("El número ingresado no es válido.")
                sys.exit(2)

    if n > 0:
        odds = [i for i in range(n) if i % 2 == 1]
    else:
        raise NotValidNumberError("El número debe ser mayor a 0.")

    print("Los números impares son: ", odds)

if __name__ == '__main__':
    main(sys.argv[1:])

