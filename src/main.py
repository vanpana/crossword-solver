import numpy

from Algorithm import Algorithm
from Individ import Individ

def get_fitness(problem):
    problem = problem
    fitness = sum([len(x) for x in problem.words])

    for i in range(len(problem.location) - 1):
        for j in range(i + 1, len(problem.location)):

            for coordinate in problem.location[i][0].get_points_in_between(problem.location[i][1]):
                if coordinate.between(problem.location[j][0], problem.location[j][1]):
                    fitness += 1

    return fitness

# ans day: 2 3 1 6 0 5 4
if __name__ == '__main__':
    repetition = 30
    most_fit = []

    for rep in range(repetition):
        print("======================={0}=======================".format(rep))
        # algorithm = Algorithm(999999999, "../data/days.crossword")
        algorithm = Algorithm(2500, "../data/first.crossword")
        # algorithm = Algorithm(2500, "../data/random.crossword")

        probability = 0.01
        algorithm.population = [Individ(len(algorithm.problem.words)) for _ in range(40)]
        algorithm.perfect_fitness = get_fitness(algorithm.problem)

        solution = algorithm.run()

        most_fit.append(algorithm.most_fit)

        if solution is not None:
            for element in solution.data:
                print(element)

    print(most_fit)

    print(numpy.std(most_fit))



