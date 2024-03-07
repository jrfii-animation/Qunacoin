from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

def bb84(len_key):
    """BB84 Quantum Key Distribution"""

    # Initialize qubits
    q = QuantumRegister(len_key)
    c = ClassicalRegister(len_key)
    qc = QuantumCircuit(q, c)

    # Prepare qubits in |+> state
    qc.h(range(len_key))

    # Encode random key
    # ...

    # Transmit qubits
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend)
    result = job.result().get_counts()

    # Measure random bases and filter
    # ...

    shared_key = ''.join(result)
    return shared_key

def e91(len_key):
    """Ekert91 Quantum Key Distribution"""
    # ...

# ... other QKD protocols