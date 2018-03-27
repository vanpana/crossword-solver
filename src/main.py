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
    # algorithm = Algorithm(999999999, "../data/days.crossword")
    algorithm = Algorithm(20000, "../data/first.crossword")

    probability = 0.01
    algorithm.population = [Individ(len(algorithm.problem.words)) for _ in range(10)]
    algorithm.perfect_fitness = get_fitness(algorithm.problem)

    solution = algorithm.run()

    if solution is not None:
        for element in solution.data:
            print(element)


