from random import randint

from Problem import Problem


class Algorithm:
    def __init__(self, noIterations, filename):
        self.filename = filename
        self.problem = self.read_file()
        self.population = None
        self.noIterations = noIterations

    def read_file(self):
        return Problem(self.filename)

    def iteration(self):
        i1 = randint(0, len(self.population) - 1)
        i2 = randint(0, len(self.population) - 1)

        if i1 != i2:
            child = self.population[i1].crossover(self.population[i2]).mutate()

            f1 = self.population[i1].fitness(self.problem)
            f2 = self.population[i2].fitness(self.problem)
            fc = child.fitness(self.problem)

            perfect_fitness = len(self.problem.words) + len(self.problem.location)

            if fc == perfect_fitness:
                return child

            if f1 > f2 and f1 > fc:
                self.population[i1] = child
            if f2 > f1 and f2 > fc:
                self.population[i2] = child

            child.print(self.problem)

    def run(self):
        for _ in range(self.noIterations):
            child = self.iteration()

            if child is not None:
                return child

    def statistics(self):
        pass  # TODO
