from Point import Point


class Problem:
    def __init__(self, filename):
        self.matrix = []
        self.location = []  # each item will the starting point and end point of the empty space
        self.words = []
        self.filename = filename

        self.__initialize_data()

    def __read_from_file(self):
        with open(self.filename, "r") as file:
            for line in file:
                yield line.strip("\n")

    def __initialize_data(self):
        k = 0
        for line in self.__read_from_file():
            line = line.split(" ")
            if len(line) == 1:
                k = int(line[0])
            elif len(line) == k:
                self.matrix.append([0 if element == '0' else '#' for element in line])
            else:
                self.words = [word for word in line]

        self.location.extend(self.__fill_location_horizontal())
        self.location.extend(self.__fill_location_vertical())

    def __fill_location_horizontal(self):
        location = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if len(location) == 0:
                    process = True
                else:
                    process = not Point(i, j).between(location[-1][0], location[-1][1])

                if self.matrix[i][j] == 0 and process:
                    offset = 0
                    while self.matrix[i][j + offset] == 0 and j + offset < len(self.matrix):
                        offset += 1
                        if j + offset == len(self.matrix):
                            break

                    if offset != 1:
                        offset -= 1
                        location.append((Point(i, j), Point(i, j + offset)))

                    if j + offset + 1 == len(self.matrix):
                        break
        return location

    def __fill_location_vertical(self):
        location = []
        for j in range(len(self.matrix)):
            for i in range(len(self.matrix)):
                if len(location) == 0:
                    process = True
                else:
                    process = not Point(i, j).between(location[-1][0], location[-1][1])

                if self.matrix[i][j] == 0 and process:
                    offset = 0
                    while self.matrix[i + offset][j] == 0 and i + offset < len(self.matrix):
                        offset += 1
                        if i + offset == len(self.matrix):
                            break

                    if offset != 1:
                        offset -= 1
                        location.append((Point(i, j), Point(i + offset, j)))

                    if i + offset + 1 == len(self.matrix):
                        break
        return location
