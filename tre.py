import math
y=int(input("y="))
x=int(input("x="))
a=int(input("a="))
G = (math.cos(2 / abs(y+x)-(x+y)))**(4*x) / (math.atanh(x+a)**4*x**5)
print(G)