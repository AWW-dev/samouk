lists = []
rap = ['peja', 'gural', 'taco']
rock = ['bob dylan', 'the beatles', 'led zeppelin']
djs = ['zeds dead', 'tiesto']

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
print(rap)
rap.append("Kendrick Lamar")
print(rap)
print(lists)

bday = {
    "hemingway": "7.21.1899",
    'fitzerald': '9.24.1896',
}

print(bday)
mylist = [bday]
print(mylist)
mytupla = (bday,)
print(mytupla)

ny = {
    "lokalizacja": (40.7128, 73.0059),
    "celebryci": ["W. Allen", "Jay Z", "K. Bacon"],
    "fakty":{
        "stan":"NY",
        "kraj":"USA",
    }
}

print(ny)