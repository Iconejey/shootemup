import pygame as pg
import os, platform
from entities import Entity, Ship, Star
from math import sin

def getImgDict(path: str) -> dict:
	d = {}
	for file in os.listdir(path):
		if '.' in file:
			name, ext = file.split('.')
			if ext in ['jpg', 'png']:
				d[name] = pg.image.load(path + '/' + file).convert_alpha()
		else:
			d[file] = getImgDict(path + '/' + file)
	return d


if __name__ == "__main__":
	if 'Windows' in platform.platform():  # car pb de dpi sur windows
		from ctypes import windll
		windll.shcore.SetProcessDpiAwareness(1)

	pg.init()
	clock = pg.time.Clock()

	SCREEN_W, SCREEN_H = 1500, 900
	SCREEN = pg.display.set_mode((SCREEN_W, SCREEN_H))
	SCALE = 3

	images = getImgDict('../img')

	font = pg.font.Font('../Consolas.ttf', 24)
	bfont = pg.font.Font('../Consolas.ttf', 48)
	bfont.set_bold(True)
	
	player = Ship([SCREEN_W // 2, SCREEN_H // 2], images['player'])
	stars = [Star(SCREEN_W, SCREEN_H, SCALE) for i in range(100)]

	mode = 'menu'
	time = 0
	while mode:
		time += 1
		clock.tick(30)
		
		for e in pg.event.get():
			if e.type == pg.QUIT:
				mode = None
				continue

		keys_press = pg.key.get_pressed()
		mouse_press = pg.mouse.get_pressed()
		mouse_pos = pg.mouse.get_pos()

		SCREEN.fill([0, 0, 0])

		for star in stars:
			star.move(time)
			star.show(SCREEN)

		direction = [0, 0]

		if mode == 'menu':
			shoot_moop = bfont.render('Shoot Moop', False, [255, 255, 255, 128])
			SCREEN.blit(shoot_moop, [SCREEN_W // 2 - shoot_moop.get_size()[0] // 2, SCREEN_H // 4])

			press_start = font.render('Press [Enter] to start.', False, [255, 255, 255, abs(255 * sin(time/100))])
			SCREEN.blit(press_start, [SCREEN_W // 2 - press_start.get_size()[0] // 2, SCREEN_H * 3 // 4])

			if keys_press[pg.K_RETURN]:
				mode = 'game'
			
		if mode == 'game':
			if keys_press[pg.K_w]: direction[1] -= 1
			if keys_press[pg.K_s]: direction[1] += 1
			if keys_press[pg.K_a]: direction[0] -= 1
			if keys_press[pg.K_d]: direction[0] += 1

			player.aimTo(*mouse_pos)

		player.move(*direction)
		player.animate(time)
		player.show(SCREEN, SCALE)
		
		pg.display.update()