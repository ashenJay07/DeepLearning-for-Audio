import numpy as np
from random import random


# Table of Contents :
#     1. save activation and derivatives
#     2. implement backpropagation
#     3. implement gradient descent
#     4. implement train
#     5. train our network with some dummy dataset
#     6. make predictions



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
      w = np.random.rand(layers[i], layers[i+1])
      self.weights.append(w)

    # Save activation
    self.activations = []
    for i in range(len(layers)):
      a = np.zeros(layers[i])
      self.activations.append(a)

    # Save derivatives
    self.derivatives = []
    for i in range(len(layers) - 1):
      d = np.zeros((layers[i], layers[i+1]))
      self.derivatives.append(d)


  # Implement forward propagation
  def forward_propagate(self, inputs):
    activations = inputs  # the input layer activation is just the input itself
    self.activations[0] = inputs

    for i, w in enumerate(self.weights):
      # Calculate matrix multiplication between previous activation and weight matrix
      net_inputs = np.dot(activations, w)

      # Applv sigmoid activation function
      activations = self._sigmoid(net_inputs)
      self.activations[i+1] = activations

    # Return output layer activation
    return activations


  # Implement forward propagation
  def back_propagate(self, error, verbose=False):
    # Looping all the layers (last to first)
    for i in reversed(range(len(self.derivatives))):
      activations = self.activations[i+1]
      delta = error * self._sigmoid_derivative(activations)  # Before reshape: ndarray([0.1, 0.2]) --> After reshape: ndarray([[0.1, 0.2]])
      delta_reshaped = delta.reshape(delta.shape[0], -1).T  # Reshaping delta
      current_activations = self.activations[i]  # Before reshape: ndarray([0.1, 0.2]) --> After reshape: ndarray([[0.1], [0.2]])
      current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)  # Reshaping activations
      self.derivatives[i] = np.dot(current_activations_reshaped, delta_reshaped)
      error = np.dot(delta, self.weights[i].T)

      if verbose:
        print("Derivatives for W{}: {}".format(i, self.derivatives[i]))

    return error;


  # Implement gradient descent
  def gradient_descent(self, learning_rate):
    for i in range(len(self.weights)):
      weights = self.weights[i]
      # print("Original W{} {}".format(i, weights))
      derivatives = self.derivatives[i]
      weights += derivatives * learning_rate
      # print("Updated W{} {}".format(i, weights))


  def train(self, inputs, targets, epochs, learning_rate):
    for i in range(epochs):
      sum_error = 0
      # Trick: for j, (input, target) in enumerate(zip(inputs, targets)):
      for input, target in zip(inputs, targets):
        # Forward propagation
        output = self.forward_propagate(input)

        # Calculate error
        error = target - output

        # Back propagation
        self.back_propagate(error)
        # mlp.back_propagate(error, verbose=True)

        # Apply gradient descent
        self.gradient_descent(learning_rate)

        # Calculating an error
        sum_error += self._mse(target, output)

      # report the error of each epoch
      # print("Error: {} at epoch {}".format((sum_error / len(inputs)), i))


  def _mse(self, target, output):
    return np.average((target - output) ** 2)

  def _sigmoid_derivative(self, x):
    return x * (1.0 - x)


  # Implement sigmoid activation function
  def _sigmoid(self, x):
    y = 1.0 / (1 + np.exp(-x))
    return y




if __name__ == "__main__":
  # Create a sample dataset to train a network for the sum operation
  inputs = np.array([[random() / 2 for _ in range(2)] for _ in range(1000)])  # array([[0.1, 0.2], [0.3, 0.4]])
  targets = np.array([[i[0] + i[1]] for i in inputs])    # array([0.3], [0.7]])

  # Create a MLP object --> MPL(input_layers, hidden_layers, output_layers)
  mlp = MLP(2, [5], 1)

  # Train MLP
  mlp.train(inputs, targets, 50, 0.1)

  # Create dummy data
  input = np.array([0.5, 0.3])
  # target = np.array([0.8])

  output = mlp.forward_propagate(input)
  print("\n\nOur neural network believes that {} + {} is equal to {}.".format(input[0], input[1], output[0]))