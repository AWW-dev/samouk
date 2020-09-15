fruit = ['truskawka','banan','mango']
print(fruit)
fruit.append('pomelo')
fruit.append('mango')
print(fruit)
print(fruit[0])
print(fruit[3])
print(fruit[2])
fruit[2] = 'borowka'
print(fruit)
fruit2 = ['ananas', 'daktyl', 'gruszka']

owoce=fruit + fruit2
print(owoce)
print(len(owoce))

guess = input("zgadnij jaki owoc jest w koszyku? ")

if guess in owoce:
    print("zgadles")
else:
    print("nie trafiles")
