# import os
#
# with open(os.path.join("Users",
#                         "python",
#                         "desktop",
#                         "tekst.odt"), "r")as f:
#     print(f.read())

# anw = input("podaj swoj numer buta ")
# with open("buty.odt", "w") as f:
#     f.write(anw)


import csv

filmy = [["top gun", "ocean's eleve", "raport mniejszosci"],["titanic", "ostatni jedi", "incepcja"],["pulp fiction", "czlowiek w ogniu", "seksmisja"]]
with open("filmy.csv", "w") as csvfile:
    tytuly = csv.writer(csvfile, delimiter =",")
    for lista_filmow in filmy:
        tytuly.writerow(lista_filmow)