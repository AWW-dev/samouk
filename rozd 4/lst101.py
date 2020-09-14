def even_odd(x):
    if x % 2 == 0:
        print('parzysta')
    else:
        print('nieparzysta')


even_odd(2)
even_odd(3)


def even():
    n = input("podaj liczbę: ")
    n = int(n)
    if n % 2 == 0:
        print("to liczba parzysta")
    else:
        print("to liczba nieparzysta")


even()


# even()
# even()
# even()
# even()

def f(x=2):
    return x ** x


print(f())
print(f(4))


def add_it(z, y=10):
    return z + y


result = add_it(2)
print(result)
