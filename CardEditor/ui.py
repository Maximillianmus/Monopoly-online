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
    def __init__(self, font, screen, input_box, text_color=pg.Color("black"), active_color=pg.Color("blue") ):
        self.rect = input_box
        #rect used for creating the perimeter around the textbox
        self.box_perimiter = pg.Rect(0,0, input_box.w-1, input_box.h-1)

        self.font = font
        self.active = False
        self.screen = screen
        self.text_color = text_color
        self.active_color = active_color
        self.bg_color = pg.Color("white")
        self.text = ""
        self.text_changed = False
        self.textbox_surface = pg.Surface((self.rect.w , self.rect.h))
        self.update()

    def update(self):
        self.textbox_surface.fill(self.bg_color)

        width = 4
        if not self.active:
            pg.draw.rect(self.textbox_surface, self.text_color, self.box_perimiter, width)
            self.textbox_surface.set_at((self.rect.w-1, self.rect.h-1), self.text_color)
        else:
            pg.draw.rect(self.textbox_surface, self.active_color, self.box_perimiter, width)
            self.textbox_surface.set_at((self.rect.w-1, self.rect.h-1), self.active_color)
    
        self.textbox_surface.blit(self.font.render(self.text, True, self.text_color), (self.box_perimiter.x+5 , self.box_perimiter.y+5))
        
        self.image = image.Image("text_box_surface", self.textbox_surface)

    def if_clicked(self, pos):
        if self.rect.collidepoint(pos):
            # Toggle the active variable.
            self.change_state()
            self.update()
        else:
            self.deactivate()
            self.update()
    
    def update_text(self, text):
        if text != self.text:
            self.text = text
            self.text_changed = True

    def get_text(self):
        return self.text

    def change_state(self):
        self.active = not self.active

    def deactivate(self):
        self.active = False

    def render(self):
        if self.text_changed:
            self.update()
            self.text_changed = False
        self.image.render_static(self.screen, self.rect)

#TODO implement a way to send out a signal that something has changed
class Button(Ui):
    """ Toggable button"""
    def __init__(self, font, screen, button_box, text,text_color=pg.Color("black"),button_color=pg.Color("white") 
    ,active_color=pg.Color("blue"), active_text_color=pg.Color("white")):
        self.font = font
        self.text = text
        self.screen = screen
        self.rect = button_box
        self.box_perimiter = pg.Rect(0,0, button_box.w-1, button_box.h-1)
        self.text_color = text_color
        self.active_color = active_color
        self.button_color = button_color
        self.active_text_color = active_text_color
        #show if the button has been pressed
        self.active = False
        #says if the button is functional, button can be turned off by making this false
        self.button_active = True
        self.button_surface = pg.Surface((self.rect.w , self.rect.h))
        self.update()

    def update(self):
        """ method that uppdates the image for the button"""
        if not self.active:
            self.button_surface.fill(self.button_color)
            text_img = self.font.render(self.text, True, self.text_color)
        else:
            self.button_surface.fill(self.active_color)
            text_img = self.font.render(self.text, True, self.active_text_color)

        pg.draw.rect(self.button_surface, self.text_color, self.box_perimiter, 4)
        self.button_surface.set_at((self.rect.w-1, self.rect.h-1), self.text_color)

        text_rect = text_img.get_rect(center=(self.rect.w/2, self.rect.h/2))
        
        self.button_surface.blit(text_img,text_rect)
        self.image = image.Image("button_surface", self.button_surface)


    def if_clicked(self, pos):
        """checks if the button has been clicked and toggles it if it has"""
        if self.rect.collidepoint(pos):
            self.toggle()

    def toggle(self):
        """ Toggles the button if it is active"""
        if self.button_active:
            self.active = not self.active
            self.update()

    def detoggle(self):
        self.active = False

    def change_text(self, text):
        """ Changes the text in the button"""
        self.text = text
        self.update()

    def toggle_button_func(self):
        """ turnes the button on/off"""
        self.button_active = not self.button_active

class PressButton(Button):
    """ Pressable button that automaticly unpresses(not toggle )"""
    def __init__(self, font, screen, button_box, text,text_color=pg.Color("black"),button_color=pg.Color("white") 
    ,active_color=pg.Color("blue"), active_text_color=pg.Color("white")):

        #init from Button
        Button.__init__(self, font, screen, button_box, text,text_color=pg.Color("black"),button_color=pg.Color("white") 
        ,active_color=pg.Color("blue"), active_text_color=pg.Color("white"))
        self.time_of_press = 0

    #overwritten method
    def if_clicked(self, pos):
        """checks if the button has been clicked and toggles it if it has"""
        if self.rect.collidepoint(pos):
            self.toggle()
            self.time_of_press = pg.time.get_ticks()

    #overwritten method
    def render(self):
        if (pg.time.get_ticks() - self.time_of_press ) > 20 and self.active:
            self.detoggle()
            self.update()
        self.image.render_static(self.screen, self.rect)


class SelectionList(Ui):
    """ List where you can make a selection """

class EditorObject(Ui):
    """ Image in the preview window """
    def __init__(self, image_name, image_dict, screen ,x, y):
        Ui.__init__(self, image_name, image_dict, screen ,x, y)
        self.color_key_dict = {}
        self.image_dict = image_dict
        self.text_fields_dict = {}
        self.number_dict = {}
        self.tag_list = []
        self.image_element_dict = {}
        self.final_image = self.image

    def render(self):
        self.final_image.render_static(self.screen, self.rect)

    def add_color_pair(self, color_key, color):
        self.color_key_dict[color_key] = color

    def remove_color_pair(self, color_key):
        self.color_key_dict.pop(color_key)

    def add_text(self, text, text_tag):
        self.text_fields_dict[text_tag] = text

    def remove_text(self, text_tag):
        self.text_fields_dict.pop(text_tag)
   
    def add_number(self, number_tag, number):
        self.number_dict[number_tag] = number
   
    def remove_number(self, number_tag):
        self.number_dict.pop(number_tag)

    def add_tag(self, tag):
        self.tag_list.append(tag)

    def remove_tag(self, tag_index):
        self.tag_list.pop(tag_index)

    def add_image(self, image_name):
        self.image_element_dict[image_name] = self.image_dict[image_name]

    def remove_image(self, image_name):
        self.image_element_dict.pop(image_name)
    
    # TODO: Implement the following three functions
    def update(self):
        pass

    def load_from_xml(self):
        pass

    def save_to_xml(self):
        pass

    def get_images(self):
        return self.image_element_dict.copy()

    def get_numbers(self):
        return self.number_dict.copy()

    def get_color_pairs(self):
        return self.color_key_dict.copy()

    def get_tags(self):
        return self.tag_list.copy()

class Decals(Ui):
    """ decorative/non-functional images """
    def __init__(self, image_name, image_dict, screen ,x, y):
        Ui.__init__(self, image_name, image_dict, screen ,x, y)
