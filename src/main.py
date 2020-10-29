import pygame as pg
import os, platform
from entities import Entity

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

	SCREEN_W, SCREEN_H = 900, 600
	SCREEN = pg.display.set_mode((SCREEN_W, SCREEN_H))
	SCALE = 3

	images = getImgDict('../img')
	
	player = Entity([100, 100], images['player'], 'ship_0')
	print(player.x, player.y)

	mode = 'game'
	time = 0
	while mode:
		time += 1
		for e in pg.event.get():
			if e.type == pg.QUIT:
				mode = None
				continue

		keys_press = pg.key.get_pressed()
		mouse_pess = pg.mouse.get_pressed()
		mouse_pos = pg.mouse.get_pos()

		SCREEN.fill([0, 0, 0])

		player.draw(SCREEN, time / 10, SCALE)
		
		pg.display.update()