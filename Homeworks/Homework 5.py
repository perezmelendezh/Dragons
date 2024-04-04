import numpy as np

# 1. Hey Twin
def findEqual(arr):
    return arr[np.all(arr == arr[:,0][:,None], axis=1)]

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
print(findEqual(arr))

# 2. Checkers
def checkerboard():
    arr = np.zeros((8,8), dtype=int)
    arr[::2, ::2] = 1
    arr[1::2, 1::2] = 1
    return arr

print(checkerboard())

# 3 I need some space 
def spaceBetween(myarr):
    return np.array([' '.join(list(s)) for s in myarr])

myarr = np.array(['python', 'is', 'cool!'])
print(spaceBetween(myarr))

# 4 Everything is in other 

def sorting(a):
    return np.sort(a, axis=0)

np.random.seed(12345)
a = np.random.randint(1, 50, (4, 5))
print(a)
print(sorting(a))


