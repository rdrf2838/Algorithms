from collections import defaultdict
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
    garage=[]
    r,c,k=(int(x) for x in f_in.readline().strip().split())
    for _ in range(r):
        garage.append(f_in.readline().strip())
    garage=['.'*c]+garage+['.'*c]
    cum_down=[[0 for _ in range(c)]for _ in range(r+3)]
    cum_up=[[0 for _ in range(c)]for _ in range(r+3)]
    for i in range(1,r+3):
        for j in range(c):
            cum_down[i][j]=cum_down[i-1][j]+(1 if garage[i-1][j]=='X' else 0)
    for i in reversed(range(r+2)):
        for j in range(c):
            cum_up[i][j]=cum_up[i+1][j]+(1 if garage[i][j]=='X' else 0)
    
    ans=0
    for letter in garage[k]:
        if letter=='X':
            ans+=1
    # import ipdb;ipdb.set_trace()
    
    for i in range(k+1,r+2):
        d=i-k
        curr=d
        for j in range(c):
            letter=garage[i][j]
            if letter=='X':
                curr+=1
            elif letter=='.':
                if cum_down[i+1][j]-cum_down[0][j]>=k:
                    curr+=1
        # if curr==3:
        #     import ipdb;ipdb.set_trace()
        ans=min(ans,curr)
    for i in range(0,k):
        d=k-i
        curr=d
        for j in range(c):
            letter=garage[i][j]
            if letter=='X':
                curr+=1
            elif letter=='.':
                if cum_up[i][j]-cum_up[r+2][j]>=r+1-k:
                    curr+=1
        ans=min(ans,curr)
        # if curr==3:
        #     import ipdb;ipdb.set_trace()
    f_out.write(f'Case #{t}: {ans}\n')


    
