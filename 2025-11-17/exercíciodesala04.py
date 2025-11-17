x = 13
c = y = 0
a = z = 1

while a <= x:
    a = z + y
    c += 1
    y = z
    z = a

if x > y: c = 0

print(c)
print(y)
print(a)
print(z)