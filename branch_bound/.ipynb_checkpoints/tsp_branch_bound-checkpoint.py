# Python3 program to solve the Traveling Salesman Problem (TSP) using 
# the Branch and Bound method.
#
#=============================== DISCLAIMER ==============================================
# This is the exact code found at:
# https://www.geeksforgeeks.org/traveling-salesman-problem-using-branch-and-bound-2/
#=========================================================================================

import math
maxsize = float('inf')

def getting_ady_list(nodes, edges):
    """
        This function was developed by team15
    """
    ady_list = [[0 for _ in nodes] for _ in nodes]
    for edge_w in edges:
        ady_list[edge_w[0]][edge_w[1]] = edge_w[2]
        ady_list[edge_w[1]][edge_w[0]] = edge_w[2]
    return ady_list

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
    return min

def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif adj[i][j] <= second and adj[i][j] != first:
            second = adj[i][j]
    return second

def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited):
    global final_res

    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if (adj[curr_path[level-1]][i] != 0 and not visited[i]):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
                                 firstMin(adj, i)) / 2)

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                TSPRec(adj, curr_bound, curr_weight, level + 1, curr_path, visited)

            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
            visited[i] = False  # Correctly backtrack only the current node

def TSP(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(adj, i) + secondMin(adj, i))

    curr_bound = math.ceil(curr_bound / 2)
    visited[0] = True
    curr_path[0] = 0

    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)

class TSPBranchBound:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def run(self):
        global adj, N, final_path, visited, final_res
        
        # Initialize/reset variables before each run
        adj = getting_ady_list(nodes=self.nodes, edges=self.edges)
        N = len(self.nodes)
        final_path = [None] * (N + 1)
        visited = [False] * N
        final_res = maxsize
        
        TSP(adj)
        
        return final_path, final_res
