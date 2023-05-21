import pygame

width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'
class Player(pygame.sprite.Sprite):
  def __init__(self):   #Функция, где указываем что будет у игрока
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + "moto.png")
       self.rect = self.image.get_rect()
       self.rect.x = width // 2
       self.rect.y = height - 150
       self.max_speed = 50
       self.min_speed = 0
       self.speed = 0
       self.global_speed = 0  # Общая скорость движения
       self.global_min_speed = 0  # Общая минимальная скорость движения
       self.global_max_speed = 50  # Общая максимальная скорость движения
       self.sound_move = pygame.mixer.Sound(snd_dir + 'motor.wav')
       self.sound_explosion = pygame.mixer.Sound(snd_dir + 'explosion_player.wav')
       self.sound_shoot = pygame.mixer.Sound(snd_dir + 'shoot.wav')
       self.score = 0
       self.lives = 120
       self.magazin = 25

  def update(self):  # Функция, действия которой выполнятся каждый тик
       keystate = pygame.key.get_pressed()  # Сохраняем нажатие на кнопку
       if keystate[pygame.K_a]:
           self.image = pygame.image.load(img_dir + "moto1.png")
           self.rect = self.image.get_rect()
           self.rect.x = 580
           self.rect.y = height - 150
       elif keystate[pygame.K_b]:
           self.image = pygame.image.load(img_dir + "moto2.png")
           self.rect = self.image.get_rect()
           self.rect.x = 580
           self.rect.y = height - 150
       elif keystate[pygame.K_c]:
           self.image = pygame.image.load(img_dir + "moto3.png")
           self.rect = self.image.get_rect()
           self.rect.x = 580
           self.rect.y = height - 150
       elif keystate[pygame.K_d]:
           self.image = pygame.image.load(img_dir + "moto.png")
           self.rect = self.image.get_rect()
           self.rect.x = 580
           self.rect.y = height - 150
       if keystate[pygame.K_RIGHT]:  # Если нажата стрелка вправо
            self.rect.x += 3  # Изменяем координату Х на 5
       elif keystate[pygame.K_LEFT]:  # Если нажата стрелка влево
            self.rect.x -= 3  # Изменяем координату Х на -5
       elif keystate[pygame.K_UP] and self.speed < self.max_speed:  # Стрелка вверх
            self.speed += 1
       elif keystate[pygame.K_DOWN] and self.global_speed > self.min_speed:  # Стрелка вниз
            self.speed -= 1
       if self.speed > 0 and not pygame.mixer.get_busy():
            self.sound_move.play()
       if self.speed == 0:
            self.sound_move.stop()
       if self.rect.x > 910:
            self.rect.x = 910
       if self.rect.x < 250:
            self.rect.x = 250