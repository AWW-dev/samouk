from math import pi

# class Apple():
#     def __init__(self, s, w, c, t):
#         self.size = s
#         self.weight = w
#         self.color = c
#         self.taste = t
#
#     def __str__(self):
#         return f"Dane jabłko ma rozmiar{self.size}, waży {self.weight} gramów, ma {self.color} kolor i {self.taste} smak!"
#
#
# antownoka = Apple("m", 100, "żółty", "słodki")
# print(antownoka)


# class Circe():
#     def __init__(self,r):
#         self.radius = r
#
#     def area(self):
#         return self.radius * pi
#
# circle = Circe(3)
# print(circle.area(3))

# class Triangel():
#     def __init__(self, s, h):
#         self.side = s
#         self.height = h
#
#     def area(self):
#         return self.side * self.height / 2
#
# triangle = Triangel(3,4)
# print(triangle.area())

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon= Hexagon(1,2,3,4,5,6)
print(hexagon.perimeter())