from collections import defaultdict
import ipdb
import copy
import pandas as pd
from tqdm import tqdm
import os
from glob import glob
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
    p=float(p)
    memo=[[0 for _ in range(n+1)]for _ in range(n+1)]
    memo[2][1]=1
    memo[2][2]=1
    for ni in range(3,n+1):
        for k in range(ni):
            A=k(k-1)
            B=(ni-2)(ni-1)-A
            C=2*k
            D=2*(ni-k-1)
            Tot=A+B+C+D
            memo[ni][k]=(B/Tot+D/Tot(1-p))*(1+memo[ni-1][k])
            if k>0:
                memo[ni][k]+=(A/Tot+C/Tot*p)*(1+memo[ni-1][k-1])
    f_out.write(f'Case #{t}:\n')
    for i in range(k):
        f_out.write(f'{memo[n][i]}\n')