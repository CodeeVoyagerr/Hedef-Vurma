import pygame as pg # Kısaltma için pg yaptık.
import sys # İşletim sisteminin kütüphanesi
import random

pg.init()  # Oyunu başlatmak için init()
ekran = pg.display.set_mode((1400,750))
zaman = pg.time.Clock()

su_yüksekliği = 600
su_hizi = 0.5

bulut_konumu1 = 200
bulut_konumu2 = 450
bulut_konumu3 = 700
bulut_konumu4 = 1200
bulut_hizi = 0.4

mario = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\mario.png")
arkaplan = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\göküyüzü.png")
çimen = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\çim.png")
su = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\su.png")
bulut_1 = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\bulut1.png")
bulut_2 = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\bulut2.png")
agac1 = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\ağaç1.png")
agac2 = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\ağaç2.png")
imleç = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\crosshair.png")
hedef = pg.image.load("C:\\Users\\Melike\\Desktop\\Pygame ile 2 Boyutlu Oyun ve Algoritma Geliştirmeye Giriş\\Proje#1\\hedef.png")

imleç_dörtgeni = imleç.get_rect(center = (700,375))

hedefler = []
for i in range(10):
    x = random.randint(150,1200)
    y = random.randint(50,550)
    hedef_dörtgeni = hedef.get_rect(center = (x,y))
    hedefler.append(hedef_dörtgeni)

while True:
    for olay in pg.event.get():
        # Oyunda ilerlemek için herhangi bir tuşa basmak bir eventtir.
        # Oyundan çıkış yapma eventi.
        if olay.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if olay.type == pg.MOUSEMOTION:
            imleç_dörtgeni = imleç.get_rect(center = olay.pos)

        if olay.type == pg.MOUSEBUTTONDOWN:
            for index, hedef1 in enumerate(hedefler):
                if hedef1.collidepoint(olay.pos):
                    del hedefler[index]
    

    ekran.blit(arkaplan,(0,0))

    su_yüksekliği -= su_hizi
    if su_yüksekliği >= 620 or su_yüksekliği <= 580:
        su_hizi *= -1

    for i in hedefler:
        ekran.blit(hedef,i)

    ekran.blit(agac1,(50,290))
    ekran.blit(agac1,(150,300))
    ekran.blit(agac2,(1150,280))
    ekran.blit(agac1,(950,300))
    ekran.blit(agac2,(1250,290))

    bulut_konumu1 -= bulut_hizi
    if bulut_konumu1 >= 250 or bulut_konumu1 <= 150:
        bulut_hizi *= -1
    bulut_konumu2 -= bulut_hizi
    if bulut_konumu2 >= 500 or bulut_konumu2 <= 400:
        bulut_hizi *= -1
    bulut_konumu3 -= bulut_hizi
    if bulut_konumu3 >= 750 or bulut_konumu3 <= 650:
        bulut_hizi *= -1
    bulut_konumu4 -= bulut_hizi
    if bulut_konumu4 >= 1250 or bulut_konumu4 <= 1150:
        bulut_hizi *= -1

    ekran.blit(bulut_1,(bulut_konumu1,210))
    ekran.blit(bulut_2,(bulut_konumu2,80))
    ekran.blit(bulut_1,(bulut_konumu3,180))
    ekran.blit(bulut_2,(bulut_konumu4,150))

    ekran.blit(çimen,(0,500))
    ekran.blit(su,(0,su_yüksekliği))

    ekran.blit(imleç,imleç_dörtgeni)

    yazi_font = pg.font.Font(None,60)
    yazi_yüzey = yazi_font.render("!!! Kazandınız !!!",True,(255,0,0))
    if len(hedefler) == 0:
        ekran.blit(yazi_yüzey,(550,375))

    pg.mouse.set_visible(False)
    pg.display.update()
    zaman.tick(120)