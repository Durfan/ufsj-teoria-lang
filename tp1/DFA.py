#!/usr/bin/python

import argparse

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
    cursor = ''
    for index,c in enumerate(s):
        try:
            state = dfa[state][c]
            #cursor += c
            q = state
        except KeyError:
            cursor = s[:index] + '[' + c +']' + s[index+1:]
            indefinition = True
            state = False
            break

    if indefinition:
        print('-I : {}'.format(cursor))
    elif q not in accepting:
        print('-F : q{}'.format(s,q))
    else:
        print('+A : {}'.format(s))

    return state in accepting

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', type=argparse.FileType('r', encoding='UTF-8'))
    parser.add_argument('-o','--output', type=argparse.FileType('w', encoding='UTF-8'))
    args = parser.parse_args()

    if args.file:
        strings = args.file.read().splitlines()
        for s in strings:
            accepts(s)
        args.file.close()