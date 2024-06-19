# Grover's Algorithm Implementation

This repository contains a Jupyter notebook that implements Grover's algorithm using Qiskit. Grover's algorithm is a quantum search algorithm that provides a quadratic speedup for unstructured search problems.

## Files

- `grovers_algorithm.ipynb`: The Jupyter notebook with the implementation and explanation of Grover's algorithm.
- `README.md`: This file.

## Requirements

- Python 3.x
- Qiskit
- Matplotlib
- Numpy

## Installation

To install the necessary dependencies, run:
!pip install qiskit, matplotlib, numpy

## Code Explanation
1. Imports and Setup
First, we import the necessary libraries:

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import matplotlib.pyplot as plt

2. Oracle Definition
The oracle function applies a controlled-Z (CZ) gate to the first and last qubits:

def oracle(qc, n):
    qc.cz(0, n-1)

3. Diffuser Definition
The diffuser function implements the inversion about the mean, which is an essential part of Grover's algorithm:

def diffuser(n):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
    return qc

4. Grover's Algorithm Implementation
The grovers_algorithm function sets up and runs the quantum circuit for Grover's algorithm:

def grovers_algorithm(N):
    n = int(np.ceil(np.log2(N)))  # Number of qubits
    qc = QuantumCircuit(n, n)

    # Apply Hadamard gates to all qubits
    
  qc.h(range(n))

    # Apply the oracle and diffuser 
  num_iterations = int(np.sqrt(N))
  for _ in range(num_iterations):
      oracle(qc, n)
      qc.append(diffuser(n).to_gate(), range(n))

    # Measure the qubits
  qc.measure(range(n), range(n))

    # Execute the circuit
  simulator = Aer.get_backend('qasm_simulator')  # Use qasm_simulator
  compiled_circuit = transpile(qc, simulator)
  result = simulator.run(compiled_circuit, shots=1024).result()

    # Plot the results
  counts = result.get_counts()
  plot_histogram(counts)

  return counts

5. Example Usage
To run the algorithm for a specific problem size N, simply call the function with the desired value of N:

N = 155  # Example number to factorize
result = grovers_algorithm(N)
print(result)

6. Plotting the Results
Finally, the results are plotted using Matplotlib:

plt.bar(result.keys(), result.values())
plt.xlabel('Measurement Outcomes')
plt.ylabel('Counts')
plt.title('Grover\'s Algorithm Results')
plt.show()

![download](https://github.com/Aakanksha04022004/Grover-s_algorithm/assets/146117000/4f43280d-4735-4172-936b-41cdce82c5f5)

## Circuit Visualization
To visualize the quantum circuits, you can use Qiskit's built-in visualization tools. Here is how you can display the oracle and diffuser circuits:

oracle_circuit = QuantumCircuit(n)
oracle(oracle_circuit, n)
oracle_circuit.draw('mpl')

diffuser_circuit = diffuser(n)
diffuser_circuit.draw('mpl')


