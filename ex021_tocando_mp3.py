import pygame
pygame.init()

titulo = 'TokPlay'
print(f'{titulo:=^40}\n')

pygame.mixer.music.load('ex021_tocando.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
