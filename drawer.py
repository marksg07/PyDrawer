import pygame as pg
import pygame.draw as draw


screensize = (800, 600)

###  PYGAME SETUP  ###
pg.init()
screen = pg.display.set_mode(screensize)
def getscreen():
    return screen
clock = pg.time.Clock()
###  DONE  ###

######################
# draw tabs          #
# tab 1 - square     #
# tab 2 - circle     #
# tab 3 - ?          #
######################


#Color options
r1 = (210,69,69)
r2 = (210,69,126)

i = 1
rect = pg.Rect(50, 50, 50, 50)
basefont = pg.font.SysFont('Monospaced', 40)
text = basefont.render('Rectangle', 1, (150, 50, 60))
text2 = basefont.render('Circle', 1, (150, 50, 60))
fxnlist = [] #for shape
blitlist = [] #for text
mode = -1 #0 - rectangle, 1 - circle

blitlist.append([text,0, 0])
blitlist.append([text2,185, 0])

#keep running dis
while(1):
    screen.fill(pg.Color('white')) #refresh the screen

    rect.center = pg.mouse.get_pos() #keep square at center of mouse
    draw.rect(screen,pg.Color('red'),rect, 0)

    '''tabs section -- refer to above diagram'''

    if 150 > rect.center[0] > 0 and 50 > rect.center[1] > 0:
            draw.rect(screen, pg.Color('red'),(0,0,150,50))
    else:
            draw.rect(screen, r1,(0,0,150,50))
    if 300 > rect.center[0] > 150 and 50 > rect.center[1] > 0:
         draw.circle(screen, pg.Color('red'), (225,0), 50)
    else:
        draw.circle(screen, r2, (225,0), 50)

    '''event handling'''

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if 150 > rect.center[0] > 0 and 50 > rect.center[1] > 0:
                mode = 0
            elif 300 > rect.center[0] > 150 and 50 > rect.center[1] > 0:
                mode = 1
            elif mode == 0 or mode == 1:
                x,y = pg.mouse.get_pos()
                fxnlist.append([x, y, mode]) #if key is press down, append mouse position to be drawn
   ''' if pg.key.get_pressed()[pg.K_e]:  # alt way if multiple keys held
        print 'e down'
    '''

    for fxn in fxnlist: #draw squares at all the mouse positions
        if fxn[2]==0:
            draw.rect(screen,pg.Color('red'),(fxn[0],fxn[1],50,50))
        if fxn[2]==1:
            draw.circle(screen, pg.Color('red'), (fxn[0],fxn[1]), 50)

    for text in blitlist: #insert text at location
        screen.blit(text[0], (text[1], text[2]))


    pg.display.update()
    clock.tick(60)
