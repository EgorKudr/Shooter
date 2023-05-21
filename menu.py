import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'

class Menu(pygame.sprite.Sprite):
  def __init__(self):   #Функция, где указываем что будет у игрока
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + "yn.png")
       self.image = pygame.transform.scale(self.image, (700, 608))  #(1082, 928))
       self.rect = self.image.get_rect()
       self.rect.x = 250   #width #323
       self.rect.y = 0



class Monet(pygame.sprite.Sprite):
  def __init__(self):   #Функция, где указываем что будет у игрока
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + "monet.png")
       self.rect = self.image.get_rect()
       self.rect.x = 295
       self.rect.y = 280