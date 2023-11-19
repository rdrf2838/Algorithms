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
    n,k,w=[int(x) for x in f_in.readline().strip().split()]
    lefts=[0]*n
    heights=[0]*n
    for arr in [lefts,heights]:
        arr[:k]=[int(x) for x in f_in.readline().strip().split()]
        a,b,c,d=[int(x) for x in f_in.readline().strip().split()]
        for i in range(k,n):
           arr[i]=(a*arr[i-2]+b*arr[i-1]+c)%d+1
    curr_heights=[0]*(lefts[-1]+w)
    for i in range(n):
        l=lefts[i]
        h=heights[i]
        for curr_w in range(w):
            curr_heights[l+curr_w]=max(curr_heights[l+curr_w],h)
    
    curr_perimeter=0
    perimeter_product=1
    rightmost=-1
    for i in range(n):
        # if t==3 and i==2:
        #     import ipdb;ipdb.set_trace()
        l=lefts[i]
        h=heights[i]
        if l>rightmost:
            curr_perimeter+=2*(h+w)
        else:
            if h<=curr_heights[l-1]:
                curr_perimeter+=2*(l+w-rightmost)
            else:
                curr_perimeter+=2*(l+w-rightmost+h-curr_heights[l-1])
        rightmost=l+w
        # print(f'{t}:{i}: {curr_perimeter}')
        perimeter_product=(perimeter_product*curr_perimeter) % bignum
    f_out.write(f'Case #{t}: {perimeter_product}\n')
