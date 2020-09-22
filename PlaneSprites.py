import random
import pygame

#屏幕大小的长量
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#敌机定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

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

class Enemy(GameSprites):
    def __init__(self):

        super(Enemy, self).__init__("./images/enemy1.png")
        self.speed = random.randint(1,3)

        self.rect.bottom = 0 #图片底部位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        pass

    def __del__(self):
        pass

        #print("敌机销毁 %s" % self.rect)

    def update(self):
        super(Enemy, self).update()

        if self.rect.y >= SCREEN_RECT.height:
            #print("飞出屏幕，需要精灵组移除")
            self.kill()
        pass

class Hero(GameSprites):

    def __init__(self):
        super(Hero, self).__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 120


        self.bulletGroup = pygame.sprite.Group()

    def fire(self):
        # print("发射子弹。。")
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y - 10
        bullet.rect.centerx = self.rect.centerx

        self.bulletGroup.add(bullet)


class Bullet(GameSprites):

    def __init__(self):
        super(Bullet, self).__init__("./images/bullet1.png", -3)


    def update(self):
        super(Bullet, self).update()

        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        # print("子弹被销毁")
        pass