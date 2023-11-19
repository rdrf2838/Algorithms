import os
from collections import defaultdict
from glob import glob
path_in=glob('*_input.txt')[0]
path_out='out.txt'
if os.path.exists(path_out):
    os.remove(path_out)
f_in=open(path_in)
f_out=open(path_out,'a')
t=int(f_in.readline())
for i in range(1,t+1):
    n,k=f_in.readline().split()
    n=int(n)
    k=int(k)
    s_arr=f_in.readline().split()
    s_dict=defaultdict(lambda:0)
    for s in s_arr:
        s_dict[s]+=1
    res=True
    for _,v in s_dict.items():
        if v>2:
            res=False
            break
    if n > 2*k:
        res=False
    ans='YES' if res else 'NO'
    f_out.write(f'Case #{i}: {ans}\n')