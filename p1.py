import numpy as np

arr = np.array([1,2,3])
print(arr)
print(np.empty(0))
print(np.zeros(2))
x = np.ones(4)
print(x)
print(np.arange(5))
print(np.arange(0,10,2))

A = np.array([[7,1,5,3],[2,8,4,6]])
print(np.sort(A))
print(np.sort(A,axis = 0))
print(A.ndim)

dtype = [('name','S20'),('height',float),('age',int)]
values = [('Krushna',5.5,23),('Ruchita',4.8,20),('Tushar',4.9,21)]
a = np.array(values,dtype=dtype)
print(np.sort(a,order='height'))
print(np.sort(a,order=['age','height']))

B = np.array([[[2,3,4,5],[5,68,8,6]],[[3,4,5,6],[5,7,3,4]]])
C = B.copy()
C[0][1][1] = 34
print(C)
print(B)

D = np.array([[[2,3,4,5],[5,68,8,6]],[[3,4,5,6],[5,7,3,4]]])
E = D.view()
E[0][1][1] = 34
print(E)
print(D)

P = np.array([[1,2,3,12],[3,56,6,7]])
print(P.sum())

A = {1,2,1,1,1,2,2,1,1,2,2,2}
print(type(A))