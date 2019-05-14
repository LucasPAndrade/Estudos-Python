#resolução
##copia música e cola no projeto
import pygame
pygame.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play()
pygame.event.wait()