import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str)
    parser.add_argument('-n', type=int)
    args = parser.parse_args()
    print((args.s + " ") * args.n)

if __name__ == '__main__':
    main()
