# class Avtomobil:
#     def_init_(self,rusumi,yili,rangi,firmasi):
#     self.rusumi=rusumi,
#     self.yili=yili,
#     self.rangi=rangi,
#     self,firmasi=firmasi
# malibu=Avtomobil("Malibu", 2022, "qora", "Chevrolet")
# lacette=Avtomobil("lacette", 2020, "oq", "Chevrolet")
# print(malibu.rusumi, malibu.rangi)
# print(malibu.__dict__)
# class Avtomobil:
#     def_init_(self,rusumi):
#         self.rusumi=rusumi
#     def signal(self):
#         print("Biiib")
#     malibu=Avtomobil("Malibu")
#     malibu.signal()
# class Shaxs:
#     def __init__(self,ism,fan):
#        self.ism=ism
#        self.fan=fan
#     def tuliq_ism(self):
#         return self.ism+self.fan
# sh1=Shaxs("Oybek", " Narzullayev")
# print(sh1.tuliq_ism())
# class Shaxs:
#     def __init__(self,ism,fan,shahri,mahallasi):
#         self.ism = ism
#         self.fan = fan
#         self.shahri=shahri
#         self.mahallasi=mahallasi
#     def tuliq_ism(self):
#         return self.ism+''+self.fan
#     def tuliq_manzil(self):
#         return f"{self.shahri}shahri;{self.mahallasi}mahallasi"
#
# sh1=Shaxs("Oybek","Narzullayev","Jizzax","Uchariq")
# print(sh1.tuliq_ism())
# print(sh1.tuliq_manzil())

class Xodim:
    def __init__(self,ismi,manzili,maoshi):
        self.ismi=ismi
        self.manzili=manzili
        self.maoshi=maoshi
xodimlar=[]
x1=Xodim("Bunyod","lalmikor",4000000)
xodimlar.append(x1)
x2=Xodim("Sunnat","Lalmikor",4000000)
xodimlar.append(x2)
x3=Xodim("Doston","Lalmikor",3000000)
xodimlar.append(x3)
x4=Xodim("Ilyos","Lalmikor",1500000)
xodimlar.append(x4)
x5=Xodim("shaxzod","Lalmikor",9000000)
xodimlar.append(x5)
for xodim in xodimlar:
    if xodim.maoshi<2000000:
        print(xodim.ismi)








