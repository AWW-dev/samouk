a = """Hej.Siema!""".split(".")
print(a)

words = ["chodzi",
         "lisek",
         "kolo",
         "drogi",
         "."]
one = " ".join(words)
print(one)

s = "  znaki maja zniknac    "
s=s.strip()
print(s)

zam = "Mam trzy latka, trzy i pol"
zam = zam.replace("r", "%")
print(zam)

try:
    print("imperialny".index("r"))
except:
    print("nie ma takiego znaku")

try:
    print("imperialny".index("z"))
except:
    print("nie ma takiego znaku")


print("kot" in "kot w butach")
print("kat" in "kot w butach")

print("uwielbiam ogladac \"klan\"")
print("uwielbiam ogladac 'klan'")

print("litwo\nojczyzno moja\nty jestes jaka zdrowie")

ivan = """a zyc tak na skraju zguby \
trzeba samotnie"""
print(ivan[0:10])
print(ivan[26:41])
print(ivan[:10])
print(ivan[26:])
print(ivan[:])