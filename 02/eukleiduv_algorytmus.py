u = 585
w = 666
while w != 0:
  r = u % w
  u = w
  w = r
else:
    print("Největší společný dělitel je", u)