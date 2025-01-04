import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)

# Load the data and add a random offset
x = data['c10p1']
centrl = np.random.rand(2)
print(f"centrl = {centrl}")
x += centrl
plt.scatter(x[:,0], x[:,1])
plt.draw()

# The parameters
eta = 1
alpha = 1 # zero for Hebbian learning, which would explode
dt = 0.01
nb_test = 10
nb_iter = 50000

# Apply Ojia's rule to learn the principal component
colors = plt.cm.viridis(np.linspace(0, 1, nb_test))
for i in range(nb_test):
    trace = np.zeros((nb_iter, 2))
    w = np.random.uniform(-2, 2, 2)

    for j in range(nb_iter):
        u = x[j % x.shape[0]]
        v = np.dot(u, w)
        w += dt * eta * (v * u - alpha * v**2 * w)
        trace[j] = w

    plt.scatter(trace[:-1,0], trace[:-1,1], color=colors[i])
    plt.scatter(trace[-1,0], trace[-1:,1], color='r')
    print(f'test{i}, final w = ', w)
    plt.draw()

# Calculate the input data correlation matrix
cov = np.dot(x.T, x) / x.shape[0]
print(f"cov = \n{cov}")

# Calculate the eigenvalues and eigenvectors of the correlation
eigenvalues, eigenvectors = np.linalg.eig(cov)
print(f"eigenvalues = {eigenvalues}")
print(f"eigenvectors = \n{eigenvectors}")

plt.show()
"""
NOTE: The correlation matrix has only one principal eigenvector,
but there are two vectors of length 1 that are parallel to this
eigenvector. w can converge to either of these two vectors.

But, the final weights are not the same as the eigenvectors of
the correlation matrix. why?
"""
