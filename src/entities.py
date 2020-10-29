import pygame as pg

class Entity:
    def __init__(self, pos: tuple, img_bnk: dict, act_img: str):
        self.x, self.y = pos
        self.img_bnk = img_bnk
        self.act_img = act_img

    @staticmethod
    def rotate(img: pg.Surface, angle: float = 0):
        center = img.get_rect().center
        rot_img = pg.transform.rotate(img, angle)
        new_rect = rot_img.get_rect(center = center)

        return rot_img, new_rect

    def draw(self, s: pg.Surface, angle: float = 0, scale: float = 1) -> None:
        img = self.img_bnk[self.act_img]
        img = pg.transform.scale(img, [img.get_width() * scale, img.get_height() * scale])
        s.blit(*Entity.rotate(img, angle))