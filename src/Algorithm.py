import copy
from random import randint, shuffle

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

        # self.population = [x[0] for x in sorted(
        #     [(self.population[i], self.population[i].fitness(self.problem)) for i in range(len(self.population))],
        #     key=lambda x: x[1], reverse=True)]

        i1, i2 = self.get_two()

        if i1 != i2:
            child = self.population[i1].crossover(self.population[i2]).mutate()

            f1 = self.population[i1].fitness(self.problem)
            f2 = self.population[i2].fitness(self.problem)
            fc = child.fitness(self.problem)

            if fc == self.perfect_fitness:
                return child

            if fc >= f1 >= f2:
                self.population[i1] = child
            if fc >= f2 >= f1:
                self.population[i2] = child

            # if child != self.population[i1] and child != self.population[i2] and (fc >= f1 or fc >= f2):
            # if fc != 0:
            #     self.population[-1] = child
            print(child.data, fc)
            # if fc > f1 > f2:
            #     self.population[i1] = child
            # if fc > f2 > f1:
            #     self.population[i2] = child

    def get_two(self):
        podium = [(self.population[x], x) for x in range(len(self.population))]

        for i in range(len(podium)):
            shuffle(podium)

        podium = podium[0:len(podium) // 3 + 1]
        podium = [x[0] for x in sorted(
            [(podium[i], podium[i][0].fitness(self.problem)) for i in range(len(podium))],
            key=lambda x: x[1], reverse=True)]

        return podium[0][1], podium[1][1]


    def run(self):
        for _ in range(self.noIterations):
            child = self.iteration()

            if child is not None:
                return child

    def statistics(self):
        pass  # TODO
