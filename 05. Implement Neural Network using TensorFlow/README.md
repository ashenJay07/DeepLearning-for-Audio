## Table of Contents

1. [What is TensorFlow](#what-is-tensorflow)
2. [Steps to follow when implementing NN using TensorFlow](#steps-to-follow-when-implementing-nn-using-tensorflow)
3. [What is Keras](#what-is-keras)
4. [Dense layer](#dense-layer)
5. [Other common layers provided by Keras](#other-common-layers-provided-by-keras)

&nbsp;

## What is TensorFlow?

- TensorFlow is a open source software framework for building and training machine learning models
- TensorFlow is named after the mathematical concept of tensors (multi-dimensional arrays)
- Popular for deep learning tasks
- TensorFlow allows us to build models using high-level APIs (like Keras) or directly manipulate tensors for low-level control
- **Scalability:** can be used on various platforms, from smartphones to clusters of servers
- **Eco-system:** part of a ML ecosystem that includes tools like <ins>TensorBoard for visualization</ins> and <ins>TensorFlow Serving for deploying models</ins>
- Supports a wide range of hardware accelerators, including GPUs and TPUs (Tensor Processing Units)
- TensorFlow can be integrated with other popular libraries and frameworks in the machine learning and data science space
- Many companies and researchers use TensorFlow for their machine learning and deep learning projects

&nbsp;

## Steps to follow when implementing NN using TensorFlow

1. Implement model (implement the architecture)
2. Compile model
3. Train model
4. Evaluate model
5. Make predictions

&nbsp;

## What is Keras

- Keras is a high-level neural networks API written in Python
- Keras provides a simple, user-friendly interface for designing neural networks and deep learning models
- Keras promotes modularity, allowing easy construction of complex neural networks from building blocks
- **Versatility:** Keras supports various types of neural networks, including feedforward, convolutional, and recurrent networks

&nbsp;

## Dense layer

- Dense typically refers to a layer in a neural network
- Also known as a fully connected layer
- In this layer, each neuron is connected to every neuron in the previous and subsequent layers
- Used for learning complex patterns and relationships in the data
- The term "dense" indicates that there are dense connections between neurons in this layer

&nbsp;

## Other common layers provided by Keras

- Conv2D (Convolutional layers)
- LSTM and GRU (Recurrent layers)
- MaxPooling2D and AveragePooling2D (Pooling layers)
- Dropout
- Flatten
- Embedding
- BatchNormalization
- Concatenate and Add
