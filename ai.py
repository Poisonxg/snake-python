import random
import math
import json
import itertools
import numpy as np


class Logic(object):
    """docstring for Logic"""

    def __init__(self):
        super(Logic, self).__init__()
        self.dis = None
        self.disNU = None
        self.disND = None
        self.disNL = None
        self.disNR = None
        self.minim = None

    def distance(self, x, y, fx, fy):
        return math.sqrt((x - fx)**2 + (y - fy)**2)

    def label(self, x, y, fx, fy, movement):
        self.dis = self.distance(x, y, fx, fy)
        self.disNU = self.distance(x, y - 9, fx, fy)
        self.disND = self.distance(x, y + 9, fx, fy)
        self.disNL = self.distance(x - 9, y, fx, fy)
        self.disNR = self.distance(x + 9, y, fx, fy)
        self.minim = [self.disNU, self.disND, self.disNL, self.disNR]
        mini = min(self.minim)
        return self.logic(mini, movement)

    def logic(self, mini, movement):
        if mini == self.disNU:
            if movement is not 1:
                return 1
            else:
                return random.randint(3, 4)
        elif mini == self.disND:
            if movement is not 0:
                return 2
            else:
                return random.randint(3, 4)
        elif mini == self.disNL:
            if movement is not 3:
                return 3
            else:
                return random.randint(1, 2)
        elif mini == self.disNR:
            if movement is not 2:
                return 4
            else:
                return random.randint(1, 2)


if __name__ == '__main__':
    features = 9 * np.random.randint(low=1, high=48, size=(20000, 5))
    labels = []
    AI = Logic()
    for i in range(20000):

        labels.append(AI.label(
            features[i][0], features[i][1], features[i][2], features[i][3], features[i][4]))

    with open('features.json', 'w') as f:
        json.dump(features.tolist(), f, indent=2)

    with open('labels.json', 'w') as f:
        json.dump(labels, f, indent=2)
