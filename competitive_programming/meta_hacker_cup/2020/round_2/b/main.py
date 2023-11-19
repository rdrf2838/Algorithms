from collections import defaultdict
import ipdb
import copy
import pandas as pd
from tqdm import tqdm
import os
from glob import glob
from decimal import *
directions=[(0,1),(1,0),(0,-1),(-1,0)]

path_in=glob('*_input.txt')[0]
path_out='out.txt'
if os.path.exists(path_out):
    os.remove(path_out)
f_in=open(path_in)
f_out=open(path_out,'a')
t_tot=int(f_in.readline())
bignum=1000000007

for t in tqdm(range(1,t_tot+1)):
    n,p=f_in.readline().strip().split()
    n=int(n)
    p=Decimal(p)
    memo=[[0 for _ in range(n+1)]for _ in range(n+1)]
    memo[2][0]=Decimal(1.0)
    memo[2][1]=Decimal(1.0)
    for ni in range(3,n+1):
        for k in range(ni):
            A=k*(k-1)/2
            C=k
            D=ni-k-1
            B=C*D
            E=D*(D-1)/2
            Tot=ni*(ni-1)/2
            # if t==3:
            #     import ipdb;ipdb.set_trace()
            if not A+B+C+D+E==Tot:
                import ipdb;ipdb.set_trace()
            a,b,c,d,e=map(lambda x:Decimal(x)/Decimal(Tot),[A,B,C,D,E])
            memo[ni][k]=1+\
                e*(memo[ni-1][k])\
                +d*((1-p)*(memo[ni-1][k]))
            if k>0:
                memo[ni][k]+=\
                    (a+b)*(memo[ni-1][k-1])\
                    +c*(p*(memo[ni-1][k-1]))
    f_out.write(f'Case #{t}:\n')
    for i in range(n):
        f_out.write(f'{memo[n][i]}\n')