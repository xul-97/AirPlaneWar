import pygame
from PlaneSprites import *

class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__createSprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)


    def __createSprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.backGroup = pygame.sprite.Group(bg1,bg2)



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
            print(event)
            if event.type == pygame.QUIT:
                PlaneGame.__gameOver()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
        pass

    def __checkCollide(self):
        '''碰撞监测'''
        pass

    def __updateSprites(self):
        '''事件精灵更新'''
        self.backGroup.update()
        self.backGroup.draw(self.screen)

        pass

    @staticmethod
    def __gameOver():
        '''游戏结束'''
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.startGame()