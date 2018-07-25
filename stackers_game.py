from __future__ import division
import time
import sys
import pygame
import random
from sense_hat import SenseHat
from pygame.locals import *
sense=SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		self.gaming=True

	def startGame(self):
		pygame.time.set_timer(USEREVENT +1,1000)
		column=0
		row=7
		speed=0.3
		yellow=(255,255,0)
		blue=(0,0,255)

		message="Game Over"
		while self.gaming:
			for event in pygame.event.get():
				color = "%06x" % random.randint(0, 0xFFFFFF)
				h = (color).lstrip('#')
				color=( tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))
				if event.type==KEYDOWN:
					sense.set_pixel(column , row,(0,0,255))
					row-=1
					column = 0
					if row <0:
						 self.gaming = False
						 sense.show_message(message, .08,text_colour=yellow,back_colour=blue)
						 sense.clear()
						 X = (255, 0, 0)  # Red
						 O = (255, 255, 255)  # White

						 question_mark = [
						 X, O, O, X, X, O, O, X,
						 O, O, X, O, O, X, O, O,
						 O, O, O, O, O, X, O, O,
						 O, O, O, O, X, O, O, O,
						 O, O, O, X, O, O, O, O,
						 O, O, O, X, O, O, O, O,
						 O, O, O, O, O, O, O, O,
						 X, O, O, X, O, O, O, X
						 ]
						 sense.set_pixels(question_mark)
						 time.sleep(4)
					         sense.show_message(" Just Kidding Your a Winner......ish",.08,text_colour=(191,0,0),back_colour=(color))
						 time.sleep(3)
						 sense.clear()
				else:
					sense.set_pixel(column,row,(color))
					time.sleep(.3)
					sense.set_pixel(column,row,(0,0,0))
					time.sleep(speed)
					speed = random.randint(1,20)/10
					column +=1
					if column== 8:
						column =0

if __name__=="__main__":
	try:
		game=stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
