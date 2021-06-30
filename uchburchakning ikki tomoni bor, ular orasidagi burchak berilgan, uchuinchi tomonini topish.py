#uchburchakning ikki tomoni bor, ular orasidagi burchak berilgan, uchuinchi tomonini topish, c=?a=int(input("a="))
import math
a = int(input("a="))
b = int(input("b="))
x = int(input("x="))
x_rad = x/180*math.pi
c = math.sqrt(a**2+b**2-2*a*b*math.cos(x_rad))
print(c)