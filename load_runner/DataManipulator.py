import glob


class DataManipulator():
    def __init__(self, data="all"):
        self.width = 33
        self.height = 22
        self.levels_raw = glob.glob("data_all/*.txt")
        self.levels_count = len(self.levels_raw)

    def get(self, count, thickness, direction):
        data = []
        if (direction == "row"):
            for level in self.levels_raw:
                with open(level) as txt:
                    for line in txt:
                        for char in line:
                            if (char != '\n'):
                                a = txt

        if (direction == "column"):
            pass

    def getAll(self):
        self.get(self.levels_count, 0, "row")
