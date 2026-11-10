n = int(input())
p = list(map(int, input().split()))
pos = [0] * (n + 1)

for i in range(n):
    pos[p[i]] = i

costo = 0

for i in range(1, n):
    costo += i * abs(pos[i] - pos[i + 1])

print(costo)