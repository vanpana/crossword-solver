from random import shuffle, randint, uniform


class Individ:
    def __init__(self, no_words):
        self.data = [x for x in range(no_words)]
        shuffle(self.data)

    def fitness(self, problem):
        points = 0
        counter = 0

        for location in problem.location:
            empty_length = location[0].distance(location[1])
            word_length = len(problem.words[self.data[counter]])

            if empty_length == word_length:
                points += word_length

            # TODO Check intersections
            counter += 1

        if len(set(self.data)) != len(self.data):
            points = points * -1
        return points

    def mutate(self, probability=0.5):
        # if probability < uniform(0, 1):
        #     return self

        l1 = randint(0, len(self.data) // 2)

        l2 = l1
        while l2 == l1:
            l2 = randint(0, len(self.data) // 2)

        if l2 < l1:
            l1, l2 = l2, l1

        r1 = randint(len(self.data) // 2 + 1, len(self.data))
        r2 = r1

        while r2 == r1:
            r2 = randint(len(self.data) // 2 + 1, len(self.data))

        if r2 < r1:
            r1, r2 = r2, r1

        mutated_data = []
        mutated_data.extend(self.data[:l1])
        mutated_data.extend(self.data[r1:r2])
        mutated_data.extend(self.data[l2:r1])
        mutated_data.extend(self.data[l1:l2])
        mutated_data.extend(self.data[r2:])

        mutant = Individ(len(mutated_data))
        mutant.data = mutated_data
        return mutant

    def crossover(self, other, probability=0.5):
        # if probability < uniform(0, 1):
        #     return self

        left = randint(0, len(self.data) // 2)

        right = left
        while right == left:
            right = randint(len(self.data) // 2, len(self.data) + 1)

        if right < left:
            left, right = right, left

        crossed_over = [None for _ in range(len(self.data))]
        crossed_over[left:right] = self.data[left:right]

        replacement_counter = 0
        for counter in range(len(crossed_over)):
            if crossed_over[counter] is None:
                while other.data[replacement_counter] in crossed_over:
                    replacement_counter += 1
                crossed_over[counter] = other.data[replacement_counter]

        child = Individ(len(crossed_over))
        child.data = crossed_over
        return child

    # def print(self, problem):
    #     for number in self.data:
    #         print(problem.words[number], end=" ")
    #     print()

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)