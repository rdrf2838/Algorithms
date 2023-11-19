from queue import Queue
import os
from glob import glob
from collections import defaultdict
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
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(1,t_tot+1):
    s=f_in.readline().strip()
    k=int(f_in.readline().strip())
    adj=defaultdict(lambda:dict())
    for i in range(k):
        a,b=list(f_in.readline().strip())
        adj[a][b]=True
    dist=defaultdict(lambda:dict())
    for letter in letters:
        for letter2 in letters:
            dist[letter][letter2]=-1
    for letter in letters:
        vis={letter}
        dist[letter][letter]=0
        q=Queue()
        q.put((0,letter))
        while not q.empty():
            d,l=q.get()
            d+=1
            for l2 in adj[l]:
                if l2 not in vis:
                    dist[letter][l2]=d
                    q.put((d,l2))
                    vis.add(l2)
    best=3000
    for letter in letters:
        ctr=0
        for c in s:
            if c==letter:
                pass
            else:
                amt=dist[c][letter]
                if amt==-1:
                    ctr=3000
                    break
                else:
                    ctr+=amt
        best=min(best,ctr)
    if best==3000:
        f_out.write(f'Case #{t}: -1\n')
    else:
        f_out.write(f'Case #{t}: {best}\n')

