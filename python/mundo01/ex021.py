# Objetivo: Faça um programa em python que abra e reproduza o áudio de um arquivo em mp3.
# Data: 19/10/22
# Author: Washington
import pygame

print("{:-^50}".format("Inicio do Programa"), "\n")

pygame.mixer.init()
pygame.mixer.music.load('arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print("\n", "{:-^50}".format("Fim do Programa"))