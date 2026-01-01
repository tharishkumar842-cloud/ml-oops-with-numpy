import numpy as np

class DatasetHandler:
    def __init__(self,data):
        self.data = data
    def get_rows(self):
        return self.data.shape[0]
    def get_columns(self):
        return self.data.shape[1]
    def get_mean(self):
        return self.data.mean(axis=0)
    def get_max(self):
        return self.data.max(axis=0)
    def get_min(self):
        return self.data.min(axis=0)


data=np.array([[1,2,3],[4,5,6]])
obj = DatasetHandler(data)

print("Rows:", obj.get_rows())
print("Columns:", obj.get_columns())
print("Mean:", obj.get_mean())
print("Max:", obj.get_max())

