from sys import path

path.append('../packages')

## Isso não funciona
# from extra.iota import FunI
# print(FunI())

import extra.bla as bla

print(bla.func_bla())
