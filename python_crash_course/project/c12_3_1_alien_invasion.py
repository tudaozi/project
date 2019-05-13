#!/usr/bin/env python
# coding=UTF-8
'''
@Description: S
@Author: StaURL
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-05-10 17:11:24
@LastEditTime: 2019-05-10 17:39:02
'''
import sys
import pygame


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
