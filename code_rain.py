# * coding=utf8
# Python(pygame)实现代码雨
# 今日头条: 明哥读世界
# 微博：明哥读世界
# 个人博客:https://www.mylasting.com
#
import sys
import random
import pygame
from pygame.locals import *

# 屏幕大小
WIDTH = 800
HEIGHT = 600
# 下落速度范围
SPEED = [20, 40]
# CODE String列表
LEN = ['PHP', 'Python', 'C++', 'Java', 'C#', 'javascript', 'GoLang', 'Ruby', 'Android', 'Vue', 'swift', 'basic', '.net']


# 随机生成一个颜色
def randomColor():
    return (0, 238, 0)
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# 随机生成一个速度
def randomSpeed():
    return random.randint(SPEED[0], SPEED[1])


# 随机生成一个位置
def randomPos():
    return (random.randint(0, WIDTH), -20)


# 随机生成一个字符串
def randomCode():
    return LEN[random.randint(1, len(LEN)) - 1]


# 随机生成字体大小
def randomSize():
    return random.randint(12, 36)


# 定义代码精灵类
class Code(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.code = randomCode()
        self.font = pygame.font.Font('./font.ttf', randomSize())
        self.speed = randomSpeed()
        self.image = self.font.render(self.code, True, randomColor())
        self.image = pygame.transform.rotate(self.image, random.randint(90, 90))  # 以垂直方式下落
        self.rect = self.image.get_rect()
        self.rect.topleft = randomPos()

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.top > HEIGHT:
            # 当精灵位置超出屏幕，销毁
            self.kill()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('code_rain - 明哥读世界')
clock = pygame.time.Clock()
codesGroup = pygame.sprite.Group()
while True:
    clock.tick(24)  # 帧数
    for event in pygame.event.get():
        # 监听关闭事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
    screen.fill((1, 1, 1))  # 填充背景色，相当于clear
    # 新建一个精灵
    codeobject = Code()
    codesGroup.add(codeobject)
    # 监控并销毁
    codesGroup.update()
    codesGroup.draw(screen)
    pygame.display.update()
