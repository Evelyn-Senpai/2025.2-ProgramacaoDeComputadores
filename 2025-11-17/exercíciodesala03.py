a = 0
b = 1
c = a + b
d = 10

for x in range(0, d -1):
    c = a + b
    a = b
    b = c

print(c)
print(b)
print(a)