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
    def __init__(self, image_name, image_dict, screen ,x, y):
        Ui.__init__(self, image_name, image_dict, screen ,x, y)
        self.color_key_dict = {}
        self.image_dict = image_dict
        self.text_fields_dict = {}
        self.number_dict = {}
        self.tag_list = []
        self.image_element_dict = {}

    def add_color_pair(self, key, color):
        self.color_key_dict[key] = color

    def remove_color_pair(self, key):
        self.color_key_dict.pop(key)

    def add_text(self, text, text_tag):
        self.text_fields_dict[text_tag] = text

    def remove_text(self, text_tag):
        self.text_fields_dict.pop(text_tag)
    
    def add_number(self, number_tag, number):
        self.number_dict[number_tag] = number
    
    def remove_number(self, number_tag):
        self.number_dict.pop(number_tag)

    def add_tag(self):
        pass

    def remove_tag(self):
        pass

    def add_image(self, image_name):
        self.image_element_dict[image_name] = self.image_dict[image]

    def remove_image(self, image_name):
        self.image_element_dict.pop(image_name)

    def update(self):
        pass

    def load_from_xml(self):
        pass

    def save_to_xml(self):
        pass

    def get_images(self):
        pass

    def get_numbers(self):
        pass
    
    def get_color_pairs(self):
        pass

    def get_tags(self):
        pass

class decals(Ui):
    """ decorative/non-functional images """
    def __init__(self, image_name, image_dict, screen ,x, y):
        Ui.__init__(self, image_name, image_dict, screen ,x, y)
