import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import matplotlib.pyplot as plt

# Define the oracle for a simple problem
def oracle(qc, n):
    qc.cz(0, n-1)

# Define the diffuser (inversion about the mean)
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

# Grover's Algorithm Implementation
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

# Example usage
N =  35 # Example number to factorize
result = grovers_algorithm(N)
print(result)

N =  155 # Example number to factorize
result = grovers_algorithm(N)
print(result)

plt.bar(result.keys(), result.values())
plt.xlabel('Measurement Outcomes')
plt.ylabel('Counts')
plt.title('Grover\'s Algorithm Results')
plt.show()