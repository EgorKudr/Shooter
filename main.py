import pygame
from player import Player
from speedometr import Speedometer
from arrow import Arrow
from bullet import Bullet
from auto_forward import Auto_forward
from auto_back import Auto_back
from road import Road
from board import Board
from tree import Tree
from explosion import Explosion
from bike import Bike1
from bike import Bike2
from bike import Bike3
from bike import Bike4
from abcd import Abcd
import random
from menu import Menu
from menu import Monet
from leves import Leves1
from leves import Leves2
from leves import Leves3
#from leves import Ak


def draw_text(screen, text, size, x, y, color):  # Функция для отображения текста
    font_name = 'font.ttf'
    font = pygame.font.Font(font_name, size)  # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)  # Превращаем текст в картинку
    text_rect = text_image.get_rect()  # Задаем рамку картинки с текстом
    text_rect.center = (x, y)  # Переносим центр текста в координаты
    screen.blit(text_image, text_rect)  # Рисуем текст на экране


def drawtext(screen, text, size, x, y, color):  # Функция для отображения текста
    font_name = 'MarkerFelt.ttc'
    font = pygame.font.Font(font_name, size)  # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)  # Превращаем текст в картинку
    text_rect = text_image.get_rect()  # Задаем рамку картинки с текстом
    text_rect.center = (x, y)  # Переносим центр текста в координаты
    screen.blit(text_image, text_rect)  # Рисуем текст на экране


width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
fps = 150  # частота кадров в секунду
gameName = "Racing"  # название нашей игры+

img_dir = 'media/img/'#папка с картинками
snd_dir = 'media/snd/'#папка со звуками

pygame.init()  # запуск игры

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
GOLD = (255, 215, 0)
BRONZE = (205, 127, 50)
ORANGE = (255, 117, 24)

# Создаем игровой экран
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption(gameName)  # Заголовок окна

icon = pygame.image.load(img_dir + 'icon1.png')  # загружаем файл с иконкой
pygame.display.set_icon(icon)  # устанавливаем иконку в окно
clock = pygame.time.Clock()  # Создаем часы pygame
  
all_sprites = pygame.sprite.Group()  # Создаем группу для спрайтов
players = pygame.sprite.Group()  # Создаем группу для игрока
bullets = pygame.sprite.Group()  # Создаем группу для спрайтов
cars = pygame.sprite.Group()  # Создаем группу для спрайтов
boards = pygame.sprite.Group()  # Создаем группу для спрайтов


road = Road()
all_sprites.add(road)  # Добавляем спрайт дороги ко всем спрайтам

board_right = Board('right')
board_left = Board('left')
all_sprites.add(board_right)
all_sprites.add(board_left)
boards.add(board_left)#добавляем левый бортик в список бортиков
boards.add(board_right)#добавляем правый бортик в список бортиков

for i in range(40):#цикл выполняется 20 раз
    tree = Tree()#создаём дерево
    all_sprites.add(tree)#добавляем дерево в список всех спрайтов

speedometer = Speedometer()#создаём спидометр
all_sprites.add(speedometer)#добавляем спидометр в список всех спрайтов

arrow = Arrow()#создаём стрелку
all_sprites.add(arrow)#добавляем стрелку в список стрелок

player = Player()  # Создаем игрока на основании класса
all_sprites.add(player)  # Добавляем спрайт игрока ко всем спрайтам
players.add(player)  # Добавляем игрока в группу ко всем игрокам

for i in range(4):#цикл выполняется 4 раза
    auto = Auto_forward()#создаём машинку, которая едет вперед
    all_sprites.add(auto)#добавляем в список всех спрайтов
    cars.add(auto)#добавляем в список машинок

for i in range(4):
    auto = Auto_back()#создаём машинку, которая едет назад
    all_sprites.add(auto)#добавили машинку во все спрайты
    cars.add(auto)#добавляем машинку auto в cars

pygame.mixer.music.load(snd_dir + 'music2.wav')
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play(-1)


bike1 = Bike1()
bike2 = Bike2()
bike3 = Bike3()
bike4 = Bike4()
abcd = Abcd()
menu = Menu()
monet = Monet()
leves1 = Leves1()
leves2 = Leves2()
leves3 = Leves3()
#ak = Ak()
all_sprites.add(bike1)
all_sprites.add(bike2)
all_sprites.add(bike3)
all_sprites.add(bike4)
all_sprites.add(abcd)
all_sprites.add(leves1)
all_sprites.add(leves2)
all_sprites.add(leves3)
#all_sprites.add(ak)

