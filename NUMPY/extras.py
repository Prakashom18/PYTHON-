import numpy as np
x=np.array([1,2,3,4,5])
for y in x:
    print(y)
    z=np.sin(y)
    print(z)
    
print("A RANGE")
arr=np.arange(0,5,1)
print(arr)
l=np.cos(arr)
m=np.tan(arr)
print(l)
print(m)

arr1=np.arange(0,5*np.pi,1)
print(arr1)

ar=np.array([1,2,3,4,5])
print(np.exp(ar))
print()
print(np.log(ar))
print()
print(np.log10(ar))
