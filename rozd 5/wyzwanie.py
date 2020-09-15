muzycy = ['gural', 'dezerter', 'analogs', 'hania rein']
print(muzycy)

miejsca = [('16.54.E', '52°23.N',), ('28.16.7.N', '16.36.20.W',)]
print(miejsca)

dane = {
    'wzrost': '189',
    'waga': '85',
    'wiek': '35',
    'ulubiony autor': 'Terry Pratchett'
}
print(dane)

odpowiedz = input('podaj wartosci dla kluczy: wzrost, waga, wiek, ulubiony autor: ')
if odpowiedz in dane:
    result = dane[odpowiedz]
    print(result)


utwory = {
    'gural': 'mandala',
    'dezerter': 'ratuj swoja dusze',
    'analogs': 'twoje klamstwa',
    'hania rein': 'f major',
}

