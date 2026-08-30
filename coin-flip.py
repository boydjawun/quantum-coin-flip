#pip install -U qiskit qiskit-ionq
from qiskit import QuantumCircuit
from qiskit_ionq import IonQProvider
import pyfiglet

# Looks for IONQ_API_KEY in environment variables from API key provided from IONQ
# Make sure to restart the terminal after adding the env variable
# Alternatively, The API key can be used as a parameter for IonQProvider
provider = IonQProvider()
simulated_backend = provider.get_backend("simulator")

# Add pyfiglet banner <- pip install pyfiglet
figlet = pyfiglet.figlet_format("Welcome to Quantum Coin Flip!")
print(figlet)

# User input for interaction
guess = input("Heads or Tails?: ").strip().capitalize()
if guess not in ("Heads", "Tails"):
    print("You must enter 'Heads' or 'Tails'")
else:
    # Create a single-qubit circuit
    qc = QuantumCircuit(1, name="Quantum Coin Flip")
    qc.h(0)     # Put the qubit into superposition(50/50)
    qc.measure_all()    # Collapese it into a 0 or 1

    # Run it just once, since I only want a single flip
    job = simulated_backend.run(qc, shots=1)
    result = job.get_counts()

    # Result will look like {"0":1} or {"1":1}
    outcome = list(result.keys())[0]

    # Map the outcome to "Heads" or "Tails"
    labels = {"0":"Heads", "1":"Tails"}
    print("The Quantum coin landed on: ", labels[outcome])

    # Check if user's guess is correct
    if guess == labels[outcome]:
        print("You're correct!")
    else:
        print("You're wrong!")