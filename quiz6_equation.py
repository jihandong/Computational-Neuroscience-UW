import numpy as np

W = np.array([
    [ 0.6, 0.1, 0.1, 0.1, 0.1 ],
    [ 0.1, 0.6, 0.1, 0.1, 0.1 ],
    [ 0.1, 0.1, 0.6, 0.1, 0.1 ],
    [ 0.1, 0.1, 0.1, 0.6, 0.1 ],
    [ 0.1, 0.1, 0.1, 0.1, 0.6 ]])

u = np.array([[ 0.6, 0.5, 0.6, 0.2, 0.1 ]]).T

M = np.array([
    [ -0.125, 0,      0.125,  0.125,  0      ],
    [ 0,      -0.125, 0,      0.125,  0.125  ],
    [ 0.125,  0,      -0.125, 0,      0.125  ],
    [ 0.125,  0.125,  0,      -0.125, 0      ],
    [ 0,      0.125,  0.125,  0,      -0.125 ]])

E_vals, E_vecs = np.linalg.eig(M)
print("Eigenvalues:\n", E_vals, "\n")
print("Eigenvectors:\n", E_vecs, "\n")
# NOTE: symmetric matrices always have orthogonal eigenvectors
print("eigenvectors are orthogonal (almost):\n",
      np.dot(E_vecs.T, E_vecs), "\n")


h = np.dot(W, u)
vss = np.zeros(h.shape)
for i in range(h.shape[0]):
    E_vec = np.array([E_vecs[:,i]]).T
    vss += np.dot(h.T, E_vec) / (1 - E_vals[i]) * E_vec

print("Stable state:\n", vss, "\n")
print("Should be zero:\n", -vss + h + np.dot(M, vss), "\n")
