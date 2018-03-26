from Algorithm import Algorithm
from Individ import Individ

# ans day: 2 3 1 6 0 5 4
if __name__ == '__main__':
    algorithm = Algorithm(999999999, "../data/days.crossword")
    # algorithm = Algorithm(999999999, "../data/first.crossword")

    probability = 0.01
    algorithm.population = [Individ(len(algorithm.problem.words)) for _ in range(10)]
    algorithm.perfect_fitness = sum([len(x) for x in algorithm.problem.words])

    solution = algorithm.run()

    for element in solution.data:
        print(element)
