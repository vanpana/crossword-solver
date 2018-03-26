from random import randint

from Problem import Problem


class Algorithm:
    def __init__(self, noIterations, filename):
        self.filename = filename
        self.problem = self.read_file()
        self.population = None
        self.noIterations = noIterations
        self.perfect_fitness = -1

    def read_file(self):
        return Problem(self.filename)

    def iteration(self):
        self.population = [x[0] for x in sorted(
            [(self.population[i], self.population[i].fitness(self.problem)) for i in range(len(self.population))],
            key=lambda x: x[1], reverse=True)]

        i1 = 0
        i2 = 1

        if i1 != i2:
            child = self.population[i1].crossover(self.population[i2]).mutate()

            f1 = self.population[i1].fitness(self.problem)
            f2 = self.population[i2].fitness(self.problem)
            fc = child.fitness(self.problem)

            if fc == self.perfect_fitness:
                return child

            # if child != self.population[i1] and child != self.population[i2] and (fc >= f1 or fc >= f2):
            if fc != 0:
                self.population[-1] = child
                print(child.data, fc)
            # if fc > f1 > f2:
            #     self.population[i1] = child
            # if fc > f2 > f1:
            #     self.population[i2] = child



    def run(self):
        for _ in range(self.noIterations):
            child = self.iteration()

            if child is not None:
                return child

    def statistics(self):
        pass  # TODO
