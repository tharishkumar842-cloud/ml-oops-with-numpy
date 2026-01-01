import numpy as np
class scaler:
    def __init__(self,data):
        self.data = np.array(data)

    def display(self):
        print(self.data)

    def min_max_scale(self):
        x_min = self.data.min(axis=0)
        x_max = self.data.max(axis=0)
        scaled = (self.data - x_min) / (x_max - x_min)
        print(scaled)


    def standardize(self):
        mean=self.data.mean()
        std=self.data.std()
        standardized=self.data-mean/std
        print(standardized)



data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

s=scaler(data)
s.display()
s.min_max_scale()
s.standardize()
