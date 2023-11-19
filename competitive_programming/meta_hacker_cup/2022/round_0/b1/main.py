import os
from collections import defaultdict
from glob import glob

def inter(iterable):
    return list(map(lambda x:int(x),iterable))

path_in=glob('*_input.txt')[0]
path_out='out.txt'
if os.path.exists(path_out):
    os.remove(path_out)
f_in=open(path_in)
f_out=open(path_out,'a')
t_tot=int(f_in.readline())
for t in range(1,t_tot+1):
    r,c=inter(f_in.readline().split())
    num_trees=0
    for i in range(r):
        line=f_in.readline()
        if '^' in line:
            num_trees+=1
    res=True
    if num_trees==0 or (r!=1 and c!=1):
        f_out.write(f'Case #{t}: Possible\n')
        if num_trees==0:
            char='.'
        else:
            char='^'
        for i in range(r):
            f_out.write(char*c+'\n')
    else:
        f_out.write(f'Case #{t}: Impossible\n')
