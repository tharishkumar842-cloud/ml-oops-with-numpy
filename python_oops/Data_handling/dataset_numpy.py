import numpy as np

class Dataset:
    def __init__(self, ds):
        self.data=ds


    def display(self):
        print("Dataset:")
        print(self.data)

    def sum(self):
        return self.data.sum()

    def mean(self):
        return self.data.mean()

    def shape(self):
        return self.data.shape

    def min(self):
        return self.data.min()

    def max(self):
        return self.data.max()

    def row_sum(self):
        return self.data.sum(axis=1)

    def col_sum(self):
        return self.data.sum(axis=0)

data = np.array([[1, 2, 3], [4, 5, 6]])
ds = Dataset(data)

ds.display()
print("Sum:", ds.sum())
print("Mean:", ds.mean())
print("Shape:", ds.shape())
print("Min:", ds.min())
print("Max:", ds.max())
print("Sum of rows:", ds.row_sum())
print("Sum of columns:", ds.col_sum())
