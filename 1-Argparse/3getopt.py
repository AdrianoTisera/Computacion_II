import getopt
import sys

def count(file):
    lines = 0
    words = 0
    chars = 0

    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)

    return lines, words, chars

def average_word_length(file):
    lines, words, chars = count(file)
    return (chars / words)

def main(argv):
    file_path = ""
    print_average_word_length = False

    try:
        opts, args = getopt.getopt(argv, "f:p")
    except getopt.GetoptError:
        print('Uso: 3getopt.py -f <archivo> [-p]')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-f":
            file_path = arg
        elif opt == "-p":
            print_average_word_length = True

    try:
        with open(file_path, "r") as file:
            file_content = file.readlines()
            lines, words, chars = count(file_content)
            print("El archivo tiene ", lines, " líneas y ", words, " palabras.")

            if print_average_word_length:
                print("El promedio de longitud de las palabras es ", str("{:.2f}".format(average_word_length(file_content))) + ".")

    except FileNotFoundError:
        with open("errors.log", "a") as error_file:
            error_file.write("No se encontró el archivo especificado.")
        sys.stderr.write("No se encontró el archivo especificado.")
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])

