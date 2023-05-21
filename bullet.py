import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'
class Bullet(pygame.sprite.Sprite):
   def __init__(self, player):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + 'shell.png')
       self.image = pygame.transform.scale(self.image, (7, 18))

       self.rect = self.image.get_rect()
       self.rect.center = player.rect.center    # Располагаем пулю там же где и игрок
       self.speed = 70

   def update(self):
       self.rect.y -= self.speed      # Полет пули против оси Y
       if self.rect.y < 0:            # Если залетела за верхний край экрана
           self.kill()