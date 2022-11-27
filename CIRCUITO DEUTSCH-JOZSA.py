import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as 

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(3, 3)
#"00 -> 0"
#"01 -> 0"
#"10 -> 1"
#"11 -> 1"
# Entrada del circuito

#circuit.x(2) [001]

#circuit.x(1) [010]

#circuit.x(2) circuit.x(1) [011]

#circuit.x(0) [100]

#circuit.x(0) circuit.x(2) [101]

#circuit.x(1) circuit.x(0) [110]

#circuit.x(2) circuit.x(1)  circuit.x(0) [111]

circuit.barrier(0,1,2)
circuit.cx(0,2)
circuit.barrier(0,1,2)
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)
# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
# Draw the circuit
print(circuit)
# Plot a histogram
plot_histogram(counts)
plt.show()



# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(3, 3)
#"00 -> 0"
#"01 -> 0"
#"10 -> 1"
#"11 -> 1"
# Entrada del circuito

#circuit.x(2) [001]

#circuit.x(1) [010]

#circuit.x(2) circuit.x(1) [011]

#circuit.x(0) [100]

#circuit.x(0) circuit.x(2) [101]

#circuit.x(1) circuit.x(0) [110]

#circuit.x(2) circuit.x(1)  circuit.x(0) [111]

circuit.barrier(0,1,2)
circuit.i(0)
circuit.i(1)
circuit.i(2)
circuit.barrier(0,1,2)
# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [2,1,0])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)
# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
# Draw the circuit
print(circuit)
# Plot a histogram
plot_histogram(counts)
plt.show()
