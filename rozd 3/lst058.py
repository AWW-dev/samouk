a = 1
b = 2
c = 3

d = a == 1 and b == 2
e = a == 1 and b == 1
f = a == 2 and b == 1
g = a == 1 and c != b and b < c

h = a == 1 or a == 2
i = a == 1 or b == 2
j = a == 2 or b == 1
k = a == b or b == c or c == 3

l = not a == 1
m = not a == 2

print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
