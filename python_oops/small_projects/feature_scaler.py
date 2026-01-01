import numpy as np
class FeatureScaler:
    def __init__(self,data):
        self.data = np.array(data)

    def min_max(self):
        min_x =self.data.min(axis=0)
        max_x =self.data.max(axis=0)
        scaled=self.data-min_x/max_x-min_x
        print(scaled)

    def standardize(self):
        std=self.data.std()
        mean=self.data.mean()
        standardized=self.data-mean/std
        print(standardized)

    def summary(self):
        print(self.data.shape)
        print(self.data.mean(axis=0))
        print(self.data.std(axis=0))
data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

s=FeatureScaler(data)
s.summary()
s.min_max()
s.standardize()
