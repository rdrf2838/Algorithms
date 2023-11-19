import os
from glob import glob
from xmlrpc.client import FastParser
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
for t in range(1,t_tot+1):
    r,c=inter(f_in.readline().split())
    grid=[]
    grid2=[]
    for i in range(r):
        grid.append(f_in.readline())
        grid2.append(list(grid[i].replace('.','^')))
    def count(i,j):
        ctr=0
        for di,dj in directions:
            i2,j2=i+di,j+dj
            if 0<=i2<r and 0 <=j2<c and grid2[i2][j2]=='^':
                ctr+=1
        return ctr
    def prune(i,j):
        positions=[(i,j)]
        while len(positions)>0:
            i_curr,j_curr=positions.pop()
            if grid[i_curr][j_curr]=='^':
                return False
            else:
                grid2[i_curr][j_curr]='.'
                for di,dj in directions:
                    i2,j2=i_curr+di,j_curr+dj
                    if 0<=i2<r and 0 <=j2<c and grid2[i2][j2]=='^' and count(i2,j2)<2:
                        positions.append((i2,j2))
        return True

    # def prune(i,j):
    #     if grid[i][j]=='^':
    #         return False
    #     else:
    #         grid2[i][j]='.'
    #         ans=True
    #         for di,dj in directions:
    #             i2,j2=i+di,j+dj
    #             if 0<=i2<r and 0 <=j2<c and grid2[i2][j2]=='^' and count(i2,j2)<2:
    #                 ans=ans and prune(i2,j2)
    #         return ans
    ans=True
    for i in range(r):
        if not ans:
            break
        for j in range(c):
            if grid2[i][j]=='^' and count(i,j)<2:
                if grid[i][j]=='^':
                    ans=False
                    break
                else:
                    res=prune(i,j)
                    if not res:
                        ans=False
                        break
    if ans:
        f_out.write(f'Case #{t}: Possible\n')
        for i in range(r):
            for j in range(c):
                f_out.write(grid2[i][j])
            f_out.write('\n')
    else:
        f_out.write(f'Case #{t}: Impossible\n')
    

