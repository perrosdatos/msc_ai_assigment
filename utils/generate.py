from itertools import permutations
import random
from tqdm import tqdm
def generate_network(num_nodes, rand_a, rand_b):
    nodes_list = [x for x in range(num_nodes)]
    edges = list(permutations(nodes_list, 2))
    edges_w = [(*x, random.randint(rand_a,rand_b)) for x in edges]

    return nodes_list, edges_w

def generate_sequential_pairs( dna):
    if len(dna) < 2:
        return []
    
    return [(dna[i], dna[i+1]) for i in range(len(dna) - 1)]+[(dna[-1], dna[0])]