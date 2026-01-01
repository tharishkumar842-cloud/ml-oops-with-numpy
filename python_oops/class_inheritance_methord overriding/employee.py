class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name:",self.name,"salary:",self.salary)
s=employee("harish",50000)
s.display()