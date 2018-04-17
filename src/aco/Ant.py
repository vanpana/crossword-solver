import copy
from random import randint, random, choice, shuffle


class Ant:
    def __init__(self, words):
        self.size = len(words)
        self.words_indices = [i for i in range(self.size)]
        shuffle(self.words_indices)
        self.path = [self.pop_random_word()]

    def pop_random_word(self):
        if len(self.words_indices):
            rand = randint(0, len(self.words_indices) - 1)
            return self.words_indices.pop(rand)

    def pop_word(self, indice):
        print("POPPING: " + str(indice))
        counter = 0
        for w_indice in self.words_indices:
            if w_indice == indice:
                return self.words_indices.pop(counter)
            else:
                counter += 1

    def distance_move(self, word_indice, problem):
        target_location = problem.location[len(self.path)]

        empty_length = target_location[0].distance(target_location[1])
        word_length = len(problem.words[word_indice])

        return abs(empty_length - word_length)

    def add_move(self, problem, q0, trace, alpha, beta):
        p = [0 for _ in range(self.size)]

        next_steps = self.words_indices.copy()

        if len(next_steps) == 0:
            return False

        for i in next_steps:
            p[i] = self.distance_move(i, problem)

        p = [(p[i] ** beta) * (trace[self.path[-1]][i] ** alpha) for i in range(len(p))]

        print("NEXT STEPS: " + str(next_steps))

        if random() < q0:
            print("RANDOMIZED")
            p = [[i, p[i]] for i in next_steps]
            p = min(p, key=lambda a: a[1])
            self.path.append(self.pop_word(p[0]))
        else:
            print("SUMMING")
            s = sum(p)
            if s == 0:
                return choice(next_steps)
            p = [p[i] / s for i in range(len(p))]
            p = [sum(p[0:i + 1]) for i in range(len(p))]
            r = random()
            i = 0
            while r > p[i]:
                i += 1

            self.path.append(self.pop_word(i))
        return True

    def fitness(self, problem):
        points = 0
        counter = 0

        # This is for days debug
        if self.path == [2, 3, 1, 6, 0, 5, 4]:
            print("ok")

        for location in problem.location:
            if counter > len(self.path) - 1:
                break

            empty_length = location[0].distance(location[1])
            word_length = len(problem.words[self.path[counter]])

            if empty_length == word_length:
                points += word_length

            counter += 1

        if points == sum([len(x) for x in problem.words]):
            for i in range(len(problem.location) - 1):
                for j in range(i + 1, len(problem.location)):

                    for coordinate in problem.location[i][0].get_points_in_between(problem.location[i][1]):
                        if coordinate.between(problem.location[j][0], problem.location[j][1]):

                            x = coordinate.y - problem.location[i][0].y
                            y = coordinate.x - problem.location[j][0].x

                            if problem.words[self.path[i]][x] == problem.words[self.path[j]][y]:
                                points += 1

        return points

    def __str__(self):
        return str(self.path)

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return copy.deepcopy(self)
