import numpy as np

a = np.array([[4,5],[3,2]])
b=a.copy()

from scipy.linalg import det

#determinant
print(det(a))

#inverse
from scipy.linalg import inv

print(inv(b)) 

# print(a.ndim,a.shape) 