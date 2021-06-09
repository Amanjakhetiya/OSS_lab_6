from scipy.linalg import eig
import numpy as np

a = np.array([[5,4],[6,3]])

eigen_values,eigen_vector = eig(a)

print("Eigen Values:",eigen_values,end='\n')
print("Eigen Vectors:",eigen_vector,end='\n')
