import pygame as pg
import pygame.draw as draw
import math

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
text3 = basefont.render('Undo', 1, (150, 50, 60))
text4 = basefont.render('Clear', 1, (150, 50, 60))

fxnlist = [] #for shape
blitlist = [] #for text
mode = -1 #0 - rectangle, 1 - circle

blitlist.append([text,0, 0])
blitlist.append([text2,185, 0])
blitlist.append([text3,360, 0])
blitlist.append([text4,480, 0])

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
    if 450 > rect.center[0] > 300 and 50 > rect.center[1] > 0:
            draw.rect(screen, pg.Color('red'),(300,0,150,50))
    else:
            draw.rect(screen, r1,(300,0,150,50))
    if 620 > rect.center[0] > 480 and 50 > rect.center[1] > 0:
            draw.rect(screen, pg.Color('red'),(480,0,150,50))
    else:
            draw.rect(screen, r1,(480,0,150,50))
    '''event handling'''

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            for fxn in fxnlist:
                sqx = (x - fxn[0])**2
                sqy = (y - fxn[1])**2
                if math.sqrt(sqx + sqy) < 100:
                    print 'in range'
            if 150 > rect.center[0] > 0 and 50 > rect.center[1] > 0: # rect
                mode = 0
            elif 300 > rect.center[0] > 150 and 50 > rect.center[1] > 0: # circle
                mode = 1
            elif 450 > rect.center[0] > 300 and 50 > rect.center[1] > 0: # undo
                mode = -1
            elif 620 > rect.center[0] > 480 and 50 > rect.center[1] > 0: # clear
                mode = -2
            elif mode == 0 or mode == 1:
                x,y = pg.mouse.get_pos()
                fxnlist.append([x, y, mode]) #if key is press down, append mouse position to be drawn
            elif mode == -1:
                if len(fxnlist)>0:
                    fxnlist.pop()
                    break


    for fxn in fxnlist: #draw squares at all the mouse positions
        if fxn[2]==0:
            draw.rect(screen,pg.Color('red'),(fxn[0],fxn[1],50,50))
        if fxn[2]==1:
            draw.circle(screen, pg.Color('red'), (fxn[0],fxn[1]), 50)

    for text in blitlist: #insert text at location
        screen.blit(text[0], (text[1], text[2]))

    #print fxnlist
    pg.display.update()
    clock.tick(60)
