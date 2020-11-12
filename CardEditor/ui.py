""" Classes for the UI elements """
import pygame as pg
import image

class Ui:
    """ basic ui element """
    def __init__(self, image_name, image_dict, screen ,x, y):
        self.image = image_dict[image_name]
        self.rect = self.image.get_rect()
        self.rect.move(x,y)
        self.screen = screen

    def render(self): 
        self.image.render_static(self.screen, self.rect)

class Text(Ui):
    """ static text """
    def __init__(self, font, text, x, y, screen,color=pg.Color("black")):
        text_image = font.render(text, True, color)
        self.image = image.Image(text, text_image)
        self.rect = self.image.get_rect()
        self.rect.move(x,y)
        self.screen = screen

class TextBox(Ui):
    """ a box where you can write """

class Button(Ui):
    """ Pressable button"""

class SelectionList(Ui):
    """ List where thou can make a selection """

class DynamicImage(Ui):
    """ Image in the preview window """

class decals(Ui):
    """ decorative/non-functional images """
    def __init__(self, image_name, image_dict, screen ,x, y):
        Ui.__init__(self, image_name, image_dict, screen ,x, y)