ziz1 = pygame.mixer.Sound(snd_dir + '-zizn.wav')
prodleniye = pygame.mixer.Sound(snd_dir + 'podleniy.wav')


def get_hit_sprite(hits_dict):  # Функция возвращает спрайт с которым столкнулись
    for hit in hits_dict.values():
        return hit[0]


run = True#игра идёт
while run:  # начинаем бесконечный цикл
    clock.tick(fps)  # контроль времени (обновление игры, максимум 30 кадров в секунду)
    all_sprites.update()  # обновление всех спрайтов
    # Рендеринг (прорисовка)
    screen.fill(GREEN)#заливка фона зеленым цветом
    all_sprites.draw(screen)  # Выводим на экран все спрайты из группы
    if player.speed > 0:
        bike1.kill()
        bike2.kill()
        bike3.kill()
        bike4.kill()
        abcd.kill()
    # Обработка ввода (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # Если клавиша нажата
            if event.key == pygame.K_SPACE:  # Если нажат пробел
                if len(players) > 0:
                    player.sound_shoot.play()
                    bullet = Bullet(player)  # Создаем пулю
                    all_sprites.add(bullet)  # Добавляем пулю ко всем спрайтам
                    bullets.add(bullet)  # Добавляем пулю ко всем пулям
                    player.magazin -= 1
                    if player.magazin <= 0:
                        bullet.kill()
                        player.sound_shoot.stop()
                        player.magazin = 0
            if event.key == pygame.K_r:
                player.magazin += 25
                if player.magazin >= 25:
                    player.magazin = 25


    # Событие столкновения пуль и авто
    hit_bullets = pygame.sprite.groupcollide(bullets, cars, True, False)
    if hit_bullets:  # Если произошло
        car = get_hit_sprite(hit_bullets)
        car.sound.play()
        expl = Explosion(car.rect.center)  # Создаем взрыв на месте моба
        all_sprites.add(expl)
        if car.type == 'forward':
            auto = Auto_forward()
            all_sprites.add(auto)
            cars.add(auto)
            player.score += random.randint(2, 20)
        else:
            auto = Auto_back()
            all_sprites.add(auto)
            cars.add(auto)
            player.score += random.randint(5, 30)

        car.kill()  # Сразу же убиваем моба

    # Событие столкновения бортика и игрока
    hit_boards = pygame.sprite.groupcollide(players, boards, False, False)
    # Событие столкновения машин и игрока
    hit_cars = pygame.sprite.groupcollide(players, cars, False, False)
    if hit_boards or hit_cars:  # Если произошло
        expl = Explosion(player.rect.center)  # Создаем взрыв на месте моба
        player.lives -= 1
        if player.lives == 80:
            leves1.kill()
            ziz1.play()
        if player.lives == 40:
            leves3.kill()
            ziz1.play()
        if player.lives == 0:
            leves2.kill()
            ziz1.play()
        if player.lives == 0:
            all_sprites.add(expl)
            player.sound_explosion.play()
            player.speed = 0
            player.sound_move.stop()
            all_sprites.add(menu)


    draw_text(screen, f'Заработано {player.score} монет', 50, width // 2, 20, GOLD)
    drawtext(screen, f'У вас осталось {player.magazin}', 25, 106, 350, ORANGE)
    drawtext(screen, 'патрон', 25, 106, 380, ORANGE)

    for car in cars:  # Перебираем в цикле все авто
        cars.remove(car)  # Удаляем одно авто из группы

        # Событие столкновения машин между собой
        hit_another_car = pygame.sprite.spritecollide(car, cars, False)
        if hit_another_car:
            car.sound.play()
            expl = Explosion(car.rect.center)  # Создаем взрыв на месте моба
            all_sprites.add(expl)
            if car.type == 'forward':
                auto = Auto_forward()
                all_sprites.add(auto)
                cars.add(auto)
            else:
                auto = Auto_back()
                all_sprites.add(auto)
                cars.add(auto)
            car.kill()  # Уничтожаем авто
        else:
            cars.add(car)  # Если не сталкивается, возвращаем обратно в группу

    keystate = pygame.key.get_pressed()  # Сохраняем нажатие на кнопку
    if keystate[pygame.K_n]:
        run = False
    elif keystate[pygame.K_y]:
        if player.score <= 0:
            all_sprites.add(monet)
            player.score += 500
            player.score -= 500
            player.kill()

        elif player.score >= 500:
            player.score -= 500
            player.lives += 125
            menu.kill()
            monet.kill()
            prodleniye.play()
            player.sound_move.play()
            all_sprites.add(leves1)
            all_sprites.add(leves2)
            all_sprites.add(leves3)


    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()  # закрываем модуль pygame