import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'  # папка с картинками
snd_dir = 'media/snd/'  # папка со звуками


class Arrow(pygame.sprite.Sprite):#наследуем класс стрелки от класса Sprite в pygame
    def __init__(self):#описываем то, как создать стрелку
        pygame.sprite.Sprite.__init__(self)# вызываем создание стандартного спрайта из pygame
        self.image = pygame.image.load(img_dir + 'arrow.png')#загружаем картинку стрелки
        self.image = pygame.transform.rotate(self.image, -200)#поворачиваем картинку стрелки
        self.rect = self.image.get_rect()#получаем прямоугольник описанный вокруг стрелки
        self.copy = self.image#создаём копию картинки
        self.rect.center = (100, height - 100)  #передвигаем стрелку на нужную позицию на экране
        self.max_speed = 50# задали максимальную скорость
        self.min_speed = 0#задали минимальную скорость
        self.speed = 0# задали текущую скорость

    def rotate(self, rotate):
        self.image = pygame.transform.rotate(self.copy, rotate)  # Поворачиваем копию
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменяем рамку

    def update(self):  # Функция, действия которой выполнятся каждый тик
        keystate = pygame.key.get_pressed()  # Смотрим на какую клавишу нажал пользователь
        if keystate[pygame.K_UP] and self.speed < self.max_speed:  # если нажата стрелка вверх и скорость меньше максимальной
            self.speed += 1#увеличиваем скорость на 1
        elif keystate[pygame.K_DOWN] and self.speed > self.min_speed:  # если нажата стрелка вниз и скорость > минимальной
            self.speed -= 1#уменьшаем скорость на 1
        self.rotate(-self.speed * 6)  # Крутим стрелку








