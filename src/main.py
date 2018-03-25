from Algorithm import Algorithm
from Individ import Individ

if __name__ == '__main__':
    algorithm = Algorithm("../data/first.crossword")

    algorithm.population = [Individ(len(algorithm.problem.words)) for _ in range(10)]
