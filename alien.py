#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 14:14
# @Author : 王志宝
# @Site : 
# @File : alien.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('image/alien.bmp')		#加载图像，得到属性
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width		#每个外星人最初在屏幕左上角
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)		#存储外星人位置

	def blitme(self):		#在指定位置绘制外星人
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):		#向右移动外星人
		self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
		self.rect.x = self.x



