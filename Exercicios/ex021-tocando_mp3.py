import pygame

pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# pygame.event.wait()
terminar = input('Aperte enter para encerrar a música')