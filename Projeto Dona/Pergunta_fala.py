import pygame

def fala():
    pygame.mixer.init()
    pygame.mixer.music.load('frasePerg.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass