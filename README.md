# QuantumRings

A Python project for working with the QuantumRings quantum computing platform.

## Development Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and virtual environment creation. uv can be installed via brew or other package managers.

### Environment Setup

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate
```

### Managing Dependencies with uv

uv manages dependencies based on `pyproject.toml` and `.python-version`. Key commands:

```bash
# Add a new dependency
uv add <package>

# Remove a dependency
uv remove <package>

# Update lock file (uv run/sync does this too)
uv lock

# Run a Python script
uv run <script.py>

# List installed packages
uv pip list
```

For more uv commands and options, see the [uv CLI Reference](https://docs.astral.sh/uv/reference/cli/).

### Credentials

Create a `.env` file with your QuantumRings credentials:
```bash
cp .env.example .env
# Edit .env with your credentials:
NAME=your-email@example.com
# note: default is 128 qubits, 200 is bonus
TOKEN_128=your-rings-128-token
TOKEN_200=your-rings-200-token
```

## Usage

Currently, this project provides helper utilities for the QR api and visualization for the Quantum Computers.
1. The `utils` folder containers helper functions for connecting to the QuantumRings platform
   - the api file can be ran directly to view full info about a QR computer
   - the `def get_provider_and_backend(num_qubits: int = 128) -> tuple[object, object]:` function can be imported also
1. The `visuals` folder is for generating graphs of the coupling map amongst qubits on the QuantumRings computers
   - see `images` output folder

More features and examples coming soon.

### Backend Configuration

```python
from utils.api import get_provider_and_backend
# default is 128 qubits for this optional arg; can specify 128 or 200 qubits
provider, backend = get_provider_and_backend(num_qubits=128) 
```

## References

- [uv Documentation](https://docs.astral.sh/uv/)
- [Official QuantumRings Installation Guide](https://portal.quantumrings.com/doc/Installation.html#installing-the-toolkit-for-qiskit)
- [QuantumRings Backend Documentation](https://portal.quantumrings.com/doc/BackendV2.html)
