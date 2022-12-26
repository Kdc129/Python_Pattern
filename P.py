import numpy as np

arr = np.array([1,2,3,4,5])         #One-Dimension Array
brr = np.array([[1,2,3,4],[5,6,7,8]])   #Two-Dimension Array
crr = np.array([[[12,3,4,6],[4,5,6,7]],[[12,4,5,6],[8,9,7,6]]])   #Three-Dimension Array

#We can create a NumPy ndarray object by using the array() function.
print(type(arr))

#To check data type of array we use dtype function
print("Data type of arr is ::",arr.dtype)

#To change data type of array we use astype function
r = brr.astype('f')
print("Data type of arr is ::",r.dtype)

#To check dimension of given array we use ndim function
print("Dimension of brr array is ::",brr.ndim)

#We can set dimension for array by using ndmin() function
A = np.array([1,2,3,4],ndmin=3)
print("Dimension of A ::",A.ndim)

print("One-Dimension Array ::")
for i in arr:
    print(i,end=" ")
print()

print("Two-Dimension Array ::")
for j in brr:
    for k in j:
        print(k,end=" ")
    print()

print("Three-Dimension Array ::")
for o in crr:
    for t in o:
        for p in t:
            print(p,end=" ")
        print()
    
"""The copy owns the data and any changes made to 
   the copy will not affect original array,
   and any changes made to the original array 
   will not affect the copy."""
Arr1 = np.array([5,6,7,9])
Arr2 = Arr1.copy()
Arr1[0:2]=([3,4])
print("Arr1 array becomes ::",Arr1)
print("Copied array Arr2 becomes ::",Arr2)

"""The view does not own the data and any changes made to
   the view will affect the original array, 
   and any changes made to the original array 
   will affect the view."""

Brr1 = np.array([5,6,7,9])
Brr2 = Brr1.view()
Brr1[0:2]=([13,24])
print("Brr1 array becomes ::",Brr1)
print("Viewed array Brr2 becomes ::",Brr2)

#The copy returns None.
#The view returns the original array.
print("Copy :: ",Arr2.base)   
print("View :: ",Brr2.base)      

# we want to join to the concatenate() function, along with the axis. 
# If axis is not explicitly passed, it is taken as 0.

#we concatenate Arr1 & Brr1 into Crr1

Crr1 = np.concatenate([Arr1,Brr1])
print(Crr1)

A = np.array([[4,6,7,8],[7,8,9,5]])
B = np.array([[5,4,2,3],[9,6,4,1]])
C = np.concatenate((A,B),axis = -1)
print("Join by using concatenate ::",C)

"""We pass a sequence of arrays that we want 
to join to the stack() method along with the axis.
 If axis is not explicitly passed it is taken as 0."""

r = np.stack((Arr1,Brr1),axis=1)
print("Join by using stack ::",r)

#NumPy provides a helper function: hstack() to stack along rows.

P = np.array([2,3,4,5])
Q = np.array([4,5,6,7])
T = np.hstack((P,Q))
print("Stack along rows ::",T)
W = np.vstack((P,Q))
print("Stack along columns ::",W)
U = np.dstack((P,Q))
print("Stack along depth ::",U)


