class Individ:
    def __init__(self, size, x):
        self.size = size
        self.x = x

    def fitness(self):
        pass  # TODO: return float

    def mutate(self, probability):
        pass  # TODO: return mutated

    def crossover(self, other, probability):
        pass  # TODO: return crossedover
