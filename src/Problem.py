class Problem:
    def __init__(self, filename):
        self.matrix = []
        self.location = None  # each item will the starting point and end point of the empty space
        self.words = []
        self.filename = filename

        self.__initialize_data()
        pass

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
                self.matrix.append(line)
            else:
                self.words = [word for word in line]
