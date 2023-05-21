import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'
class Board(pygame.sprite.Sprite):
  def __init__(self, type):   # Здесь получаем тип бордюра
      pygame.sprite.Sprite.__init__(self)

      self.image = pygame.image.load(img_dir + "board.png")
      self.rect = self.image.get_rect()
      if type == 'lefs':      # В зависимости от типа располагаем и переворачиваем
           self.image = pygame.transform.flip(self.image, True, False)
           self.rect.centerx = width // 2 + 370
      else:
           self.rect.centerx = width // 2 - 370
      self.speed = 0
      self.max_speed = 50
      self.min_speed = 0

      if type == 'right':
          self.image = pygame.transform.flip(self.image, True, False)
          self.rect.centerx = width // 2 + 370
      else:
          self.rect.centerx = width // 2 - 370

  def update(self):  # Функция, действия которой будут выполняться каждый тик
      keystate = pygame.key.get_pressed()  # Сохраняем нажатие на кнопку
      if keystate[pygame.K_UP] and self.speed < self.max_speed:  # Стрелка вверх
          self.speed += 1
      elif keystate[pygame.K_DOWN] and self.speed > self.min_speed:  # Стрелка вниз
          self.speed -= 1

      self.rect.y += self.speed  # Изменяем положение по вертикали

      if self.rect.centery > height:  # Если центр достиг низа
          self.rect.centery = 0  # Переносим бортик
