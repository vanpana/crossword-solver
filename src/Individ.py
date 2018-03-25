from random import shuffle


class Individ:
    def __init__(self, noWords):
        self.data = [x for x in range(noWords)]
        shuffle(self.data)

    def fitness(self):
        pass  # TODO: return float

    def mutate(self, probability):
        pass  # TODO: return mutated

    def crossover(self, other, probability):
        pass  # TODO: return crossedover
