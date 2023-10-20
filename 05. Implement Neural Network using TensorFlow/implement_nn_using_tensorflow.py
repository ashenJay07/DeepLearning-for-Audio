import numpy as np
from random import random
from sklearn.model_selection import train_test_split


def generate_dataset(num_samples, test_size=0.3):
  # Create dataset
  x = np.array([[random() / 2 for _ in range(2)] for _ in range(num_samples)])
  y = np.array([[i[0] + i[1]] for i in x])

  # Create training and testing sets
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
  return x_train, x_test, y_train, y_test


if __name__ == "__main__":
  x_train, x_test, y_train, y_test = generate_dataset(10, 0.2)
  print("x_test: \n{}\n".format(x_test))  # 2 x 2 matrix
  print("y_test: \n{}".format(y_test))  # 2 x 1 matrix

