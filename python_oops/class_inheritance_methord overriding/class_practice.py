class laptop():
    brand=""
    price=0
    method=""
    def __init__(self,brand,price,method):
        self.brand=brand
        self.price=price
        self.method=method
    def display(self):
        print(self.brand,self.price,self.method)
s=laptop("hp",5000,"ryzen")
s.display()