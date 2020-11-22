# class Rectangle():
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l
#
#     def calculate_permiter(self):
#         return self.width *2 + self.len *2
#
# class Square():
#     def __init__(self, s):
#         self.side = s
#
#     def calculate_permiter(self):
#         return self.side *4
#
# a_ractangle = Rectangle(10, 20)
# a_square = Square(10)
#
# print(a_ractangle.calculate_permiter())
# print(a_square.calculate_permiter())


# class Square():
#     def __init__(self, s):
#         self.side = s
#
#     def calculate_permiter(self):
#         return self.side * 4
#
#     def change_size(self, new_size):
#         self.side += new_size
#
# a_square = Square(20)
# print(a_square.side)
#
# a_square.change_size(20)
# print(a_square.side)


# class Shape():
#     def what_am_i(self):
#         print("Jestem figura")
#
# class Rectangle(Shape):
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l
#
#     def calculate_permiter(self):
#         return self.width *2 + self.len *2
#
# class Square(Shape):
#     def __init__(self, s):
#         self.side = s
#
#     def calculate_permiter(self):
#         return self.side *4
#
# a_rectangel =  Rectangle(10,20)
# a_square = Square(10)
#
# a_rectangel.what_am_i()
# a_square.what_am_i()

class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

kon = Horse("rafal")
jezdziec = Rider("egzorcysta", kon)

print(jezdziec.horse.name)