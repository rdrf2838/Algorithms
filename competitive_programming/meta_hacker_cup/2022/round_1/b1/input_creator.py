from glob import glob
path_in=glob('*_input.txt')[0]
f_in=open(path_in,'w')
f_in.write('50\n')
for i in range(50):
    f_in.write('500000\n')
    for j in range(500000):
        f_in.write('1000000000 1000000000\n')
    f_in.write('500000\n')
    for j in range(500000):
        f_in.write('1000000000 1000000000\n')
f_in.close()