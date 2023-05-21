import pygame
import random
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'
class Auto_back(pygame.sprite.Sprite):#наследуем класс машинки от класса Sprite в pygame
   def __init__(self):   # описываем то, как создать машинку
      pygame.sprite.Sprite.__init__(self)# вызываем создание стандартного спрайта из pygame
      self.type = 'back'#переменная, которая показывает, что машинка едет назад
      self.points = [(width // 2 - 50),
                     (width // 2 - 130),
                     (width // 2 - 210),
                     (width // 2 - 290)]#точки, на которых машина будет появляться
      self.image = pygame.image.load(img_dir + f"auto/{random.randrange(5)}.png")#загрузили рандомную картинку машины
      self.image = pygame.transform.rotate(self.image, 180)#повернули машину на 180 градусов, так как она едет назад
      self.rect = self.image.get_rect()#получили прямоугольник описанный вокруг спрайта
      self.rect.center = (random.choice(self.points), 0)#выбрали рандомную точку для появления машины
      self.min_speed = 5  # Минимальная скорость движения
      self.max_speed = 20  # Максимальная скорость движения
      self.speed = random.randint(self.min_speed, self.max_speed)# задали текущую скорость машины

      self.global_speed = 0  # Общая скорость движения
      self.global_min_speed = 0  # Общая минимальная скорость движения
      self.global_max_speed = 50  # Общая максимальная скорость движения

      self.rect.y = random.randrange(-height, 0, 300)#задали координату y для машины
      self.sound = pygame.mixer.Sound(snd_dir + 'explosion_car.wav')#задали звук взрыва

   def update(self):  # Функция, действия которой будут выполняться каждый тик

       self.rect.y += self.speed + self.global_speed#добавить скорость к машине

       keystate = pygame.key.get_pressed()  # Сохраняем нажатие на кнопку
       if keystate[pygame.K_UP] and self.global_speed < self.global_max_speed:#если нажата кнопка и скорость меньше максимальной
           self.global_speed += 1#увеличить скорость на 1
       elif keystate[pygame.K_DOWN] and self.global_speed > self.global_min_speed:#если нажата кнопка и скорость меньше максимальной
           self.global_speed -= 1#уменьшаем скорость на 1

       if self.rect.top > height:  # Если достигли нижнего края экрана
           self.speed = random.randint(self.min_speed, self.max_speed)#задаём рандомную скорость
           self.rect.center = (random.choice(self.points), random.randrange(-height, 0, 300))#задаём рандомные координаты для появления машины после того как она исчезла за экраном