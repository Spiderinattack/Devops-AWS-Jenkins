#!/bin/python3

#import sys

if __name__ == "__main__":
    ''' Main logic'''
    n = int(input().strip())
    l = []
    for a0 in range(n):
        s, n = input().strip().split(' ')
        s, n = [str(s), str(n)]
        l.append((s,n))
    l = [x for x in l if \
         x[1].count('4')==x[1].count('7') \
         and x[1].count('4')+x[1].count('7')==len(x[1])]
    l.sort(key = lambda x: int(x[1]))
    if len(l) > 0:
        print(l[0][0])
    else:
        print('-1')
