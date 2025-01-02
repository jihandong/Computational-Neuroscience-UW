import numpy as np

W = np.array([
    [ 0.6, 0.1, 0.1, 0.1, 0.1 ],
    [ 0.1, 0.6, 0.1, 0.1, 0.1 ],
    [ 0.1, 0.1, 0.6, 0.1, 0.1 ],
    [ 0.1, 0.1, 0.1, 0.6, 0.1 ],
    [ 0.1, 0.1, 0.1, 0.1, 0.6 ]])

u = np.array([[0.6, 0.5, 0.6, 0.2, 0.1]]).T

M = np.array([
    [ -0.125, 0, 0.125, 0.125, 0],
    [ 0, -0.125, 0, 0.125, 0.125],
    [ 0.125, 0, -0.125, 0, 0.125],
    [ 0.125, 0.125, 0, -0.125, 0],
    [ 0, 0.125, 0.125, 0, -0.125]])

E_vals, E_vecs = np.linalg.eig(M)

print(E_vals)
print(E_vecs)

"""
for i in range(E_vecs.shape[1]):
    print(f"M * e      {i} = {np.dot(M, E_vecs[:, i])}")
    print(f"lambda * e {i} = {E_vals[i] * E_vecs[:, i]}")
"""

"""
for i in range(E_vecs.shape[1]):
    for j in range(i, E_vecs.shape[1]):
        dot_product = np.dot(E_vecs[:, i], E_vecs[:, j])
        print(f"Dot product of vector {i+1} and vector {j+1}: {dot_product}")
"""

h = np.dot(W, u)
v_ss = np.zeros(h.shape)
for i in range(h.shape[0]):
    v_eig = np.array([E_vecs[i]])
    v_ss += np.dot(h.T, v_eig.T) / (1 - E_vals[i]) * v_eig.T

print(v_ss)
