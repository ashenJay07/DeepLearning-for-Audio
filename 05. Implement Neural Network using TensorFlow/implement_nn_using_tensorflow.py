import numpy as np
from random import random
import tensorflow as tf
from sklearn.model_selection import train_test_split


def generate_dataset(num_samples, test_size=0.3):
  # Create dataset
  x = np.array([[random() / 2 for _ in range(2)] for _ in range(num_samples)])
  y = np.array([[i[0] + i[1]] for i in x])

  # Create training and testing sets
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
  return x_train, x_test, y_train, y_test


if __name__ == "__main__":
  x_train, x_test, y_train, y_test = generate_dataset(5000, 0.2)

  # print("x_test: \n{}\n".format(x_test))  # 2 x 2 matrix
  # print("y_test: \n{}".format(y_test))  # 2 x 1 matrix

  # Build model: 2 -> 5 -> 1
  model = tf.keras.Sequential([
      tf.keras.layers.Dense(5, input_dim=2, activation='sigmoid'),  # Hidden-layer
      tf.keras.layers.Dense(1, activation='sigmoid')  # Output-layer
  ])

  # Compile model
  optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)  # SGD - Stochastic Gradient Descent
  model.compile(optimizer=optimizer, loss='MSE')  # loss means error

  # Train model
  model.fit(x_train, y_train, epochs=100)

  # Evaluate model
  print('\n\n======================= Model Evaluation =======================')
  model.evaluate(x_test, y_test, verbose=1)

  # Make predictions
  data = np.array([[0.1, 0.2], [0.3, 0.6]])
  predictions = model.predict(data)

  print('\n\n======================= Predictions =======================')
  for data, pred in zip(data, predictions):
    print("{} + {} = {}".format(data[0], data[1], pred[0]))