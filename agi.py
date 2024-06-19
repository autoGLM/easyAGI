import numpy as np
import logging
from jax import numpy as jnp
import jax
from jax import grad, jit, vmap, pmap
from typing import List, Tuple, Union
from concurrent.futures import ThreadPoolExecutor, as_completed
import optax  # For advanced optimization algorithms
import haiku as hk  # For model building and parameter management

class SimpleMind:
    def __init__(self, input_size, hidden_sizes, output_size, activation='relu', optimizer='adam', learning_rate=0.001, regularization=None, reg_lambda=0.01):
        """
        Initialize the SimpleMind neural network.
        
        :param input_size: Number of input neurons.
        :param hidden_sizes: List of the number of neurons in each hidden layer.
        :param output_size: Number of output neurons.
        :param activation: Activation function to use ('sigmoid', 'tanh', 'relu').
        :param optimizer: Optimizer to use ('sgd', 'adam').
        :param learning_rate: Learning rate for training.
        :param regularization: Regularization method ('l2').
        :param reg_lambda: Regularization strength.
        """
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.regularization = regularization
        self.reg_lambda = reg_lambda

        self.params = self._initialize_parameters()

        self.activation = activation
        self.optimizer = optimizer
        self.opt_state = self._setup_optimizer()
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def _activation_function(self, s):
        if self.activation == 'sigmoid':
            return 1 / (1 + jnp.exp(-s))
        elif self.activation == 'tanh':
            return jnp.tanh(s)
        elif self.activation == 'relu':
            return jnp.maximum(0, s)
        else:
            raise ValueError("Unsupported activation function.")

    def _activation_derivative(self, s):
        if self.activation == 'sigmoid':
            return s * (1 - s)
        elif self.activation == 'tanh':
            return 1 - jnp.power(s, 2)
        elif self.activation == 'relu':
            return jnp.where(s > 0, 1, 0)
        else:
            raise ValueError("Unsupported activation function.")

    def _initialize_parameters(self):
        params = {}
        layer_sizes = [self.input_size] + self.hidden_sizes + [self.output_size]
        for i in range(len(layer_sizes) - 1):
            params[f'W{i}'] = jnp.random.randn(layer_sizes[i], layer_sizes[i+1]) * 0.01
            params[f'b{i}'] = jnp.zeros(layer_sizes[i+1])
        return params

    def forward(self, X, params):
        activations = X
        for i in range(len(self.hidden_sizes) + 1):
            z = jnp.dot(activations, params[f'W{i}']) + params[f'b{i}']
            activations = self._activation_function(z) if i < len(self.hidden_sizes) else z
        return activations

    @jit
    def backpropagate(self, X, y, params, opt_state):
        def loss_fn(params):
            predictions = self.forward(X, params)
            loss = jnp.mean(jnp.square(y - predictions))
            if self.regularization == 'l2':
                l2_penalty = sum(jnp.sum(jnp.square(params[f'W{i}'])) for i in range(len(self.hidden_sizes) + 1))
                loss += self.reg_lambda * l2_penalty / 2
            return loss

        grads = grad(loss_fn)(params)
        updates, opt_state = self.optimizer.update(grads, opt_state)
        new_params = optax.apply_updates(params, updates)
        return new_params, opt_state

    def _setup_optimizer(self):
        if self.optimizer == 'adam':
            self.optimizer = optax.adam(self.learning_rate)
        elif self.optimizer == 'sgd':
            self.optimizer = optax.sgd(self.learning_rate)
        else:
            raise ValueError("Unsupported optimizer.")
        return self.optimizer.init(self.params)

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            self.params, self.opt_state = self._parallel_backpropagate(X, y, self.params, self.opt_state)
            if epoch % 100 == 0:
                loss = self._calculate_loss(X, y, self.params)
                logging.info(f"Epoch {epoch}, Loss: {loss}")

    def _parallel_backpropagate(self, X, y, params, opt_state):
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.backpropagate, X[i], y[i], params, opt_state) for i in range(len(X))]
            for future in as_completed(futures):
                params, opt_state = future.result()
        return params, opt_state

    @jit
    def _calculate_loss(self, X, y, params):
        output = self.forward(X, params)
        loss = jnp.mean(jnp.square(y - output))
        if self.regularization == 'l2':
            loss += self.reg_lambda / 2 * sum(jnp.sum(jnp.square(params[f'W{i}'])) for i in range(len(self.hidden_sizes) + 1))
        return loss

# Example Usage
if __name__ == "__main__":
    input_size = 3
    hidden_sizes = [5, 5]
    output_size = 1
    learning_rate = 0.001
    epochs = 1000

    X = jnp.array([[0.1, 0.2, 0.3]])
    y = jnp.array([[0.5]])

    mind = SimpleMind(input_size, hidden_sizes, output_size, activation='relu', optimizer='adam', learning_rate=learning_rate, regularization='l2', reg_lambda=0.01)

    mind.train(X, y, epochs)
    print("Final Output:", mind.forward(X, mind.params))
