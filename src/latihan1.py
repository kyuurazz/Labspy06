import math

a = lambda x : x ** 2

b = lambda x, y : x**2 + y**2

c = lambda *args : sum(args)/len(args)

d = lambda s: "".join(set(s))

print(a(50))
print(b(10 , 25))
print(c(-2, 30, 6, 8))
print(d("Bilal"))