class Rectangel():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l


rectangel = Rectangel(10,20)
print(rectangel.area())
rectangel.change_size(20,40)
print(rectangel.area())