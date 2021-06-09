import numpy as np
from scipy import io

a = np.ones((4,4))

io.savemat('test.txt',{'ar':a})
data = io.loadmat('test.txt',struct_as_record=True)
print(data['ar'])