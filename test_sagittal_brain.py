import numpy as np

input = np.zeros((20, 20))
input[-1, :] = 1
np.savetxt("brain_sample.csv", input, fmt='%d', delimiter=',')

expected = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

