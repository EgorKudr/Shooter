import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'

class Leves1(pygame.sprite.Sprite):
  def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + "zizni.png")
       self.image = pygame.transform.scale(self.image, (80, 40))
       self.rect = self.image.get_rect()
       self.rect.x = 500
       self.rect.y = 47


class Leves2(pygame.sprite.Sprite):
  def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + "zizni.png")
       self.image = pygame.transform.scale(self.image, (80, 40))
       self.rect = self.image.get_rect()
       self.rect.x = 560
       self.rect.y = 47


class Leves3(pygame.sprite.Sprite):
  def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + "zizni.png")
       self.image = pygame.transform.scale(self.image, (80, 40))
       self.rect = self.image.get_rect()
       self.rect.x = 620
       self.rect.y = 47


#class Ak(pygame.sprite.Sprite):pyinstaller
  #def __init__(self):
       #pygame.sprite.Sprite.__init__(self)
       #self.image = pygame.image.load(img_dir + "ak47.png")
       #self.rect = self.image.get_rect()
       #self.rect.x = 950
       #self.rect.y = 10