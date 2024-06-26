
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

# for binary coded problems


class OnePointCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def get_recombinations(self) -> List[Individual]:

        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]

        co_point = np.random.randint(len(p1.chromosome))

        p1_seg1 = list(p1.chromosome[0:co_point])
        p1_seg2 = list(p1.chromosome[co_point:])

        p2_seg1 = list(p2.chromosome[0:co_point])
        p2_seg2 = list(p2.chromosome[co_point:])

        # First child
        child_1 = Individual()
        new_chromosome_1 = p1_seg1 + p2_seg2
        child_1.chromosome = new_chromosome_1
        child_1.ch_size = len(new_chromosome_1)

        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1.chromosome)
        offsprings.append(child_1)

        # Second child
        child_2 = Individual()
        new_chromosome_2 = p1_seg2 + p2_seg1
        child_2.chromosome = new_chromosome_2
        child_2.ch_size = len(new_chromosome_2)

        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2.chromosome)

        offsprings.append(child_2)

        return offsprings
