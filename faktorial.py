# def yigindi_toq(n):
#     if n == 1:
#         print(n)
#     else:
#         if n % 2 == 0:
#             n = n - 1
#             print(n)
#             yigindi_toq(n - 2)
#
#
# print(yigindi_toq(6))

# def fib (n):
#     if n==1 or n==2:
#        return 1
#     else:
#         return fib (n -1)+fib (n-2)
# def fib|_hadlari(n)
#     for i in range(1, +1):
#         print(fib (i), end =' ')
# fib|_hadlari(9)


# try:
#     n = int (input('n = '))
#     if n != 10:
#         raise Exception()
# except:
#     print("xato")
# else:
#     print("xato yo'q")
#
# finally:
#     print ("dastur tamom")
import pygame
import random
pygame.int()
dis=pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('mening birinchi o\'yinim')

blue=(0, 0, 255)
red=(255, 0, 0)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update()


pygame.quit()
quit()