import pygame
import random

pygame.init()
# Songs below are made by me :D
# Used Fl Studio 20 for production, first one uses BeepBox

path = r"C:\KBTU\2nd semester\pp2\TSIS7\audio"

songs = [path+r"\raining oranges.mp3", 
         path+r"\smth tropical.mp3",
         path+r"\Spider theme pluto remix.mp3", 
         path+r"\Raindrops.mp3",
         path+r"\Planet theme.mp3", 
         path+r"\Snowcats.mp3",
         path+r"\when muffins sleep.mp3",
         path+r"\ruska 8bit.mp3",
         path+r"\stardust.mp3"
         ]
i = random.randint(0, len(songs)-1)
j = i # checks if future songs are not out of range
pygame.mixer.music.load(songs[i])
pygame.mixer.music.play()


WIDTH = 200
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fPaused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            # pause
            if event.key == pygame.K_SPACE and not fPaused:
                pygame.mixer.music.pause()
                fPaused = True
            elif event.key == pygame.K_SPACE and fPaused:
                pygame.mixer.music.unpause()
                fPaused = False
            
            # previous
            if event.key == pygame.K_LEFT:
                j -= 1
                if j >= 0:
                    i -= 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.rewind()
            # next
            if event.key == pygame.K_RIGHT:
                j += 1
                if j < len(songs):
                    i += 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.rewind()

            

    screen.fill((0, 0, 0))
    pygame.display.update()
