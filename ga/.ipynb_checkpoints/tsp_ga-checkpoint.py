import random
from itertools import permutations
import random
import pandas as pd

class TSPGA:
    def __init__(self, nodes_list, edges_w_list, population_number,*, crossover_proportion = 0.7,crossover_thd = None, mutation_thd = 0.1, exploration_prob = 0.1):
        self.nodes_list = nodes_list
        self.edges_w_list = edges_w_list
        self.population_number= population_number
        
        self.crossover_thd = crossover_thd
        self.crossover_proportion = crossover_proportion
        self.mutation_thd = mutation_thd

        self.exploration_prob = exploration_prob
        
        # Easy way to store nodes weights
        self.nodes_weights = self.__generate_dict_cost()
        
        self.population = self.__get_random_dnas()
        self.step_number = 0
    def step(self):

        new_members = self.__crossover_and_mutation()
        self.population += new_members
        
        cost_list = list(map(lambda dna: self.__evaluate_cost_dna(dna),self.population))
        fitness_list = self.__get_fitness_values(cost_list)


        population_fitness = list(zip(self.population, fitness_list, cost_list))
        
        sorted_population = sorted(population_fitness, key=lambda x: x[1], reverse=True)
        
        most_probable_populations = [pop[0] for pop in sorted_population[:self.population_number]]
        
        mpp_cost_list = [pop[2] for pop in sorted_population[:self.population_number]]

        self.population = most_probable_populations


        self.step_number+=1
        
        return most_probable_populations, mpp_cost_list

    
    def __generate_dict_cost(self):
        
        nodes_weights = {node:{} for node in self.nodes_list}
        for edge in self.edges_w_list:
            nodes_weights[edge[0]][edge[1]] = edge[2]
            nodes_weights[edge[1]][edge[0]] = edge[2]

        
        #print("Edges paths")
        #display(pd.DataFrame(nodes_weights).sort_index())
        return nodes_weights


    def __get_random_dnas(self):
        stacks=[]
        for x in range(self.population_number):
            dna = []
            for _ in range(len(self.nodes_list)):
                dna.append(random.choice(list(set(self.nodes_list)-set(dna))))
            stacks.append(dna)
        return stacks


    def generate_sequential_pairs(self, dna):
        if len(dna) < 2:
            return []
        
        return [(dna[i], dna[i+1]) for i in range(len(dna) - 1)]+[(dna[-1], dna[0])]
        
    def __evaluate_cost_dna(self, dna):
        paths = self.generate_sequential_pairs(dna)
        
        cost = sum(list(map(lambda pair: self.nodes_weights[pair[0]][pair[1]], paths)))
        del paths
        return cost

    def __get_fitness_values(self, cost_list):
        # Normalize costs to the range [0, 1]
        min_cost = min(cost_list)
        max_cost = max(cost_list)

        if min_cost == max_cost:
            # All elements has same cost
            normalized_costs = [0.0 for cost in cost_list]
        else:
            normalized_costs = [(cost - min_cost) / (max_cost - min_cost) for cost in cost_list]
        
        probabilities = [(1 - norm) for norm in normalized_costs]
        
        probabilities_sum = sum(probabilities)
        normalized_probabilities = [p / probabilities_sum for p in probabilities]

        exploration_idxs = random.sample(range(len(normalized_probabilities)), k=int(self.exploration_prob*len(normalized_probabilities)))

        # Forcing to preserve the element
        for idx in exploration_idxs:
            normalized_probabilities[idx] = 1
        
    
        return normalized_probabilities


    def __mutation(self, dna):
        """
            We evaluated the
            mutual exchange mutation in this survey, which
            randomly chooses two nodes and exchanges them.
        """
        a,b = random.sample(list(range(len(dna))), k=2)
        aux = dna[a]
        dna[a] = dna[b]
        dna[b] = aux
    
        return dna
        
    def __tradditional_crossover(self, dna_a, dna_b, crossover_thd = None):
        """
            crossover_thd is None then len(dna_a)//2
        """
        if crossover_thd is None:
            crossover_thd = len(dna_a)//2
        
        child_a = dna_a[:crossover_thd]
        child_b = dna_b[:crossover_thd]
    
        child_a = child_a+[node for node in dna_b if node not in child_a]
        child_b = child_b+[node for node in dna_a if node not in child_b]
    
        return child_a, child_b

    def __crossover_and_mutation(self):
        new_members = []
        mutation_thd = self.mutation_thd
        
        for dna_a, dna_b in list(permutations(
                                    random.sample(self.population, k=int(len(self.population)*self.crossover_proportion)),
                                    2
                                )
                            ):
            children_list = list(self.__tradditional_crossover(dna_a, dna_b))
            for idx, children in enumerate(children_list):
                # Verify mutation
                if random.uniform(0,1) <= mutation_thd:
                    children_list[idx] = self.__mutation(children)
                    
            new_members = new_members+children_list
        return new_members