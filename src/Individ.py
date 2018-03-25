from random import shuffle, randint, uniform


class Individ:
    def __init__(self, noWords):
        self.data = [x for x in range(noWords)]
        shuffle(self.data)

    def fitness(self, problem):
        points = 0
        counter = 0

        for location in problem.location:
            empty_length = location[0].distance(location[1])
            word_length = len(problem.words[self.data[counter]])

            if empty_length == word_length:
                points += 1

            # TODO Check intersections
            counter += 1
        return points

    def mutate(self, probability=0.2):
        if probability < uniform(0,1):
            return self

        l1 = randint(0, len(self.data) / 2)

        l2 = l1
        while l2 == l1:
            l2 = randint(0, len(self.data) / 2)

        if l2 < l1:
            l1, l2 = l2, l1

        r1 = randint(len(self.data) / 2 + 1, len(self.data) - 1)
        r2 = r1

        while r2 == r1:
            r2 = randint(len(self.data) / 2 + 1, len(self.data) - 1)

        if r2 < r1:
            r1, r2 = r2, r1

        mutated_data = []
        mutated_data.extend(self.data[:l1])
        mutated_data.extend(self.data[r1:r2])
        mutated_data.extend(self.data[l2:r1])
        mutated_data.extend(self.data[l1:l2])
        mutated_data.extend(self.data[r2:])

        self.data = mutated_data
        return self

    def crossover(self, other, probability=0.2):
        if probability < uniform(0,1):
            return self

        left = randint(0, len(self.data) / 2)

        right = left
        while right == left:
            right = randint(0, len(self.data) / 2)

        if right < left:
            left, right = right, left

        self.data[left:right] = other.data[left:right]
        return self

    def print(self, problem):
        for number in self.data:
            print(problem.words[number], end=" ")
        print()
