from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Función que se encarga de convertir un número decimal a binario
def Binario(n):
    string = ""
    while n != 0:
        string += str(n % 2)
        n = n // 2
    string = string[::-1]
    while len(string) < 5:
        string = "0" + string
    return string
 
# Función que imprime con formato a una matriz
def printMatrix(matrix):
    for i in matrix:
        print(" ".join(i))
    print()
   

def isBalanced(counts):
    if '0000' in counts.keys():
        print("Es constante.")
    else:
        print("Es balanceada.")

def Test():
    res = []
    print("\n1. Funcion Balanceada.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)

    circuit.x(4)
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.h(4)

    circuit.barrier()
    circuit.cx(0, 4)
    circuit.cx(1, 4)
    circuit.cx(2, 4)
    circuit.cx(3, 4)
    circuit.barrier()
    circuit.x(0)
    circuit.x(2)

    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.barrier()


    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()

    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("2. Funcion Balanceada.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)

    circuit.x(4)
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.h(4)

    circuit.barrier()
    circuit.x(2)
    circuit.x(4)
    circuit.cx(3, 4)
    circuit.barrier()
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.barrier()


    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()

    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("3. Funcion Balanceada.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)

    circuit.x(4)
    circuit.barrier(0, 1, 2, 3, 4)
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.h(4)

    circuit.barrier()
    circuit.x(1)
    circuit.cx(3, 4)
    circuit.cx(2, 4)
    circuit.barrier()

    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.barrier()
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()

    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("4. Funcion Constante.\n")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)

    circuit.x(4)
    circuit.barrier(0, 1, 2, 3, 4)
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.h(4)
    circuit.barrier(0, 1, 2, 3, 4)
    circuit.ccx(0, 1, 3)
    circuit.barrier(0, 1, 2, 3, 4)
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.barrier(0, 1, 2, 3, 4)


    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()

    counts = result.get_counts(circuit)
    res.append(counts)
    isBalanced(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    res = list(res)
    return res
