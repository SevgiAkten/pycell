from Individual import *
from Grid import *
from Neighborhoods.Linear5 import *
from Problems.abstractproblem import AbstractProblem

class Population:
    def __init__(self, ch_size, n_rows, n_cols, gen_type, problem: AbstractProblem):
        self.ch_size = ch_size
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.gen_type = gen_type
        self.problem = problem

    def InitialPopulation(self):

        pop_size = self.n_rows * self.n_cols
        pop_list = []

        grid = Grid(self.n_rows, self.n_cols).make2DGrid()

        for i in range(pop_size):
            ind = Individual(gen_type=self.gen_type, ch_size=self.ch_size)
            ind.chromosome = ind.setChromosome()
            ind.position = grid[i]
            ind.fitness_value = self.problem.f(ind.chromosome)
            ind.neighbors_positions = Linear5(
                position=ind.position, n_rows=self.n_rows, n_cols=self.n_cols
            ).calculateNeighborsPositions()
            ind.neighbors = None
            pop_list.append(ind)

        return pop_list
