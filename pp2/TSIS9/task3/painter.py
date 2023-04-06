import pygame

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

colors = [RED, GREEN, BLUE]

# draw functions
def drawCircle( screen, x, y, color):
    pygame.draw.circle( screen, color, ( x ,y), 40)

def freeDraw( screen, x, y, color):
    pygame.draw.circle( screen, color, (x, y), 2)

def drawRect( screen, x, y, color):
    pygame.draw.rect(screen, color, (x, y, 50, 80))

def drawSquare( screen, x, y, color):
    pygame.draw.rect(screen, color, (x, y, 50, 50)) 

def drawRightTriangle(screen, x, y, color):
    pygame.draw.polygon(screen, color, ((x,y),(x+50,y),(x+50,y+50)))

def drawEquiTriangle(screen, x, y, color):
    pygame.draw.polygon(screen, color, ((x,y), (x+50, y+40), (x+60, y-20)))

def drawRhombus(screen, x, y, color):
    pygame.draw.polygon(screen, color, ((x,y),  (x+50, y-70), (x+100,y), (x+50, y+70)))

screen.fill(WHITE)

i = 0 # color's index

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # choose color
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            i += 1
            i = i % 3

        # circle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (x, y) =  pygame.mouse.get_pos()
            drawCircle( screen, x, y, colors[i])
        
        # free drawing
        key = pygame.key.get_pressed()
        if key[pygame.K_t]:
            (x, y) =  pygame.mouse.get_pos()
            freeDraw(screen, x, y, colors[i])

        # rectangle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            (x, y) = pygame.mouse.get_pos()
            drawRect( screen, x, y, colors[i])
        
        if event.type == pygame.KEYDOWN:
            (x, y) =  pygame.mouse.get_pos()
            # square
            if event.key == pygame.K_q:
                drawSquare(screen, x, y, colors[i])
            # right triangle
            elif event.key == pygame.K_w:
                drawRightTriangle(screen, x,y,colors[i])
            # equilateral
            elif event.key == pygame.K_e:
                drawEquiTriangle(screen, x,y,colors[i])
            # rhombus
            elif event.key == pygame.K_r:
                drawRhombus(screen, x,y,colors[i])

        # eraser
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(WHITE)

    pygame.display.update()
    clock.tick(60)