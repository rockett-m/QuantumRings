#!/usr/bin/env python3

import os
import sys
import platform
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import QuantumRingsLib
from QuantumRingsLib import (
    QuantumRegister,
    AncillaRegister,
    ClassicalRegister,
    QuantumCircuit,
    QuantumRingsProvider,
    job_monitor,
    JobStatus,
    qasm2,
    OptimizeQuantumCircuit
)

from matplotlib import pyplot as plt
import numpy as np
import math
import networkx as nx
import argparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT)

from utils.api import get_provider_and_backend


def parse_args():
    parser = argparse.ArgumentParser(description='Visualize the coupling map of a quantum backend.')
    parser.add_argument('--num_qubits', type=int, default=128,
                        help='Number of qubits to visualize [128, 200] supported')
    args = parser.parse_args()
    return args


def visualize_coupling_map(backend):
    """Create a visualization of the quantum backend's coupling map.

    The coupling map shows how qubits are connected in the quantum device.
    Each node represents a qubit, and each edge represents a possible
    interaction between qubits.

    Args:
        backend: QuantumRings backend object containing the coupling map
    """
    # Create a directed graph
    G = nx.DiGraph()

    # Add edges from the coupling map
    coupling_map = backend.coupling_map
    G.add_edges_from(coupling_map)

    # Set up the plot with white background
    plt.figure(figsize=(12, 12), facecolor='white')
    ax = plt.gca()
    ax.set_facecolor('white')

    # Create a grid layout for the nodes
    # First, determine the grid dimensions based on number of qubits
    num_qubits = len(G.nodes)
    grid_size = int(np.ceil(np.sqrt(num_qubits)))

    # Create positions dictionary for grid layout
    pos = {}
    for i in G.nodes:
        row = i // grid_size
        col = i % grid_size
        pos[i] = np.array([col, -row])  # Negative row to plot from top to bottom

    # Draw the complete graph
    nx.draw(G, pos,
            node_color='lightblue',
            node_size=500,
            arrowsize=10,
            width=0.5,
            with_labels=True,
            font_size=8,
            font_weight='bold')

    # Set equal aspect ratio to make grid square
    plt.grid(True)
    ax.set_aspect('equal')

    # Add some padding around the graph
    x_values = [x for x, y in pos.values()]
    y_values = [y for x, y in pos.values()]
    x_margin = 0.5
    y_margin = 0.5
    plt.xlim(min(x_values) - x_margin, max(x_values) + x_margin)
    plt.ylim(min(y_values) - y_margin, max(y_values) + y_margin)

    # Remove axis labels
    plt.axis('off')

    # Add a title
    plt.title(f'QuantumRings Coupling Map - {backend.num_qubits} Qubits\n{backend.name} v{backend.backend_version}', pad=20)

    # Save the plot
    output_folder = os.path.join(ROOT, 'images')
    os.makedirs(output_folder, exist_ok=True)
    generated_image = os.path.join(output_folder, f'coupling_map_{backend.num_qubits}q_{backend.name}.png')
    plt.savefig(generated_image, dpi=300, bbox_inches='tight')
    print(f"\nCoupling map visualization saved as {generated_image}")
    print(f"Number of qubits: {backend.num_qubits}")
    print(f"Number of connections: {len(coupling_map)}")


if __name__ == "__main__":
    # provider, backend = get_provider_and_backend(num_qubits=200)
    args = parse_args()

    provider, backend = get_provider_and_backend(num_qubits=args.num_qubits)

    visualize_coupling_map(backend)


"""
run at project root:
uv run visuals/view_coupling_map.py --num_qubits 200
or
uv run visuals/view_coupling_map.py --num_qubits 128
"""
