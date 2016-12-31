import pygame as pg
import pygame.draw as draw


screensize = (800, 600)

###  PYGAME SETUP  ###
pg.init()
screen = pg.display.set_mode(screensize)
clock = pg.time.Clock()
###  DONE  ###

i = 1
rect = pg.Rect(50, 50, 50, 50)
basefont = pg.font.SysFont('Monospaced', 100)
text = basefont.render('hello', 1, (150, 50, 60))
fxnlist = []
while(1):
    screen.fill(pg.Color('white'))
    screen.blit(text, (400, 400))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            fxnlist.append([x, y])
            #draw.rect(screen,pg.Color('red'),(200,150,100,50))
            #exit(0)
    if pg.key.get_pressed()[pg.K_e]:  # alt way if multiple keys held
        print 'e down'
    rect.center = pg.mouse.get_pos()
    draw.rect(screen,pg.Color('red'),rect, 0)
    for fxn in fxnlist:
        draw.rect(screen,pg.Color('red'),(fxn[0],fxn[1],50,50))
    pg.display.update()
    clock.tick(60)
