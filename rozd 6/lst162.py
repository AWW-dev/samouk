author = "Kafka"
print(author[4])
print(author[-2])

a = "kot"
b = "w"
c = "butach"
print(a, b, c)
print(a * 3)

d = "Nie pytaj, komu bije dzwon..."
print(d.upper())

e = "nie wiadomo co to za halasy. pewnie dzieciaki znowu wariuja"
print(e.capitalize())

last = "Faulkner"
print("William {}".format(last))

tworca = "William Fauklner"
data_ur = "1897"
print("""{} urodził się w {} roku""" \
      .format(tworca, data_ur))

marka = input("wpisz marke samochodu ")
model = input("wpisz model samochodu ")
pojemnosc = input("wpisz pojemnosc samochodu ")
paliwo = input("wpisz rodzaj paliwa ")

s = """Twoj samochod jest marki {}, model {}, 
    o pojemnosci {}, napedzany {}""".format(marka,
                                            model,
                                            pojemnosc,
                                            paliwo)

print(s)