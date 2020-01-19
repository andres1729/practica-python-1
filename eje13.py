from random import randint as rnd
from math import pi, e

lanzamiento = rnd(1, 6)
if lanzamiento < 4:
    print(pi*lanzamiento)
else:
    print(e*lanzamiento)