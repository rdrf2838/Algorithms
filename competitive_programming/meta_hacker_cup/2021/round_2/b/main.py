from collections import defaultdict
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
    n,m=(int(x)for x in f_in.readline().strip().split())
    p=[]
    for _ in range(n+1):
        row=(int(x) for x in f_in.readline().strip().split())
        d=defaultdict(int)
        for s in row:
            d[s]+=1
        p.append(d)

    d_style_used_num=defaultdict(lambda:defaultdict(int))
    for k,v in p[0].items():
        d_style_used_num[k][0]=v

    ans=0
    for i in range(1,n+1):
        d_style_used_num_nxt=defaultdict(lambda:defaultdict(int))
        for s in p[i]:
            num_unused=d_style_used_num[s][0]
            num_used=d_style_used_num[s][1]
            num_req=p[i][s]
            if num_req>num_used+num_unused:
                ans+=num_req-num_unused-num_used
                d_style_used_num_nxt[s][0]=num_unused
                d_style_used_num_nxt[s][1]=num_req-num_unused
            elif num_req>num_used:
                d_style_used_num_nxt[s][0]=num_req-num_used
                d_style_used_num_nxt[s][1]=num_used
            else:
                d_style_used_num_nxt[s][0]=0
                d_style_used_num_nxt[s][1]=num_req
        d_style_used_num=d_style_used_num_nxt
    unused=0
    for s in d_style_used_num:
        unused+=d_style_used_num[s][0]
    f_out.write(f'Case #{t}: {max(0,ans-m+unused)}\n')
    




        