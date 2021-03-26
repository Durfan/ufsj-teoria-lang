#!/usr/bin/python3

import argparse
import sys, timeit

start_time = timeit.default_timer()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

dfa = {
    0:{'5':1},
    1:{'7':2, '8':3},
    2:{'p':4},
    3:{'a':4},
    4:{'8':3, '7':5},
    5:{'p':4}
}

def sread(s,out=None):
    initial = 0
    accepting = {5}
    indefinition = False

    state = initial
    for index,c in enumerate(s):
        try:
            state = dfa[state][c]
            q = state
        except KeyError:
            cursor = s[:index] + '[' + c +']' + s[index+1:]
            indefinition = True
            state = False
            break

    if indefinition:
        result = '-I : {}'.format(cursor)
        print(bcolors.FAIL + result + bcolors.ENDC)
        out.write(result + '\n') if out else None
    elif q not in accepting:
        result = '-{} : {}'.format(q,s)
        print(bcolors.FAIL + result + bcolors.ENDC)
        out.write(result + '\n') if out else None
    else:
        result = '+A : {}'.format(s)
        print(bcolors.OKGREEN + result + bcolors.ENDC)
        out.write(result + '\n') if out else None

    return state in accepting

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
        help='mostrar leganda')
    args = parser.parse_args()

    if not (args.str or args.file or args.out):
        parser.print_help()
        sys.exit(1)

    print('ER = 5(7p+8a)\u207A7')

    if args.file:
        strings = args.file.read().splitlines()
        for s in strings:
            sread(s,args.out) if args.out else sread(s)
        args.file.close()

    if args.str:
        sread(args.str)

    if args.out:
        args.out.close()

    if args.legend:
        stop_time = timeit.default_timer()
        execution_time = round(stop_time - start_time,4)
        print('+A : Aceito')
        print('-I : Rejeitado (Indefinido)')
        print('-# : Rejeitado (Estado nao final)')
        print(' t : {}s'.format(execution_time))

    sys.exit(0)