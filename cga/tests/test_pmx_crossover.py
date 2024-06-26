from problems.single_objective.discrete.permutation.tsp import Tsp
from recombination.pmx_crossover import PMXCrossover
from individual import Individual
import random


def test_pmx_crossover():

    CHSIZE = 52

    indv1 = Individual(gen_type="Permutation", ch_size=CHSIZE)
    indv2 = Individual(gen_type="Permutation", ch_size=CHSIZE)

    p1 = list(random.sample(range(1, 53), 52))
    p2 = list(random.sample(range(1, 53), 52))

    indv1.chromosome = p1
    indv2.chromosome = p2
    parents = [indv1, indv2]

    theproblem = Tsp()

    ucx = PMXCrossover(parents, theproblem)
    child1, child2 = ucx.get_recombinations()

    assert child1.ch_size == child2.ch_size
    assert child1.ch_size == CHSIZE
