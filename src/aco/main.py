import copy

from aco.Controller import Controller


def get_fitness(problem):
    problem = problem
    fitness = sum([len(x) for x in problem.words])

    for i in range(len(problem.location) - 1):
        for j in range(i + 1, len(problem.location)):

            for coordinate in problem.location[i][0].get_points_in_between(problem.location[i][1]):
                if coordinate.between(problem.location[j][0], problem.location[j][1]):
                    fitness += 1

    return fitness


if __name__ == '__main__':
    no_epoch = 2000
    no_ants = 10
    alpha = 1.9
    beta = 0.9
    rho = 0.05
    q0 = 0.5

    filename = "../../data/days.crossword"

    controller = Controller(no_epoch, filename)
    controller.perfect_fitness = get_fitness(controller.problem)

    sol = None
    best_sol = None
    best_sol_fitness = 0
    trace = [[1 for i in range(len(controller.problem.words))] for j in range(len(controller.problem.words))]

    for i in range(no_epoch):
        sol = controller.epoch(no_ants, controller.problem.words, trace, alpha, beta, q0, rho)

        if best_sol is None:
            best_sol = copy.deepcopy(sol)
        else:
            sol_fitness = sol.fitness(controller.problem)
            if sol_fitness > best_sol_fitness:
                best_sol = copy.deepcopy(sol)
                best_sol_fitness = sol_fitness

    print("Best sol for run is: {0}".format(best_sol))
