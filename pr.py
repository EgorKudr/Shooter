import pygame
img_dir = 'media/img/'#папка с картинками
snd_dir = 'media/snd/'#папка со звуками
pygame.init()
clock = pygame.time.Clock()


class Background(pygame.sprite.Sprite):
    def __init__(self, left):
        super().__init__()
        self.image = pygame.image.load(img_dir + "road.jpg").convert()
        self.rect = self.image.get_rect(topleft=(left, 0))

    def update(self):
        keystate = pygame.key.get_pressed()  # Сохраняем нажатие на кнопку
        if keystate[pygame.K_RIGHT]:
            if self.rect.right == 642:
                bg_group.add(Background(left=640))
            self.rect.x = self.rect.x - 2
            if self.rect.right == 1:
                self.kill()


win = pygame.display.set_mode((640, 480))
bg_group = pygame.sprite.Group()
bg_group.add(Background(left=0))
while 1:
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()

    bg_group.draw(win)
    bg_group.update()
    pygame.display.update()
    clock.tick(200)