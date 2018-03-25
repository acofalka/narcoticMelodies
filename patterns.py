import random

class Patterns:
    def __init__(self):
        self.pattern_list = []
        self.pattern_list.append([0, 2, 0, 2])
        self.pattern_list.append([0, 4, 7, 4])
        self.pattern_list.append([0, 7, 12, 16, 12, 7])
        self.pattern_list.append([0, 4, 2, 5, 4, 7, 7, 4, 5, 2, 4, 0])
        self.pattern_list.append([0, 4, 2, 5, 4, 7, 5, 9, 7, 11, 9, 12])
        self.pattern_list.append([0, 3, 6, 3, 6, 3])
        self.pattern_list.append([3, 0, 5, 0, 6, 0, 5, 0])

    def random_pattern(self):
        pattern_number = random.randint(0, len(self.pattern_list) - 1)
        return self.pattern_list[pattern_number]
