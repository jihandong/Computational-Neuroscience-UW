import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('tuning_3.4.pickle', 'rb') as f:
    tunning_data = pickle.load(f)

nb_timeslices = 24
nb_neurons = 4
neuron_labels = ["neuron1", "neuron2", "neuron3", "neuron4"]
colors = ['red', 'yellow', 'green', 'blue']
x = tunning_data['stim']

with open('pop_coding_3.4.pickle', 'rb') as f:
    coding_data = pickle.load(f)

basis_labels = ["c1", "c2", "c3", "c4"]
exprm_labels = ["r1", "r2", "r3", "r4"]
resultQ9 = np.zeros(2)

# quesion7: plot the firing rate curves.
plt.figure(1)
for i in range(nb_neurons):
    y = np.mean(tunning_data[neuron_labels[i]], axis = 0)
    plt.plot(x, y, label = neuron_labels[i], color = colors[i])
plt.legend()

# quesion8: the expectations and variants.
plt.figure(2)
for i in range(nb_neurons):
    means = np.mean(tunning_data[neuron_labels[i]], axis = 0)
    vars = np.var(tunning_data[neuron_labels[i]], axis = 0)
    fano = np.where(means == 0, 0, vars / means)
    plt.plot(x, fano, label = neuron_labels[i], color = colors[i])
plt.legend()
plt.show()

# quesion9: 
for i in range(nb_neurons):
    basis = coding_data[basis_labels[i]]
    exprm = coding_data[exprm_labels[i]]
    peak_spike = np.max(tunning_data[neuron_labels[i]])
    resultQ9 += basis * np.mean(exprm) / peak_spike
print(resultQ9)
print(np.degrees(np.arctan2(resultQ9[1], resultQ9[0])))
# NOTE: we ignored the lambda for coding efficiency and difference
# between our result and reality.
