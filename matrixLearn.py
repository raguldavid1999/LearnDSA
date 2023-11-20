import numpy as np

a = np.array([[1,2,3,4],[4,55,1,2],
              [8,3,20,19],[11,2,22,21]])

m = np.reshape(a,(4,4))

m = np.append(m,[[1, 15,13,11]],0)

m = np.delete(m,[0],0)

print(m)