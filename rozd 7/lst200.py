name = "Ted"
for character in name:
    print(character)

shows = ["Jaka to melodia",
         "Kolo fortuny",
         "Familiada"]
for show in shows:
    print(show)

coms = ("Programowanie",
        "Znajomi",
        "Chillout")
for com in coms:
    print(com)


people = {"Fowler": "Wzroce projektowe",
          "Knuth": "Algorytmy",
          "Stroustrup": "C++"}

for n in people:
    print(n)

tv = ["Wiadomości", "Fakty", "Informacje"]
i = 0
for o in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

tv = ["Wiadomości", "Fakty", "Informacje"]
for i, o in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)


news = ["Jaka to melodia",
         "Kolo fortuny",
         "Familiada"]
tv = ["Wiadomości", "Fakty", "Informacje"]

all_show = []

for show in news:
    show = show.upper()
    all_show.append(show)

for show in tv:
    show = show.upper()
    all_show.append(show)

print(all_show)