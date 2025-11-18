l = [3, 6, 11, 16, 21, 23, 25]

x = 0

for n in l:
    a = 0
    for b in range(0, n+1):
        if b == 0: continue
        if n % b == 0: a += 1
    if a == 2: x += 1

print(x)