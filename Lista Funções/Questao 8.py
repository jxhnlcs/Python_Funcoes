import random

d1 = random.randrange(1,7)
d2 = random.randrange(1,7)
def dado(a,b):
  conte = (d1+d2)
  if conte == 7 or conte == 11:
    print("Você ganhou!")
  elif conte == 2 or conte == 3 or conte == 12 or conte == 3:
    print("Você perdeu!")
  elif conte == 4 or conte == 5 or conte == 6 or conte == 9 or conte == 10:
    print("Ponto!")
dado(d1,d2)