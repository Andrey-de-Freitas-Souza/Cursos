import pygame                               # importando py game
pygame.init()                               # iniciando py game
pygame.mixer.music.load('ex021.mp3')        # carregando a música
pygame.mixer.music.play()                   # dando play na música
input()                                     # entrada
pygame.event.wait()                         # esperando a música acabar
