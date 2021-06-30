#uchburchakning tomonlari a=3, b=4, c=5 P=?, S=?
import math

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
P1=a+b+c
P=(a+b+c)/2
S=math.sqrt(P*(P-a)*(P-b)*(P-c))
print("P1=",P1,"S=",S)