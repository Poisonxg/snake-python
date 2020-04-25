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
        self.x = None
        self.y = None

    def distance(self, x, y, fx, fy):
        return math.sqrt((x - fx)**2 + (y - fy)**2)

    def label(self, data):
        data = np.squeeze(data)
        x = data[0]
        y = data[1]
        fx = data[2]
        fy = data[3]
        movement = data[4]
        self.dis = self.distance(x, y, fx, fy)
        self.disNU = self.distance(x, y - 9, fx, fy)
        self.disND = self.distance(x, y + 9, fx, fy)
        self.disNL = self.distance(x - 9, y, fx, fy)
        self.disNR = self.distance(x + 9, y, fx, fy)
        self.minim = [self.disNU, self.disND, self.disNL, self.disNR]
        mini = min(self.minim)
        self.x = x
        self.y = y
        return self.logic(mini, movement)

    def logic(self, mini, movement):
        if self.y <= 9:
            if movement == 0:
                return 3

            elif mini is self.disNU:
                if movement is not 1:
                    return 1
            elif mini == self.disND:
                if movement is not 0:
                    return 2
            elif mini == self.disNL:
                if movement is not 3:
                    return 3
            elif mini == self.disNR:
                if movement is not 2:
                    return 4
        if self.y >= 432:
            if movement == 1:
                return 4

            elif mini is self.disNU:
                if movement is not 1:
                    return 1
            elif mini == self.disND:
                if movement is not 0:
                    return 2
            elif mini == self.disNL:
                if movement is not 3:
                    return 3
            elif mini == self.disNR:
                if movement is not 2:
                    return 4
        if self.x >= 430:
            if movement == 3:
                return 1

            elif mini is self.disNU:
                if movement is not 1:
                    return 1
            elif mini == self.disND:
                if movement is not 0:
                    return 2
            elif mini == self.disNL:
                if movement is not 3:
                    return 3
            elif mini == self.disNR:
                if movement is not 2:
                    return 4

        if self.x <= 9:
            if movement == 2:
                return 2

            elif mini is self.disNU:
                if movement is not 1:
                    return 1
            elif mini == self.disND:
                if movement is not 0:
                    return 2
            elif mini == self.disNL:
                if movement is not 3:
                    return 3
            elif mini == self.disNR:
                if movement is not 2:
                    return 4

        elif mini is self.disNU:
            if movement is not 1:
                return 1
        elif mini == self.disND:
            if movement is not 0:
                return 2
        elif mini == self.disNL:
            if movement is not 3:
                return 3
        elif mini == self.disNR:
            if movement is not 2:
                return 4


# Data Augmentation for a ANN.
if __name__ == '__main__':
    features = 9 * np.random.randint(low=1, high=48, size=(2000, 4))
    movements = np.random.randint(low=0, high=4, size=(2000, 1))
    labels = []
    features = np.concatenate((features, movements), axis=1)
    AI = Logic()
    for i in range(0, 2000):
        if AI.label(features[i, :]) == None:
            print(features[i, :])
        labels.append(AI.label(features[i, :]))

    labels = np.array(labels)
    import h5py

    with h5py.File('data.h5', 'w') as f:
        f.create_dataset("features", data=features, dtype="float")
        f.create_dataset("labels", data=labels, dtype="float")
