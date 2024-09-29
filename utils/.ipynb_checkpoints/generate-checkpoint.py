from itertools import permutations
import random
from tqdm import tqdm
import datetime as dt

def generate_network(num_nodes, rand_a, rand_b):
    nodes_list = [x for x in range(num_nodes)]
    edges = list(permutations(nodes_list, 2))
    edges_w = [(*x, random.randint(rand_a,rand_b)) for x in edges]

    return nodes_list, edges_w

def generate_sequential_pairs( dna):
    if len(dna) < 2:
        return []
    
    return [(dna[i], dna[i+1]) for i in range(len(dna) - 1)]+[(dna[-1], dna[0])]



def scheduler(solution, name=""):
    start = dt.datetime.now()
    tour, cost = solution.run()
    end = dt.datetime.now()
    seconds = (end-start).total_seconds()
    print(f"{name}: The process started {start} and ended at {end} with {seconds} seconds")
    return tour, cost, start, end, seconds