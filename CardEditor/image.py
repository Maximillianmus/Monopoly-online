""" file that contains setup for image rendering"""
import os
import pygame as pg

# om en bild inte har laddats förut laddar den in den i minnet i form av ett dictionary
# annars hämtar den bilden från dictionary
def get_image(image_dictionary, path):
    """ Returns an image at a specific path from the image_dicionary,
     if the image is not loaded it will be loaded to a dictonary and then returned """
    image = image_dictionary.get(path)
    if image is None:
        image = pg.image.load(os.path.join('Images', path))
        image_dictionary[path] = image
    return image

def create_image_class_dict(directory):
    """ returns a dictionary containing all images in a specified directory"""
    paths = os.listdir(directory)
    image_class_list = {}
    for file_name in paths:
        image = pg.image.load(os.path.join(directory, file_name))
        picture_class = Image(file_name, image)
        image_class_list[file_name] = picture_class
    return image_class_list

class Image:
    """ Image class used to manage rendering of images"""
    def __init__(self, path, image):
        self.path = path
        self.image = image
        self.rect = image.get_rect()

    def get_image(self):
        """ returns the image of this object """
        return self.image

    def render_dynamic(self, screen, game_object_rect, camera):
        """ renders the image relative to the camera, the game object rect should have the same size as the the image"""
        rect = self.rect.move(game_object_rect.x - camera.w, game_object_rect.y - camera.h)

        if rect.colliderect(camera):
            image = self.get_image()
            screen.blit(image,rect)


    def render_static(self, screen, game_object_rect):
        """ renders the image directly onto the screen, with no consideration for the camera, the game object rect should have the same size as the the image """
        rect = self.rect.move(game_object_rect.x, game_object_rect.y)
        image = self.get_image()
        screen.blit(image,rect)


