import ply.lex
from lexer import lexer

def read_file(filename: str) -> str:
    with codecs.open(filename, 'r', encoding='utf-8') as INFILE:
        return INFILE.read()


def tokenize_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        lexer.input(data)
        while True:
            token = lexer.token()
            if token is None:
                break
            print(token)

if __name__ == '__main__':
    import argparse, codecs

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--who', action='store_true', help='who wrote this')
    group.add_argument('-f', '--file', help='filename to process')

    ns = parser.parse_args()
    if ns.who:
        # identify who wrote this
        print('152103143 Minh Hoang')
    elif ns.file is None:
        # user didn't provide input filename
        parser.print_help()
    else:
        tokenize_file(filename=ns.file)