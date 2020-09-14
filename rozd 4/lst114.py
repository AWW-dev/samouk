try:
    a = input("wpisz liczbe: ")
    b = input("wpisz druga liczbe: ")
    a = int(a)
    b = int(b)
    print(a/b)

except (ZeroDivisionError, ValueError):
    print("bledne dane wejsciowe")