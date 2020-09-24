for i in range(1, 11):
    print(i)

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Szczęśliwego Nowego Roku!")

for i in range(0, 100):
    print(i)

for i in range(0, 100):
    print(i)
    break

qs = ['Jak masz na imie?',
      'Jaki jest Twoj ulubiony kolor?',
      'Jakie masz zadanie?']

n = 0
while True:
    print("Wpisz q zeby zakonczyc")
    a = input(qs[n])
    if a == 'q':
        break
    n = (n+1) % 3

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
