import pygame

screen = pygame.display.set_mode((600, 600))
bg = pygame.image.load("./Hangman/aZRnb0.webp")

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()