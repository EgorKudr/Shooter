import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Bike1(pygame.sprite.Sprite):
  def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + 'moto1.png')
       self.rect = self.image.get_rect()
       self.rect.x = 605
       self.rect.y = 70


class Bike2(pygame.sprite.Sprite):
  def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + 'moto2.png')
       self.rect = self.image.get_rect()
       self.rect.x = 605
       self.rect.y = 155


class Bike3(pygame.sprite.Sprite):
  def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + 'moto3.png')
       self.rect = self.image.get_rect()
       self.rect.x = 605
       self.rect.y = 245


class Bike4(pygame.sprite.Sprite):
  def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + 'moto.png')
       self.rect = self.image.get_rect()
       self.rect.x = 605
       self.rect.y = 327