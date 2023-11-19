import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a[0]
c=a[0:2]
d=a[:,0]
e=a[:,0:2]
i=np.where(b>1,-1,-2)
print(i)