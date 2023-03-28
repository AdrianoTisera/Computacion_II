import argparse
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=argparse.FileType('r'))
    parser.add_argument('-p', action='store_true')
    args = parser.parse_args()

    try:
        file_content = args.f.readlines()
        lines, words, chars = count(file_content)
        print("El archivo tiene ", lines, " líneas y ", words, " palabras.")

        if args.p:
            print("El promedio de longitud de las palabras es ", str("{:.2f}".format(average_word_length(file_content))) + ".")

    except Exception as e:
        with open('error.log', 'w') as f:
            f.write(str(e))
        print("Error: ", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
