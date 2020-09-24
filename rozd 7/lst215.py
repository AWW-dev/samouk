for i in range(1, 5):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

while input("t czy n?") != "n":
    for i in range(1, 6):
        print(i)