import math

def sigmoid(x):
  y = 1.0 / (1 + math.exp(-x))
  return y


def activate(inputs, weights):
  # Calculate net input
  h = 0
  for x, w in zip(inputs, weights):
    h += x * w

  # Calculate activation value
  return sigmoid(h)


def artifical_neuron():
  inputs = [0.5, 0.3, 0.2];
  weights = [.4, .7, .2]

  output = activate(inputs, weights)
  print(output)


artifical_neuron()