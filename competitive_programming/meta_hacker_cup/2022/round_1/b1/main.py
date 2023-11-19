import pandas as pd
from tqdm import tqdm
import os
from glob import glob
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
bignum=1000000007

def findSquareSum(Coordinates, N):
    xq , yq = 0, 0
    xs , ys = 0, 0
 
    # Stores final answer
    res = 0
 
    # Traverse the array
    for i in range(N):
 
        a = Coordinates[i][0]
        b = Coordinates[i][1]
 
        res += xq
        res -= 2 * xs * a
 
        # Adding the effect of this
        # point for all the previous
        # x - points
        res += i * (a * a)
 
        # Temporarily add the
        # square of x-coordinate
        xq += a * a
        xs += a
        res += yq
        res -= 2 * ys * b
        res += i * b * b
 
        # Add the effect of this point
        # for all the previous y - points
        yq += b * b
        ys += b
 
    # Print the desired answer
    return res

for t in tqdm(range(1,t_tot+1)):
    n=int(f_in.readline().strip())
    pos_tree=[0]*n
    for i in range(n):
        a,b=inter(f_in.readline().strip().split())
        pos_tree[i]=(a,b)
    q=int(f_in.readline().strip())
    pos_well=[0]*q
    for i in range(q):
        x,y=inter(f_in.readline().strip().split())
        pos_well[i]=(x,y)
    ans=(findSquareSum(pos_tree+pos_well,n+q)-findSquareSum(pos_tree,n)-findSquareSum(pos_well,q))%bignum
    f_out.write(f'Case #{t}: {ans}\n')

