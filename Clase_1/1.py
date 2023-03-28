import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    args = parser.parse_args()
    
    if args.n > 0:
        odds = []
        for i in range(args.n):
            if i % 2 == 1:
                odds.append(i)

    else:
        print('n debe ser positivo.')

    print("Los números impares son: ", odds)

if __name__ == '__main__':
    main()
