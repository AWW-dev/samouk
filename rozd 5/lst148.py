fruits = {
    'agrest': 'zielony',
    "porzeczka": 'czerowna'
}
print(fruits)

facts = {}
facts['programowanie'] = 'zabawa'
facts['Bill'] = "Gates"
facts['Grunwald'] = 1410

print(facts)

print(facts['programowanie'])
print(facts['Bill'])
print(facts['Grunwald'])
print("Bill" in facts)

del facts['Bill']
print(facts)

rhymes = {
    '1': 'niebem',
    '2': 'kwa kwa',
    '3': 'sni',
    '4': 'bajery',
    '5': 'cięć'
}

n = input("wpisz cyfre: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("nie znaleziono")