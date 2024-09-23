from sys import path

path.append('../modules')

import module

for p in path:
    print(p)

zeroes = [0 for i in range(5)]
ones = [1 for j in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

