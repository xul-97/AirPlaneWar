import pygame
from sys import exit
from PlaneSprites import *

heroRect = pygame.Rect(100,500,102,126)
#模块初始化
pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480,700))
#加载图像
background = pygame.image.load("./images/background.png")


#创建敌机精灵
enemy = GameSprites("./images/enemy1.png")
enemy1 = GameSprites("./images/enemy1.png",2)
#创建敌机精灵组
enemyGroup = pygame.sprite.Group(enemy, enemy1)



hero = pygame.image.load("./images/me1.png")


clock = pygame.time.Clock()


while True:
    # 更新屏幕
    clock.tick(60)
    heroRect.y -= 5
    if heroRect.y < -125:
        heroRect.y = 700
    screen.blit(background, (0, 0)) #每次重绘背景图像，避免重影
    screen.blit(hero, heroRect)

    enemyGroup.update()
    enemyGroup.draw(screen)

    pygame.display.update()
    for event in pygame.event.get():  # 获取，并判断事件
        print(event)
        if event.type == pygame.QUIT:  # 如果获取到QUIT（退出）事件
            exit()  # 退出游戏

