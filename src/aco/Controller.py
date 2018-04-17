from aco.Ant import Ant
from aco.Problem import Problem


class Controller:
    def __init__(self, no_epoch, filename):
        self.filename = filename
        self.problem = self.read_file()
        self.population = None
        self.noIterations = no_epoch
        self.perfect_fitness = -1
        self.most_fit = 0

    def read_file(self):
        return Problem(self.filename)

    def epoch(self, no_ants, words, trace, alpha, beta, q0, rho):
        ants = [Ant(words) for _ in range(no_ants)]

        for i in range(len(words)):
            for x in ants:
                x.add_move(self.problem, q0, trace, alpha, beta)

        d_trace = [0 if ants[i].fitness(self.problem) == 0 else 1.0 / ants[i].fitness(self.problem) for i in range(len(ants))]
        for i in range(len(words)):
            for j in range(len(words)):
                trace[i][j] = (1 - rho) * trace[i][j]

        for i in range(len(ants)):
            for j in range(len(ants[i].path) - 1):
                x = ants[i].path[j]
                y = ants[i].path[j + 1]
                trace[x][y] += d_trace[i]

        f = [[ants[i].fitness(self.problem), i] for i in range(len(ants))]
        f = max(f)

        # Return the ant
        return ants[f[1]]
