from numpy import random
import random as rd


class Individual:
    chromosome = []
    fitness_value = 0
    position = (0, 0)
    neighbors_positions = None
    neighbors = None

    def __init__(self, gen_type="Binary", ch_size=0):
        self.gen_type = gen_type
        self.ch_size = ch_size
        # self.chromosome = rd.sample(range(1, 53), self.ch_size)

    def randomize(self):
        if self.gen_type == "Binary":
            # # CountSat, Fms, Mmdp, OneMax, Ecc, Maxcut20_01, Maxcut20_09, Maxcut100
            self.chromosome = [random.randint(2) for i in range(self.ch_size)]

            # Peak
            # self.chromosome = [[random.randint(2) for g in range(self.ch_size)] for h in range(self.ch_size)]

        elif self.gen_type == "Permutation":
            # # Tsp
            self.chromosome = list(rd.sample(range(1, 15), self.ch_size))
        elif self.gen_type == "Real-valued":
            # # Ackley
            # self.chromosome = [round(rd.uniform(-32.768, 32.768), 3) for i in range(self.ch_size)]

            # # Bohachevsky
            # self.chromosome = [random.randint(-15.0, 16.0)for i in range(self.ch_size)]

            # # Fms
            # self.chromosome = [round(rd.uniform(-6.4, 6.35), 3) for i in range(self.ch_size)]

            # # Griewank
            # self.chromosome = [round(rd.uniform(-600, 600), 3) for i in range(self.ch_size)]
            
            # # Holzman
            # self.chromosome = [round(rd.uniform(-10, 10), 3) for i in range(self.ch_size)]

            # # Rastrigin
            # self.chromosome = [round(rd.uniform(-5.12, 5.13), 2) for i in range(self.ch_size)]

            # # Rosenbrock
            # self.chromosome = [random.randint(-5.0, 11.0) for i in range(self.ch_size)]

            # # Schaffer and Schaffer2
            # self.chromosome = [round(rd.uniform(-100, 100), 3) for i in range(self.ch_size)]

            # # Matyas
            # self.chromosome = [round(rd.uniform(-10, 10), 3) for i in range(self.ch_size)]

            # # Bentcigar
            # self.chromosome = [round(rd.uniform(-100, 100), 3) for i in range(self.ch_size)]

            # # Sumofdifferentpowers
            # self.chromosome = [round(rd.uniform(-10.0, 10.0), 3) for i in range(self.ch_size)]
            
            # # Powell
            # self.chromosome = [round(rd.uniform(-4.0, 5.0), 3) for i in range(self.ch_size)]

            # # Rothellipsoid
            # self.chromosome = [round(rd.uniform(-100, 100), 3) for i in range(self.ch_size)]

            # # Chichinadze
            # self.chromosome = [round(rd.uniform(-30, 30), 5) for i in range(self.ch_size)]

            # # Levy
            # self.chromosome = [round(rd.uniform(-10.0, 10.0), 2) for i in range(self.ch_size)]

            # # Zettle
            # self.chromosome = [round(rd.uniform(-5.0, 5.0), 4) for i in range(self.ch_size)]

            # # Dropwave
            # self.chromosome = [round(rd.uniform(-5.12, 5.12), 3) for i in range(self.ch_size)]

            # # StyblinskiTang
            self.chromosome = [round(rd.uniform(-5.0, 5.0), 6) for i in range(self.ch_size)]
            
            # # Threehumps
            # self.chromosome = [round(rd.uniform(-5.0, 5.0), 3) for i in range(self.ch_size)]

            # # Zakharov
            # self.chromosome = [round(rd.uniform(-5.0, 10.0), 3) for i in range(self.ch_size)]

            # # Schwefel
            # self.chromosome = [round(rd.uniform(-500.0, 500.0), 3) for i in range(self.ch_size)]

            # # Sphere
            # self.chromosome = [round(rd.uniform(-5.12, 5.12), 3) for i in range(self.ch_size)]

            # # Pow
            # self.chromosome = [round(rd.uniform(-5.0, 15.0), 2) for i in range(self.ch_size)]

        else:
            raise NotImplementedError(self.gen_type + " not implemented yet.")
        return self.chromosome

    def generate_candidate(self, vector: list) -> list:
        ind = []
        for p in vector:
            ind.append(
                1) if random.rand() < p else ind.append(0)

        return ind

    def getneighbors_positions(self):
        return self.neighbors_positions

    def setneighbors_positions(self, positions):
        self.neighbors_positions = positions

    def getneighbors(self):
        return self.neighbors

    def setneighbors(self, neighbors):
        #  Copies the argument, not getting the argument itself
        self.neighbors = list(neighbors)
