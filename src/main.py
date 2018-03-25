from Algorithm import Algorithm
from Individ import Individ

if __name__ == '__main__':
    algorithm = Algorithm(999999999, "../data/first.crossword")

    probability = 0.01
    algorithm.population = [Individ(len(algorithm.problem.words)) for _ in range(10)]

    solution = algorithm.run()

    for element in solution.data:
        print(element)
