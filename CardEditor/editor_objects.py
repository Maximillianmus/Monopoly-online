""" File containing all objects that are changeable """
import os
import pygame as pg

class EditorObject():
    """ Top class for objects that are editable in the card editor  """

    def __init__(self,image_path):
        self.background_image = pg.image.load(os.path.join('Data', image_path))
        self.card_rect = self.background_image.get_rect()
        #the initial position is probably gona have to change
        self.card_rect = self.card_rect.move(400,400)
    