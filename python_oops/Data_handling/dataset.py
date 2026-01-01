import numpy as np

class Dataset:
    def __init__(self, ds):

        self.ds = np.array(ds)

    def display(self):
        print("Dataset:")
        print(self.ds)

    def sum(self):
        return self.ds.sum()

    def mean(self):
        return self.ds.mean()

    def shape(self):
        return self.ds.shape

data_list = [[1, 2], [3, 4], [5, 6]]
ds = Dataset(data_list)

ds.display()
print("Sum:", ds.sum())
print("Mean:", ds.mean())
print("Shape:", ds.shape())
