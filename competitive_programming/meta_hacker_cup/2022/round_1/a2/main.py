import os
from glob import glob
directions=[(0,1),(1,0),(0,-1),(-1,0)]
def inter(iterable):
    return list(map(lambda x:int(x),iterable))
# Python program for KMP Algorithm
class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret




def test():
    p1 = "aa"
    t1 = "aaaaaaaa"

    kmp = KMP()
    assert(kmp.search(t1, p1) == [0, 1, 2, 3, 4, 5, 6])

    p2 = "abc"
    t2 = "abdabeabfabc"

    assert(kmp.search(t2, p2) == [9])

    p3 = "aab"
    t3 = "aaabaacbaab"

    assert(kmp.search(t3, p3) == [1, 8])

    p4 = "11"
    t4 = "111"
    assert(kmp.search(t4, p4) == [0, 1])

    print("all test pass")

path_in=glob('*_input.txt')[0]
path_out='out.txt'
if os.path.exists(path_out):
    os.remove(path_out)
f_in=open(path_in)
f_out=open(path_out,'a')
t_tot=int(f_in.readline())

for t in range(1,t_tot+1):
    n,k = inter(f_in.readline().split())
    str_a=f_in.readline().strip().replace(' ','')
    str_b=f_in.readline().strip().replace(' ','')
    kmp=KMP()
    idxes_match=kmp.search(str_a+str_a,str_b)
    if len(idxes_match)==0:
        f_out.write(f'Case #{t}: NO\n')
    else:
        idx_match=idxes_match[0]
        if idx_match==0:
            if len(idxes_match)==2:
                if k==1:
                    f_out.write(f'Case #{t}: NO\n')
                elif k%2==0:
                    f_out.write(f'Case #{t}: YES\n')
                else:
                    if n==2:
                        f_out.write(f'Case #{t}: NO\n')
                    else:
                        f_out.write(f'Case #{t}: YES\n')
            else:
                f_out.write(f'Case #{t}: YES\n')
        else:
            if k==0:
                f_out.write(f'Case #{t}: NO\n')
            elif k%2==1:
                f_out.write(f'Case #{t}: YES\n')
            else:
                if n==2:
                    f_out.write(f'Case #{t}: NO\n')
                else:
                    f_out.write(f'Case #{t}: YES\n')

        # if n==2:
        #     if idx_match==0:
        #         if k%2==0:
        #             f_out.write(f'Case #{t}: YES\n')
        #         else:
        #             f_out.write(f'Case #{t}: NO\n')
        #     else:
        #         if k%2==1:
        #             f_out.write(f'Case #{t}: YES\n')
        #         else:
        #             f_out.write(f'Case #{t}: NO\n')
        # else:
        #     if idx_match==0:
        #         if k!=1:
        #             f_out.write(f'Case #{t}: YES\n')
        #         else:
        #             f_out.write(f'Case #{t}: NO\n')
        #     else:
        #         if k!=0:
        #             f_out.write(f'Case #{t}: YES\n')
        #         else:
        #             f_out.write(f'Case #{t}: NO\n')