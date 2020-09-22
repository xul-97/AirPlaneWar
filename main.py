import pygame
from PlaneSprites import *

class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__createSprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)


    def __createSprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.backGroup = pygame.sprite.Group(bg1,bg2)

        self.enemyGroup = pygame.sprite.Group()

        self.hero = Hero()
        self.heroGroup = pygame.sprite.Group(self.hero)



    def startGame(self):
        print("开始游戏。。")

        while True:

            self.clock.tick(FRAME_PER_SEC)

            self.__eventHandler()

            self.__checkCollide()

            self.__updateSprites()

            pygame.display.update()

            pass

    def __eventHandler(self):
        '''事件监听'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__gameOver()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemyGroup.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keysPressed = pygame.key.get_pressed()

        if keysPressed[pygame.K_RIGHT] or keysPressed[pygame.K_d]:
            if self.hero.rect.x < (SCREEN_RECT.width - self.hero.rect.width):

                self.hero.rect.centerx += 2
        elif keysPressed[pygame.K_LEFT] or keysPressed[pygame.K_a]:
            if self.hero.rect.x > 0 :

                self.hero.rect.centerx -= 2
        elif keysPressed[pygame.K_UP] or keysPressed[pygame.K_w]:
            if self.hero.rect.y > 0:

                self.hero.rect.y -= 2
        elif keysPressed[pygame.K_DOWN] or keysPressed[pygame.K_s]:
            if self.hero.rect.bottom < SCREEN_RECT.height:

                self.hero.rect.y += 2


        pass

    def __checkCollide(self):
        '''碰撞监测'''
        pygame.sprite.groupcollide(self.hero.bulletGroup, self.enemyGroup, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemyGroup,True)
        if len(enemies) > 0:
            PlaneGame.__gameOver()

        pass

    def __updateSprites(self):
        '''事件精灵更新'''
        self.backGroup.update()
        self.backGroup.draw(self.screen)

        self.enemyGroup.update()
        self.enemyGroup.draw(self.screen)

        self.heroGroup.update()
        self.heroGroup.draw(self.screen)

        self.hero.bulletGroup.update()
        self.hero.bulletGroup.draw(self.screen)


    @staticmethod
    def __gameOver():
        '''游戏结束'''
        # print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.startGame()