# Quiz 4

## Question 1

Suppose that we have a neuron which, in a given time period, will fire with probability 0.1, yielding a Bernoulli distribution for the neuron's firing (denoted by the random variable F = 0 or 1) with P(F = 1) = 0.1. 

Which of these is closest to the entropy H(F) of this distribution (calculated in bits, i.e., using the base 2 logarithm)?

```python
import math
0.1 * math.log(0.1, 2) + 0.9 * math.log(0.9, 2) # 0.4690
```

## Question 2

Continued from Question 1:

Now lets add a stimulus to the picture. Suppose that we think this neuron's activity is related to a light flashing in the eye. Let us say that the light is flashing in a given time period with probability 0.10. Call this stimulus random variable S.

If there is a flash, the neuron will fire with probability 1/2. If there is not a flash, the neuron will fire with probability 1/18. Call this random variable F (whether the neuron fires or not).

Which of these is closest, in bits (log base 2 units), to the mutual information MI(S,F)?

