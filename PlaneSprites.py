import pygame

#屏幕大小的长量
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprites(pygame.sprite.Sprite):

    def __init__(self, imageName, speed = 1):
        super(GameSprites, self).__init__()

        self.image = pygame.image.load(imageName)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed

class BackGround(GameSprites):

    def __init__(self, isAlt = False):
        super(BackGround, self).__init__("./images/background.png")

        if isAlt:
            self.rect.y = -self.rect.height
    def update(self):

        #调用父类方法实现
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
