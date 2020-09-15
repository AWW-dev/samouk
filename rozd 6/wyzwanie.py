a = "Camus"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

b = input("co wczoraj napisales? ")
c = input("do kogo to wyslales? ")
d = """Wczoraj napisalem {} i wyslalem do {}""".format(b, c)
print(d)

print("aldous Hauxley rodzil sie w 1894 roku".capitalize())

list = ["Zwinny","lis","przeskoczyl","nad","leniwym","psem","."]
list = " ".join(list)
list = list[0:-2] + "."
print(list)

s = "W czasie suszy szosa sucha".replace('s', '$')
print(s)

print("Hemingway".index('m'))

print("Czyz jest kro na swiecie co naprawde sadzil, ze bylo tylu \"Amadsow\".")
print("trzy "+"trzy "+"trzy ")
print("trzy "*3)

print("Dlugo ma szturm i szaniec podgladal w milczeniu. Na koniec szekl: 'Stracona'.".index("."))
print("Dlugo ma szturm i szaniec podgladal w milczeniu. Na koniec szekl: 'Stracona'."[:49])
