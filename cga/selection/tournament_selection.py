from typing import List
from individual import Individual
import numpy as np
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class TournamentSelection:
    def __init__(self, pop_list: List[Individual] = {}, c: int = 0, K: int = 2):
        self.pop_list = pop_list
        self.c = c
        self.K = K  # How many people will be chosen at random from neighbors

    def get_parents(self) -> List[Individual]:
        parents = []
        p1 = self.pop_list[self.c - 1]

        parents.append(p1)
        neighbors_positions = p1.neighbors_positions
        neighbors = []

        for i in range(len(self.pop_list)):
            if self.pop_list[i].position in neighbors_positions:
                neighbors.append(self.pop_list[i])

        tournament_selection_pool = []

        while len(tournament_selection_pool) < self.K:

            index = np.random.randint(0, len(neighbors))

            if neighbors[index] not in tournament_selection_pool:
                tournament_selection_pool.append(neighbors[index])
            else:
                pass

        tournament_selection_pool_ordered = sorted(
            tournament_selection_pool, key=lambda x: x.fitness_value, reverse=True
        )
        p2 = tournament_selection_pool_ordered[0]
        parents.append(p2)

        return parents
