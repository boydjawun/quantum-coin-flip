# Quantum Coin Flip🪙
<img src="https://github.com/boydjawun/quantum-coin-flip/blob/main/assets/Screenshot%202026-08-30%20063845.png" height = "500" width = "500">

> A simple Qiskit + IonQ program that puts a qubit in superposition and measures it as **Heads** or **Tails**.

| | |
|---|---|
| **Backend** | IonQ simulator (`simulator`) |
| **Circuit** | 1 qubit + Hadamard + measure |
| **SDK** | [Qiskit](https://qiskit.org) + [qiskit-ionq](https://pypi.org/project/qiskit-ionq/) |
| **Language** | Python |

> Create an [IonQ Cloud](https://cloud.ionq.com) account to get an API key.  
> Store the key as an environment variable, or pass it directly to `IonQProvider(API_KEY)`.

---

## Features

- Interactive Heads / Tails guess in the terminal
- Single-qubit Hadamard circuit (true 50/50 superposition)
- Runs on the IonQ cloud simulator
- ASCII banner via `pyfiglet`
- Instant win/lose check against the measured outcome

---

## Project structure
```
quantum-coin-flip/
├── coin-flip.py    # Circuit, IonQ backend, and CLI game
└── README.md
```

---

## Quick start

### Prerequisites

- Python 3.8+
- An [IonQ Cloud](https://cloud.ionq.com) account and API key
- Qiskit + IonQ provider:

```
pip install -U qiskit qiskit-ionq
pip install pyfiglet
```
# IonQ API key
> The API key comes from creating an IonQ Cloud account. Use it in one of two ways:

1. Environment variable (recommended):
   
- **Linux & macOS**: ``` export IONQ_API_KEY="your_ionq_api_key" ``` 

- **Windows**: ``` setx IONQ_API_KEY "your_ionq_api_key" ``` 
> Close and reopen the terminal after setx

2. Pass the key into the provider
``` provider = IonQProvider("your_ionq_api_key") ```

# Run
``` python coin-flip.py ```
# Circuit Setup
```
from qiskit import QuantumCircuit
from qiskit_ionq import IonQProvider

provider = IonQProvider()  # or IonQProvider(API_KEY)
simulated_backend = provider.get_backend("simulator")

qc = QuantumCircuit(1, name="Quantum Coin Flip")
qc.h(0)            # superposition (50/50)
qc.measure_all()   # collapse to 0 or 1

job = simulated_backend.run(qc, shots=1)
result = job.get_counts()
```
# Tech Stack

| | |
|---|---|
| **Language** | Python |
| **SDK** | Qiskit |
| **Provider** | qiskit-ionq (IonQ Cloud simulator) |
| **CLI banner** | pyfiglet |
