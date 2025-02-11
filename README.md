# QuantumRings

A Python project for working with the QuantumRings quantum computing platform.

## Development Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and virtual environment creation. uv can be installed via brew or other package managers.

### Environment Setup

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies from requirements.txt
uv pip install -r requirements.txt
```

### Managing Dependencies with uv

uv manages dependencies based on `pyproject.toml` and `.python-version`. Key commands:

```bash
# Add a new dependency
uv pip install <package>

# Remove a dependency
uv pip uninstall <package>

# Update lock file
uv pip compile requirements.txt

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
# NAME=your-email@example.com
# TOKEN=your-rings-128-token
```

## Usage

Currently, this project provides helper utilities for connecting to the QuantumRings platform. More features and examples coming soon.

### Backend Configuration

```python
from utils.api import get_provider_and_backend

provider, backend = get_provider_and_backend()
```

## References

- [uv Documentation](https://docs.astral.sh/uv/)
- [Official QuantumRings Installation Guide](https://portal.quantumrings.com/doc/Installation.html#installing-the-toolkit-for-qiskit)
- [QuantumRings Backend Documentation](https://portal.quantumrings.com/doc/BackendV2.html)