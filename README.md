# Multi-Agent Pathfinding (A* and CBS) 🚀

This repository contains Python scripts for solving and visualizing pathfinding problems. It features a straightforward conversion of grid-based maps to graph representations, single-agent A* search, and a simplified multi-agent approach using Conflict-Based Search (CBS) principles.

## Features ✨

* **Grid to Graph Conversion (`GridToGraphConversion.py`)**: 
  Converts a generic 2D grid (where `1` defines a valid path and `0` defines an obstacle) into a graph mapped with coordinates and their corresponding accessible neighbors. Includes a basic plot visualization of the resultant graph.
  
* **Single Agent A* Pathfinding (`SingleAgentAStar.py`)**: 
  Implements the standard A* pathfinding algorithm using a pre-defined graph and Manhattan distance as an admissible heuristic. Reconstructs and plots the chosen optimal path on a static graph visualization.

* **Multi-Agent Conflict-Based Pathfinding (`MultiAgentCBS.py`)**: 
  Implements a simple Multi-Agent Path Finder that detects when multiple agents are navigating the same coordinates simultaneously. Re-evaluates their A* path dynamically upon conflict detection. Plots paths of all agents to visually inspect routes and conflicts.

## Requirements 🛠️

Ensure you have Python 3 installed. You will also need the `matplotlib` library for rendering the graphical visualizations.

You can install the dependencies via pip:

```bash
pip install matplotlib
```

## Usage 💡

Each script is standalone and contains a `main()` execution block. Simply execute the script of interest through your Python interpreter from the project root.

### 1. View Grid-To-Graph Conversion
Evaluates a simple 9x10 grid matrix and plots the network of nodes:
```bash
python GridToGraphConversion.py
```

### 2. View Single Agent Pathfinding
Visualizes the shortest path bounded by a predefined graph from a start point `(0,0)` to an end point `(3,4)`:
```bash
python SingleAgentAStar.py
```

### 3. View Multi-Agent Pathfinding
Demonstrates the resolution of collision courses between two agents moving natively on a large, hardcoded graph:
```bash
python MultiAgentCBS.py
```

---
*Created and maintained as a demonstration of basic node traversal and collision-checking strategies.*
