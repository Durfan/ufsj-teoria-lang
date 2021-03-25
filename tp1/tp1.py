#!/usr/bin/python3

import argparse
import sys, time

start_time = time.time()

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

def accepts(s,output=None):
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
        output.write(result + '\n') if output else None
    elif q not in accepting:
        result = '-{} : {}'.format(q,s)
        print(bcolors.FAIL + result + bcolors.ENDC)
        output.write(result + '\n') if output else None
    else:
        result = '+A : {}'.format(s)
        print(bcolors.OKGREEN + result + bcolors.ENDC)
        output.write(result + '\n') if output else None

    return state in accepting

if __name__ == '__main__':
    print('UFSJ/T.Linguagens TP1')
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--string')
    parser.add_argument('-f','--file', type=argparse.FileType('r', encoding='UTF-8'))
    parser.add_argument('-o','--output', type=argparse.FileType('w', encoding='UTF-8'))
    args = parser.parse_args()

    if not (args.string or args.file or args.output):
        parser.error('No action requested')

    print('ER = 5(7p+8a)\u207A7\n')

    if args.file:
        strings = args.file.read().splitlines()
        for s in strings:
            accepts(s,args.output) if args.output else accepts(s)
        args.file.close()

    if args.string:
        accepts(args.string)

    if args.output:
        args.output.close()

    print('\n+A Aceito -I Indefinido -# Nao Final')
    print('{}s'.format(time.time() - start_time))
    sys.exit(0)