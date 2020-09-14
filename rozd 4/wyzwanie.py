def a(x):
    """
    funkcja zwraca x podniesiony do kwadratu
    :param x: int
    :return: int kwadrat x
    """
    x = int(x)
    x = x**2
    print(x)


a(10)

def tekst(z):
    """
    funkcja wypisuje podany string
    :param z: string
    :return: string z
    """
    print(z)

tekst("to jest string")

def sum(q, w, e=10):
    """
    suma q, w i e
    :param q: int
    :param w: int
    :param e: int parametr opcjonalny
    :return: int, suma q w i e
    """
    q = int(q)
    w = int(w)
    e = int(e)
    print(q+w+e)

sum(2,3)

def one(h):
    """
    pobiera h a wynikem jej jest dzielenia przez dwa
    :param h: int
    :return: int h/2
    """
    return h/2

def two(h):
    """
    pobiera h i daje wynik mnozenia razy 4
    :param h: int
    :return: int
    """
    return h * 4

j=one(6)
g=two(j)

print(g)

def flo(f):
    """
    konweruje string na float
    :param f: str
    :return: float
    """
    try:
        f=float(f)
        print(f)
    except(ZeroDivisionError, ValueError):
        print("zle dane wejsciowe")

flo("100")
