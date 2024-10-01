# Group 15 Assignment Report
## An Evolutionary Algorithm for the Travelling Salesman Problem

**Course:** TARI29 Artificial Intelligence, 2024 Evolutionary Computation Assignment  
**University:** Jonkoping University  
**Program:** MSc AI Engineering Program  

### Authors
- Gonzalez Juan Carlos
- Batini Dhanwanth
- Bhargavi Chadalawada
- Divya Komati

**Date:** September 30, 2024


| No. | Notebook Name                        | Description                                             |
|-----|--------------------------------------|---------------------------------------------------------|
| 1   | `1.- population_tunning.ipynb`       | Notebook for tuning the population parameters.          |
| 2   | `2.- crossover_proportion field.ipynb` | Analysis of crossover proportion in genetic algorithms. |
| 3   | `3.- mutation_thd.ipynb`             | Study of mutation threshold effects on optimization.    |
| 4   | `4.- exploration_prob.ipynb`         | Exploration probability settings and their impacts.     |
| 5   | `5 Notebook for testing.ipynb`       | Testing GA-P Using randomized samples. (Testing with different sizes)   |
| 6   | `6.-ComparingAlgorithms.ipynb`       | Comparison of different algorithms' performance (Data Generation).        |
| 7   | `7-Final_graphs.ipynb`               | Generation of final visualizations and graphs to compare different algorithms approach.          |
| 8   | `8.- Numerical Results Replication.ipynb` | Replication and verification of numerical results (Will be used to validate results in our work).     |




## Overview

### `ga/tsp_ga.py`
This corresponds to the **GA-N** algorithm in the written work. It implements a Genetic Algorithm (GA) using a **STATIC \|v\|//2 CUT CROSSOVER**.

### `ga/tsp_ga_din_crossover.py`
This corresponds to the **GA-P** algorithm in the written work, using a dynamic crossover proportion.

### `branch_bound/TSP.py`
Contains the implementation of the Branch and Bound algorithm, which was copied and modified from the [tsp-solver repository](https://github.com/mostafabahri/tsp-solver/).


## Usage Examples

### Importing Classes and Running Algorithms

```python
# Importing necessary classes from the modules
from branch_bound.TSP import TSPBranchBound
from ga.tsp_ga_din_crossover import TSPGA 
from ga.tsp_ga import TSPGA as TSPGAStaticCrossover

# Parameters for the GA algorithms
params = {
    "population_prop": 1.1, 
    "crossover_proportion": 0.8,
    "mutation_thd": 0.3, 
    "exploration_prob": 0.2
}

# Define the 4-node complete graph
nodes = [0, 1, 2, 3]
edges = [
    [0, 1, 10],
    [0, 2, 20],
    [0, 3, 25],
    [1, 2, 15],
    [1, 3, 35],
    [2, 3, 30]
]

# Running Branch and Bound algorithm
tsp_search = TSPBranchBound(nodes, edges)
tour1, cost1 = tsp_search.run()

# Running Genetic Algorithm with Dynamic Crossover (GA-P)
ga = TSPGA(nodes, edges, **params)
tour2, cost2 = ga.run()

# Running Genetic Algorithm with Static Crossover (GA-N)
ga_static = TSPGAStaticCrossover(nodes, edges, **params)
tour3, cost3 = ga_static.run()
