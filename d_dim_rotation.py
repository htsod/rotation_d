# d_dim_rotation.py
# Max Liang
# created 02/04/2023
# Description:


import numpy as np

def d_rotation(N, vec, angles):

    A = np.zeros([int(N * (N - 1) / 2), N, N])
    k, cap = 0, 1
    for i in range(N - 1):
        for j in range(cap, N):
            A[k][i][j] = (-1) ** k
            A[k][j][i] = (-1) ** (k + 1)
            k += 1
        cap += 1

    R = np.identity(N)
    for r in range(k):
        g = A[r].dot(A[r]) * np.cos(angles[r]) + A[r] * np.sin(angles[r])
        for ii in range(N):
            if g[ii][ii] == 0:
                g[ii][ii] = 1
        R = R.dot(g)
    vec_prime = R.dot(vec)
    return np.round(vec_prime, 3)

# example for 3 dimensional rotation
N = 3
vec = np.array([1.0, 0.0, 0.0])
angles = np.array([0, np.pi/2, 0])
vec_prime = d_rotation(N, vec, angles)
print(f"vector {vec} rotate through angle {np.round(angles, 2)} to vector prime {vec_prime}")
