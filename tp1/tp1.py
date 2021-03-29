#!/usr/bin/python3

import sys
import argparse
import timeit

START_TIME = timeit.default_timer()

DFA = {
    0:{'5':1},
    1:{'7':2, '8':3},
    2:{'p':4},
    3:{'a':4},
    4:{'8':3, '7':5},
    5:{'p':4}
}

class BColors:
    HEADER  = '\033[95m'
    OKBLUE  = '\033[94m'
    OKCYAN  = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    ENDC    = '\033[0m'
    BOLD    = '\033[1m'
    UNDERLINE = '\033[4m'

def str_read(s,output=None):
    initial = 0
    accepting = {5}
    indefinition = False
    path = ''

    state = initial
    for index,c in enumerate(s):
        path += '{}({})\u2192'.format(str(state),c)
        try:
            state = DFA[state][c]
            q = state
        except KeyError:
            cursor = s[:index] + '[' + c +']' + s[index+1:]
            indefinition = True
            state = False
            break

    not_final = q not in accepting

    if indefinition:
        path += 'I'
        result = '-I : {}'.format(cursor)
    elif not_final:
        path += '{}'.format(q)
        result = '-{} : {}'.format(q,s)
    else:
        path += 'F'
        result = '+A : {}'.format(s)

    if indefinition or not_final:
        print(BColors.FAIL + result + BColors.ENDC)
    else:
        print(BColors.OKGREEN + result + BColors.ENDC)

    if output:
        output.write(result + '\n')

    return path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UFSJ/T.Linguagens TP1')
    parser.add_argument('-s','--str', help='string de entrada')
    parser.add_argument('-f','--file',
        type=argparse.FileType('r', encoding='UTF-8'),
        help='arquivo de entrada')
    parser.add_argument('-o','--out',
        type=argparse.FileType('w', encoding='UTF-8'),
        help='arquivo de saida')
    parser.add_argument('-l','--legend',
        action="store_true",
        help='mostrar legenda')
    args = parser.parse_args()

    if not (args.str or args.file or args.out):
        parser.print_help()
        sys.exit(1)
    elif not (args.str or args.file) and args.out:
        parser.error('Nenhuma entrada estipulada')
        sys.exit(1)

    print('ER = 5(7p+8a)\u207A7')

    if args.file:
        strings = args.file.read().splitlines()
        for s in strings:
            str_read(s,args.out) if args.out else str_read(s)
        args.file.close()

    if args.str:
        path = str_read(args.str,args.out) if args.out else str_read(args.str)
        print(path)

    if args.out:
        args.out.close()

    if args.legend:
        stop_time = timeit.default_timer()
        execution_time = round(stop_time - START_TIME,4)
        print('+A : Aceito')
        print('-I : Rejeitado (Indefinido)')
        print('-# : Rejeitado (Estado nao final)')
        print(' t : {}s'.format(execution_time))

    sys.exit(0)