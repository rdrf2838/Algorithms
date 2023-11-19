from collections import defaultdict
import ipdb
import copy
import pandas as pd
from tqdm import tqdm
import networkx as nx
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
    pass