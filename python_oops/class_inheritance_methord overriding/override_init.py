class emp:
    def __init__(self,name):
        self.name=name

    def work(self):
        print(f"employee {self.name} is working")

class dev(emp):
    def __init__(self,name,language):
        super().__init__(name)
        self.language=language

    def work(self):
        print(f"developer {self.name} is working in {self.language}")

s=dev("harish","python")
s.work()


