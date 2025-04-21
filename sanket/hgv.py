import numpy as np
import matplotlib.pyplot as plt
a = np.array([10, 20, 30, 40, 50,60])
print(a)

student=np.dtype([('name','S20'),('age','i1'),('mrk','f4')])
a=np.array([('vijay',20,30),('pras',39,24)],dtype=student)
print(a)

a = np.array([10, 20, 30, 40, 50,60])
a.shape=(6,1)
print(a)

plt.plot([1,2,5,4,2])
plt.ylabel('some no')
plt.show()