import numpy as np

Q = np.array([
    [ 0.15, 0.1 ],
    [ 0.1,  0.12 ]])

eigenvalues, eigenvectors = np.linalg.eig(Q)
print("Eigenvalues:\n", eigenvalues, "\n")
print("Eigenvectors:\n", eigenvectors, "\n")
# Largest eigenvalue domainates
print(2 * eigenvectors)
