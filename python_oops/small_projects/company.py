class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"Employee {self.name} is working with salary {self.salary}")

class Dev(Emp):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language


    def work(self):
        print(f"Developer {self.name} is coding in {self.language} and has salary {self.salary}")

class Manager(Emp):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


    def work(self):
        print(f"Manager {self.name} is managing a team of {self.team_size}")

dev1 = Dev("Harish", 100000, "Python")
mgr1 = Manager("Rahul", 50000, 8)


dev1.work()
mgr1.work()
