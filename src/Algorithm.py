from Problem import Problem


class Algorithm:
    def __init__(self, filename):
        self.filename = filename
        self.problem = self.read_file()

    def read_file(self):
        return Problem(self.filename)

    def iteration(self):
        pass  # TODO

    def run(self):
        pass  # TODO

    def statistics(self):
        pass  # TODO
