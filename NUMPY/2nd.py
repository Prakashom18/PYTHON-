import numpy as np

a= np.array([1,2,3,5,88])
print(a)
print(a.max()) #max 
print(a.min())  #min
print(a.sum())  #sum

b=np.array([(1,2,3),(4,5,6),(7,5,3)])
print(b.sum(axis=1)) #sum of one row
print(np.sqrt(a)) 
print(np.std(a))#std deviation
print(b.ravel()) #combines the inside array
a= np.array([1,2,3,5,88])
b= np.array([1,2,3,5,88])
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)

print(np.vstack((a,b))) #vertical stack
print(np.hstack((a,b))) #horizontal stack
