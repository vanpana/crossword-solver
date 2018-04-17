from random import  shuffle
from matplotlib import pyplot


from Problem import Problem


class Algorithm:
    def __init__(self, noIterations, filename):
        self.filename = filename
        self.problem = self.read_file()
        self.population = None
        self.noIterations = noIterations
        self.perfect_fitness = -1
        self.most_fit = 0

    def read_file(self):
        return Problem(self.filename)

    def iteration(self):

        temp = [x[1] for x in
                [(self.population[i], self.population[i].fitness(self.problem)) for i in range(len(self.population))]]

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

            if f1 > self.most_fit:
                self.most_fit = f1
            elif f2 > self.most_fit:
                self.most_fit = f2
            elif fc > self.most_fit:
                self.most_fit = fc

            print(child.data, fc)

            return sum(temp) / len(self.population)

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
        fitness_avg = []
        for counter in range(self.noIterations):
            child = self.iteration()

            if child is not None and (type(child) != float and type(child) != int):
                self.plot(counter, fitness_avg)
                return child

            fitness_avg.append(child)

        self.plot(self.noIterations, fitness_avg)



    def plot(self, steps, avg):
        pyplot.plot(range(len(avg)), avg)
        pyplot.axis([0, steps, min(avg), max(avg)])
        pyplot.show()

    def statistics(self):
        pass  # TODO
