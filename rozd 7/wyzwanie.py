movies = ["Noc zywych trupow", "Ekipa", "Rodzina Soprano", "Pamietniki wampirow"]
for movie in movies:
    print(movie)

for i in range(25, 51):
    print(i)

for index, movie in enumerate(movies):
    print(index)
    print(movie)

list = [1, 2, 3, 4, 5]
while True:
    print("Wpisz q aby zakonczyc")
    a = input("zgadnij cyfre ")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("wpisz liczbe")
    if a in list:
        print("zgadles")
    if a not in list:
        print(" probuj dalej")


list1 = [8, 19, 148, 4]
list2 = [9, 1, 22, 83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)