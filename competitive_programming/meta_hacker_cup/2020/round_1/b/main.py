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
    # if t==2:
    #     import ipdb;ipdb.set_trace()
    n,m,k,s=[int(x) for x in f_in.readline().strip().split()]
    persons=[0]*n
    logs=[0]*m
    persons[:k]=[int(x) for x in f_in.readline().strip().split()]
    a,b,c,d=[int(x) for x in f_in.readline().strip().split()]
    for i in range(k,n):
        persons[i]=(a*persons[i-2]+b*persons[i-1]+c)%d+1
    logs[:k]=[int(x) for x in f_in.readline().strip().split()]
    a,b,c,d=[int(x) for x in f_in.readline().strip().split()]
    for i in range(k,m):
        logs[i]=(a*logs[i-2]+b*logs[i-1]+c)%d+1
    logs.sort()
    persons.sort()
    l=0
    h=2*(logs[-1]+persons[-1])
    def calculate(left,right,person_idx):
        if logs[left] >= persons[person_idx]:
            return logs[right]-persons[person_idx]
        elif logs[right]<=persons[person_idx]:
            return persons[person_idx]-logs[left]
        else:
            return min(
                2*(logs[right]-persons[person_idx])+persons[person_idx]-logs[left],
                2*(persons[person_idx]-logs[left])+logs[right]-persons[person_idx]
            )
    while l+1<h:
        # if h<=10:
        #     import ipdb;ipdb.set_trace()
        time_allowed=(l+h)//2
        left=0
        right=0
        person_index=0
        success=False
        while person_index<n:
            while right<m and calculate(left,right,person_index)<=time_allowed:
                right+=1
            if right==m:
                success=True
                break
            else:
                left=right
                person_index+=1
        if success:
            h=time_allowed
        else:
            l=time_allowed

    if h==1:
        time_allowed=0
        left=0
        right=0
        person_index=0
        success=False
        while person_index<n:
            while right<m and calculate(left,right,person_index)<=time_allowed:
                right+=1
            if right==m:
                success=True
                break
            else:
                left=right
                person_index+=1
        if success:
            h=0
        else:
            h=1
    f_out.write(f'Case #{t}: {h}\n')


    

