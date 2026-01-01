class employee:
    def __init__(self,name):
        self.name=name

    def work(self):
        print(f"{self.name} is working")

class developer(employee):
    def __init__(self,name,language):
        super().__init__(name)
        self.language=language

    def code(self):
        print(f"{self.name} is coding in {self.language}")

s=developer("harish","python")
s.work()
s.code()