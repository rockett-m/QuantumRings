#!/usr/bin/env python3

"""
can be imported as a module ...
ROOT = ...; sys.path.append(ROOT);
from utils.api import get_provider_and_backend
provider, backend = get_provider_and_backend()

or
ran as a script (also prints debug info)
uv run utils/api.py
"""

import os
import sys
import platform
from dotenv import load_dotenv
from QuantumRingsLib import QuantumRingsProvider

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT)


def load_credentials() -> tuple[str, str]:
    """ load .env file to get credentials """
    if not os.path.exists(os.path.join(ROOT, '.env')):
        raise ValueError(".env file is not found")
    try:
        load_dotenv()
    except Exception as e:
        raise ValueError from e

    TOKEN = os.getenv("TOKEN", None)
    if not TOKEN:
        raise ValueError("TOKEN is not set")

    NAME = os.getenv("NAME", None)
    if not NAME:
        raise ValueError("NAME is not set")
    return NAME, TOKEN

def get_provider() -> object | None:
    """
    returns a QuantumRingsProvider object or None
    """
    NAME, TOKEN = load_credentials()
    # token='rings-128 ....'
    # name='<email for account>'
    try:
        QRingsProvider = QuantumRingsProvider(
            token=TOKEN,
            name=NAME
        )
    except ConnectionError as e:
        raise ValueError from e
    except Exception as e:
        raise ValueError from e
    finally:
        return QRingsProvider

def get_backend(QRingsProvider: object) -> object | None:
    """
    https://portal.quantumrings.com/doc/BackendV2.html

    returns a Backend object or None
    """
    try:
        backend = QRingsProvider.get_backend("scarlet_quantum_rings")
    except ConnectionError as e:
        raise ValueError from e
    except Exception as e:
        raise ValueError from e
    finally:
        return backend

def get_provider_and_backend() -> tuple[object, object]:
    """
    import this module into other scripts to get provider and backend objects
    """
    QRingsProvider = get_provider()
    backend = get_backend(QRingsProvider)
    assert QRingsProvider is not None
    assert backend is not None

    return QRingsProvider, backend


def debug_info(QRingsProvider: object, backend: object) -> None:

    print("\nsys.path =")
    [print(f"{x}") for x in sys.path]

    print(f'\n{platform.system() = }')
    print(f'{platform.machine() = }\n')

    print(f'{QRingsProvider = }')
    print(f'{backend = }')

    """ cli output
    QRingsProvider = QuantumRingsProvider(
        version = 1,
        'backends': ['scarlet_quantum_rings']
    )
    backend = Backend(
        backend_name = scarlet_quantum_rings,
        backend_version = 0.9.0,
        online_date = 9/12/2023,
        num_qubits = 128
    )
    """

    # Specific attribute prints
    print(f'{backend.name = }')  # instead of backend_name
    print(f'{backend.backend_version = }')
    print(f'{backend.online_date = }')
    print(f'{backend.num_qubits = }')
    print(f'{backend.description = }')

    # Dynamic attribute discovery
    print('\nAll Backend Attributes:'); print('-' * 50)

    # Get all public attributes (those not starting with _)
    attributes = [attr for attr in dir(backend) if not attr.startswith('_')]
    attributes.sort()

    for attr in attributes:
        # coupling_map         = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [0, 4], [4, 0], [0, 5],
        # 4], [124, 127], [127, 125], [125, 127], [127, 126], [126, 127]]
        try:
            value = getattr(backend, attr)
            # Skip methods, only print properties
            if not callable(value):
                if type(value) is int:
                    print(f'{attr:20} = {value}')
                elif len(value) <= 50:
                    print(f'{attr:20} = {value}')
                else:
                    # coupling map is a list of lists and large output given 128 qubits
                    print(f'{attr:20} = {value[:50]}\n...\n{value[-50:]}\n')
        except Exception as e:
            print(f'{attr:20} = Error: {e}')

    print()


if __name__ == "__main__":

    QRingsProvider, backend = get_provider_and_backend()

    debug_info(QRingsProvider, backend)


"""
sample output

(quantumrings) /Users/sudo/CodeProjects/QuantumRings/ uv run utils/api.py

sys.path =
.../QuantumRings/utils
/opt/homebrew/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python313.zip
/opt/homebrew/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13
/opt/homebrew/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload
.../QuantumRings/.venv/lib/python3.13/site-packages
.../QuantumRings

platform.system() = 'Darwin'
platform.machine() = 'arm64'

QRingsProvider = QuantumRingsProvider(version = 1,'backends': ['scarlet_quantum_rings'])
backend = Backend(backend_name = scarlet_quantum_rings,backend_version = 0.9.0,online_date = 9/12/2023,num_qubits = 128)
backend.name = 'scarlet_quantum_rings'
backend.backend_version = '0.9.0'
backend.online_date = '9/12/2023'
backend.num_qubits = 128
backend.description = 'Quantum Rings Simulator Scarlet'

All Backend Attributes:
--------------------------------------------------
backend_version      = 0.9.0
coupling_map         = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [0, 4], [4, 0], [0, 5], [5, 0], [0, 6], [6, 0], [0, 7], [7, 0], [0, 8], [8, 0], [0, 9], [9, 0], [0, 10], [10, 0], [0, 11], [11, 0], [0, 12], [12, 0], [0, 13], [13, 0], [0, 14], [14, 0], [0, 15], [15, 0], [0, 16], [16, 0], [0, 17], [17, 0], [0, 18], [18, 0], [0, 19], [19, 0], [0, 20], [20, 0], [0, 21], [21, 0], [0, 22], [22, 0], [0, 23], [23, 0], [0, 24], [24, 0], [0, 25], [25, 0]]
...
[[127, 102], [102, 127], [127, 103], [103, 127], [127, 104], [104, 127], [127, 105], [105, 127], [127, 106], [106, 127], [127, 107], [107, 127], [127, 108], [108, 127], [127, 109], [109, 127], [127, 110], [110, 127], [127, 111], [111, 127], [127, 112], [112, 127], [127, 113], [113, 127], [127, 114], [114, 127], [127, 115], [115, 127], [127, 116], [116, 127], [127, 117], [117, 127], [127, 118], [118, 127], [127, 119], [119, 127], [127, 120], [120, 127], [127, 121], [121, 127], [127, 122], [122, 127], [127, 123], [123, 127], [127, 124], [124, 127], [127, 125], [125, 127], [127, 126], [126, 127]]

description          = Quantum Rings Simulator Scarlet
dt                   = 1
dtm                  = 1
max_circuits         = 1
name                 = scarlet_quantum_rings
num_qubits           = 128
online_date          = 9/12/2023
version              = 2
"""
