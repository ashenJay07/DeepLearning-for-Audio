import numpy as np

# Multilayer Perceptron (MLP): Forward Propagation
class MLP:
  def __init__(self, num_inputs=3, num_hidden=[3, 5], num_outputs=2):
    self.num_inputs = num_inputs
    self.num_hidden = num_hidden
    self.num_outputs = num_outputs

    layers = [self.num_inputs] + num_hidden + [self.num_outputs]

    # Initiate random weights
    self.weights = []
    for i in range(len(layers) - 1):
      w = np.random.rand(layers[i], layers[i + 1])
      self.weights.append(w)


  # Implement forward propagation
  def forward_propagate(self, inputs):
    activations = inputs

    for w in self.weights:
      # Calculate net inputs
      net_inputs = np.dot(activations, w)

      # Calculate the activations
      activations = self._sigmoid(net_inputs)

    return activations


  # Implement sigmoid activation function
  def _sigmoid(self, x):
    return 1 / (1 + np.exp(-x))



if __name__ == "__main__":
  # Create a MLP
  mlp = MLP()

  # Create some inputs
  inputs = np.random.rand(mlp.num_inputs)

  # Perform forward prop
  outputs = mlp.forward_propagate(inputs)

  # Print the result
  print("The network input is: {}".format(inputs))
  print("The network output is: {}".format(outputs))