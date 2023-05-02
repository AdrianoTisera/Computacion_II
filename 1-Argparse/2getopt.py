import getopt
import sys

def main(argv):
    s = ""
    n = 1

    try:
        opts, args = getopt.getopt(argv, "s:n:", ["string=", "number="])
    except getopt.GetoptError:
        print('Uso: 2getopt.py -s <cadena> -n <numero>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--string"):
            s = arg
        elif opt in ("-n", "--number"):
            try:
                n = int(arg)
            except ValueError:
                print("El número ingresado no es válido.")
                sys.exit(2)

    print((s + " ") * n)

if __name__ == '__main__':
    main(sys.argv[1:])

