# Exemplo 1:
var = 1
print(var > 0)
print(not (var <= 0))

# Exemplo 2:
print(var != 0)
print(not (var == 0))

# Exemplo 3:
p = True
q = False
print(not (p and q) == (not p) or (not q))
print(not (p or q) == (not p) and (not q))

# Exemplo 4:
# Operação bit a bit
i = 15  # 0000 1111
j = 22  # 0001 0110
print(i & j)  # 0000 0110
print(i | j)  # 0001 1111
print(i ^ j)  # 0001 1001
print(~i)  # 1111 0000

# Exemplo 5:
x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y)
print(not z)

# Exemplo 6:
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
