import os
from glob import glob
from xmlrpc.client import FastParser
directions=[(0,1),(1,0),(0,-1),(-1,0)]
def inter(iterable):
    return list(map(lambda x:int(x),iterable))

path_in=glob('*_input.txt')[0]
path_out='out.txt'
if os.path.exists(path_out):
    os.remove(path_out)
f_in=open(path_in)
f_out=open(path_out,'a')
t_tot=int(f_in.readline())

letters=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
vowels={'A','E','I','O','U'}
consonants=letters-vowels

for t in range(1,t_tot+1):
    s=f_in.readline().strip()
    best=1010
    for letter in letters:
        curr=0
        is_vowel=letter in vowels
        # breakpoint()
        for c in s:
            c_is_vowel=c in vowels
            if c==letter:
                continue
            elif is_vowel==c_is_vowel:
                curr+=2
            else:
                curr+=1
        best=min(best,curr)
    f_out.write(f'Case #{t}: {best}\n')
