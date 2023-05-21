import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Abcd(pygame.sprite.Sprite):
  def __init__(self):   #Функция, где указываем что будет у игрока
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + "change.png")
       self.rect = self.image.get_rect()
       self.rect.x = 510
       self.rect.y = 70