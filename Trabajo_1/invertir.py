import argparse
import os
import multiprocessing


def process_line(line, conn):
    # Invierte el orden de los caracteres de la línea y envía el resultado al proceso padre a través del pipe.
    inverted_line = line[::-1]
    conn.send(inverted_line)
    conn.close()


def main():
    # Configura la entrada de argumentos
    parser = argparse.ArgumentParser(description='Invierte cada línea de un archivo de texto')
    parser.add_argument('-f', '--file', type=str, required=True, help='Ruta del archivo de texto')
    args = parser.parse_args()

    # Lee el archivo y obtiene las líneas
    with open(args.file, 'r') as f:
        lines = f.readlines()

    # Crea un proceso para cada línea y envía la línea a través de un pipe.
    # Cada proceso invertirá la línea y enviará el resultado al proceso padre a través de un nuevo pipe.
    processes = []
    for line in lines:
        parent_conn, child_conn = multiprocessing.Pipe()
        process = multiprocessing.Process(target=process_line, args=(line.strip(), child_conn))
        processes.append((process, parent_conn))
        process.start()

    # Espera a que todos los procesos terminen y recupera los resultados.
    inverted_lines = []
    for process, parent_conn in processes:
        process.join()
        inverted_lines.append(parent_conn.recv())

    # Imprime los resultados invertidos.
    for line in inverted_lines:
        print(line)


if __name__ == '__main__':
    main()

