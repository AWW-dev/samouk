#1
print("pierwsza runda")
print("druga runda")
print("trzecia runda")

#2
x = 5
if x > 10:
    print("x jest mniejsza niz 10")
else:
    print("x jest rowna lub wieszka niz 10")

#3
a = 13
if a >= 10:
    print("a jest mniejsza lub rowna 10")

if 10 > a >= 25:
    print("a jest wieksza od 10 ale mniejsza lub rowna 25")

if a > 25:
    print("a jest wieksze od 25")

#4
a = 10
b = 3
c = a%b
print(c)

#5
d = 10
e = 2
f = d/e
print(f)

#6
age = 17
drive = 18-age
if drive <2:
    print("nie dlugo bedziesz mogl jezdzic")
else:
    print("jeszcze sporo brakuje do zrobienia prawa jazdy")